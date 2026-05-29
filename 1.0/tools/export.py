#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Export TCASVS requirements to various formats (JSON, CSV, XML, CycloneDX).

Usage:
    python export.py --format json --language en
    python export.py --format csv --language en
    python export.py --format xml --language en
    python export.py --format cdx_json --language en
    python export.py --verify-only --format json --language en

Copyright (c) 2024 OWASP Foundation
Licensed under MIT. See tcasvs.py for full license text.
"""

import argparse
from tcasvs import TCASVS
from cyclonedx import CycloneDX

parser = argparse.ArgumentParser(description="Export TCASVS requirements.")
parser.add_argument(
    "--format",
    choices=["json", "json_flat", "xml", "csv", "cdx_json"],
    default="json",
)
parser.add_argument("--language", default="en")
parser.add_argument("--verify-only", action="store_true")

args = parser.parse_args()

m = TCASVS(args.language)

if args.verify_only:
    if args.format == "csv":
        print(m.verify_csv(m.to_csv()))
    else:
        print(m.verify_json(m.to_json()))
else:
    if args.format == "csv":
        print(m.to_csv())
    elif args.format == "xml":
        print(m.to_xml())
    elif args.format == "json_flat":
        print(m.to_json_flat())
    elif args.format == "cdx_json":
        cdx = CycloneDX(m.to_json())
        print(cdx.to_json())
    else:
        print(m.to_json())
