#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TCASVS document parser and converter class.

Adapted from the ASVS parser by Bernhard Mueller, Jonny Schnittger, and Josh Grossman.
Modified for the TCASVS table format (| V1.2.3 | Description | Level | CWE | Source |).

Copyright (c) 2024 OWASP Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import re
import json
import csv
from xml.sax.saxutils import escape
from dicttoxml2 import dicttoxml

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class TCASVS:
    """Parser for TCASVS markdown files in ASVS 5.0.0 table format."""

    def __init__(self, language):
        self.language = language
        self.standard = {
            "Name": "Thick Client Application Security Verification Standard",
            "ShortName": "TCASVS",
            "Version": "",
            "Description": (
                "The OWASP Thick Client Application Security Verification Standard "
                "(TCASVS) provides a basis for testing thick client application technical "
                "security controls and provides developers with a list of requirements "
                "for secure development."
            ),
            "Requirements": [],
        }
        self.flat_requirements = []

        self._parse_version()
        self._parse_chapters()

    def _parse_version(self):
        """Extract version from the Frontispiece file."""
        frontispiece = os.path.join(self.language, "0x01-Frontispiece.md")
        version_regex = re.compile(r"Version\s+(([\d.]+){3})")
        if os.path.exists(frontispiece):
            with open(frontispiece, encoding="utf8") as f:
                for line in f:
                    m = version_regex.search(line)
                    if m:
                        self.standard["Version"] = m.group(1)
                        break

    def _parse_chapters(self):
        """Parse all chapter files matching the 0xNN-V pattern."""
        # Regex for the TCASVS table format:
        # | V1.2.3 | Description text | 1 | 123 | TASVS |
        req_regex = re.compile(
            r"^\|\s*V([\d.]+)\s*\|"       # ID (e.g., V1.2.3)
            r"\s*(.*?)\s*\|"               # Description
            r"\s*([123]?)\s*\|"           # Level (1, 2, 3, or blank)
            r"\s*([0-9,\s]*)\s*\|"         # CWE
        )

        chapter_heading_regex = re.compile(r"^#\s+V(\d+)\s+(.*)")
        section_regex = re.compile(r"^##\s+V(\d+)\.(\d+)\s+[—–-]\s+(.*)")
        # Also match section headings without dash: ## V2.1 Section Name
        section_regex_alt = re.compile(r"^##\s+V(\d+)\.(\d+)\s+(.*)")
        filename_regex = re.compile(r"0x\d{2}-(V(\d+))-(.*)")

        for file in sorted(os.listdir(self.language)):
            if not re.match(r"0x\d{2}-V", file):
                continue

            m = filename_regex.search(file)
            if not m:
                continue

            chapter = {
                "Shortcode": m.group(1),
                "Ordinal": int(m.group(2)),
                "ShortName": m.group(3).replace("-", " "),
                "Name": "",
                "Items": [],
            }

            current_section = None

            with open(os.path.join(self.language, file), encoding="utf8") as f:
                for line in f:
                    # Chapter heading
                    ch_match = chapter_heading_regex.match(line)
                    if ch_match:
                        chapter["Name"] = ch_match.group(2).strip()
                        continue

                    # Section heading (with dash separator)
                    sec_match = section_regex.match(line)
                    if not sec_match:
                        sec_match = section_regex_alt.match(line)
                    if sec_match:
                        current_section = {
                            "Shortcode": f"V{sec_match.group(1)}.{sec_match.group(2)}",
                            "Ordinal": int(sec_match.group(2)),
                            "Name": sec_match.group(3).strip(),
                            "Items": [],
                        }
                        chapter["Items"].append(current_section)
                        continue

                    # Requirement row
                    req_match = req_regex.match(line)
                    if req_match and current_section is not None:
                        req_id = req_match.group(1)
                        description = req_match.group(2).strip()
                        level_str = req_match.group(3).strip()
                        cwe_str = req_match.group(4).strip()

                        # Derive per-level applicability from the single
                        # numeric Level column (lowest applicable level).
                        int_level = int(level_str) if level_str.isdigit() else 99
                        l1 = "✓" if int_level <= 1 else ""
                        l2 = "✓" if int_level <= 2 else ""
                        l3 = "✓" if int_level <= 3 else ""

                        cwe_list = [
                            int(c.strip())
                            for c in cwe_str.split(",")
                            if c.strip().isdigit()
                        ]

                        req = {
                            "Shortcode": f"V{req_id}",
                            "Ordinal": int(req_id.rsplit(".", 1)[1]),
                            "Description": description,
                            "L1": {"Required": l1 == "✓", "Requirement": l1},
                            "L2": {"Required": l2 == "✓", "Requirement": l2},
                            "L3": {"Required": l3 == "✓", "Requirement": l3},
                            "CWE": cwe_list,
                        }

                        current_section["Items"].append(req)

                        # Flat representation
                        self.flat_requirements.append({
                            "chapter_id": chapter["Shortcode"],
                            "chapter_name": chapter["Name"],
                            "section_id": current_section["Shortcode"],
                            "section_name": current_section["Name"],
                            "req_id": f"V{req_id}",
                            "req_description": description,
                            "level1": l1,
                            "level2": l2,
                            "level3": l3,
                            "cwe": cwe_str,
                        })

            self.standard["Requirements"].append(chapter)

    # --- Export methods ---

    def to_json(self):
        """Export as structured JSON."""
        return json.dumps(self.standard, indent=2, ensure_ascii=False)

    def to_json_flat(self):
        """Export as flat JSON array of requirements."""
        output = {
            "Name": self.standard["Name"],
            "ShortName": self.standard["ShortName"],
            "Version": self.standard["Version"],
            "requirements": self.flat_requirements,
        }
        return json.dumps(output, indent=2, ensure_ascii=False)

    def to_csv(self):
        """Export as CSV."""
        si = StringIO()
        writer = csv.writer(si)
        writer.writerow([
            "chapter_id", "chapter_name", "section_id", "section_name",
            "req_id", "req_description", "level1", "level2", "level3", "cwe",
        ])
        for req in self.flat_requirements:
            writer.writerow([
                req["chapter_id"],
                req["chapter_name"],
                req["section_id"],
                req["section_name"],
                req["req_id"],
                req["req_description"],
                req["level1"],
                req["level2"],
                req["level3"],
                req["cwe"],
            ])
        return si.getvalue()

    def to_xml(self):
        """Export as XML."""
        xml_str = dicttoxml(self.standard, custom_root="tcasvs", attr_type=False)
        return xml_str.decode("utf-8")

    def verify_json(self, json_str):
        """Verify JSON output is valid and contains expected structure."""
        try:
            data = json.loads(json_str)
            assert "Requirements" in data
            assert len(data["Requirements"]) > 0
            total_reqs = sum(
                len(req["Items"])
                for chapter in data["Requirements"]
                for req in chapter["Items"]
            )
            return f"OK: {len(data['Requirements'])} chapters, {total_reqs} requirements"
        except (json.JSONDecodeError, AssertionError, KeyError) as e:
            return f"FAIL: {e}"

    def verify_csv(self, csv_str):
        """Verify CSV output."""
        reader = csv.reader(StringIO(csv_str))
        rows = list(reader)
        if len(rows) < 2:
            return "FAIL: No data rows"
        return f"OK: {len(rows) - 1} requirements"
