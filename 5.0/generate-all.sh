#!/bin/bash
# Generate all TCASVS output formats.
# Run from the 5.0/ directory.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== TCASVS Document Generation ==="
echo ""

# Check prerequisites
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 is required. Run tools/install_deps.sh first."
    exit 1
fi

# Always generate structured exports (no pandoc needed)
echo "Generating JSON..."
make json

echo "Generating flat JSON..."
make json_flat

echo "Generating CSV..."
make csv

echo "Generating XML..."
make xml

echo "Generating CycloneDX..."
make cdx_json

# PDF/DOCX require pandoc + LaTeX
if command -v pandoc &>/dev/null; then
    echo "Generating DOCX..."
    make docx

    if command -v xelatex &>/dev/null; then
        echo "Generating PDF..."
        make pdf
    else
        echo "Skipping PDF (xelatex not found). Install texlive-xetex for PDF output."
    fi
else
    echo "Skipping PDF/DOCX (pandoc not found). Install pandoc for document outputs."
fi

echo ""
echo "Verifying outputs..."
make verify

echo ""
echo "Done. Outputs in 5.0/dist/"
