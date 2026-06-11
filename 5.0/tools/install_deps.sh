#!/bin/bash
# Install dependencies for TCASVS document generation.

set -e

echo "Installing TCASVS build dependencies..."

# System packages
if command -v apt-get &>/dev/null; then
    sudo apt-get update -qq
    sudo apt-get install -y pandoc python3 python3-pip texlive-xetex
elif command -v brew &>/dev/null; then
    brew install pandoc python3
    brew install --cask mactex-no-gui
else
    echo "Please install pandoc, python3, and texlive-xetex manually."
fi

# Python packages
pip3 install --user dicttoxml2

echo "Done. Run 'make' from the 5.0/ directory to build all outputs."
