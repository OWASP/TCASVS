#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CycloneDX converter for TCASVS.

Converts the TCASVS JSON into CycloneDX Standards format (spec 1.6).

Adapted from the ASVS CycloneDX converter.
Copyright (c) 2024 OWASP Foundation
Licensed under MIT. See tcasvs.py for full license text.
"""

import json
import datetime
import uuid


class CycloneDX:
    """Convert TCASVS structured JSON to CycloneDX 1.6 Standards format."""

    def __init__(self, tcasvs_json_str):
        self.tcasvs = json.loads(tcasvs_json_str)

        self.bom = {
            "bomFormat": "CycloneDX",
            "specVersion": "1.6",
            "serialNumber": f"urn:uuid:{uuid.uuid4()}",
            "version": 1,
            "metadata": {
                "timestamp": datetime.datetime.now()
                .astimezone()
                .replace(microsecond=0)
                .isoformat(),
                "licenses": [
                    {
                        "license": {
                            "id": "CC-BY-SA-4.0",
                            "url": "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt",
                        }
                    }
                ],
                "supplier": {
                    "name": "OWASP Foundation",
                    "url": ["https://owasp.org"],
                },
            },
            "declarations": {"standards": [{}]},
        }

        standard = self.bom["declarations"]["standards"][0]
        bom_ref = f"{self.tcasvs['ShortName']}-{self.tcasvs['Version']}"
        standard["bom-ref"] = bom_ref
        standard["name"] = self.tcasvs["Name"]
        standard["version"] = self.tcasvs["Version"]
        standard["description"] = self.tcasvs["Description"]
        standard["owner"] = self.tcasvs["Name"]

        requirements = []
        l1_reqs = []
        l2_reqs = []
        l3_reqs = []

        for chapter in self.tcasvs.get("Requirements", []):
            chapter_req = self._convert_requirement(chapter, None)
            requirements.append(chapter_req)
            for section in chapter.get("Items", []):
                section_req = self._convert_requirement(section, chapter_req["bom-ref"])
                requirements.append(section_req)
                for item in section.get("Items", []):
                    item_req = self._convert_requirement(item, section_req["bom-ref"])
                    requirements.append(item_req)
                    # Determine level
                    if item.get("L1", {}).get("Required"):
                        l1_reqs.append(item_req["bom-ref"])
                    elif item.get("L2", {}).get("Required"):
                        l2_reqs.append(item_req["bom-ref"])
                    elif item.get("L3", {}).get("Required"):
                        l3_reqs.append(item_req["bom-ref"])

        standard["requirements"] = requirements
        standard["levels"] = [
            {
                "bom-ref": "level-1",
                "identifier": "Level 1",
                "description": "Minimum security baseline for all thick client applications.",
                "requirements": l1_reqs,
            },
            {
                "bom-ref": "level-2",
                "identifier": "Level 2",
                "description": "Standard security for applications handling sensitive data.",
                "requirements": l2_reqs,
            },
            {
                "bom-ref": "level-3",
                "identifier": "Level 3",
                "description": "Maximum security for critical applications in adversarial environments.",
                "requirements": l3_reqs,
            },
        ]

    def _convert_requirement(self, item, parent_ref):
        """Convert a chapter/section/requirement to CycloneDX requirement format."""
        req = {
            "bom-ref": item.get("Shortcode", ""),
            "identifier": item.get("Shortcode", ""),
            "title": item.get("Name", item.get("Description", "")),
        }
        if "Description" in item:
            req["text"] = item["Description"]
        if parent_ref:
            req["parent"] = parent_ref
        return req

    def to_json(self):
        """Export CycloneDX BOM as JSON string."""
        return json.dumps(self.bom, indent=2, ensure_ascii=False)
