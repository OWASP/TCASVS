# TCASVS Build System
# Generates PDF, DOCX, JSON, CSV, XML, and CycloneDX outputs from source Markdown.

PROJDIR := $(realpath $(CURDIR))
TOOLSDIR := tools
TEMPLATEDIR := templates
SOURCEDIR := en
BUILDDIR := build
DISTDIR := dist

TARGETNAME := OWASP_Thick_Client_Application_Security_Verification_Standard_5.0.0_

# Source files
SOURCE_FILES := $(sort $(wildcard $(SOURCEDIR)/0x*.md $(SOURCEDIR)/0x*.yaml))
BUILD_FILES := $(patsubst $(SOURCEDIR)/%, $(BUILDDIR)/%, $(SOURCE_FILES))

# Output targets
MD_FILE := $(DISTDIR)/$(TARGETNAME)en.md
PDF_FILE := $(DISTDIR)/$(TARGETNAME)en.pdf
DOCX_FILE := $(DISTDIR)/$(TARGETNAME)en.docx
JSON_FILE := $(DISTDIR)/$(TARGETNAME)en.json
JSON_FLAT_FILE := $(DISTDIR)/$(TARGETNAME)en.flat.json
CSV_FILE := $(DISTDIR)/$(TARGETNAME)en.csv
XML_FILE := $(DISTDIR)/$(TARGETNAME)en.xml
CDX_FILE := $(DISTDIR)/$(TARGETNAME)en.cdx.json

EXPORT_TOOL := $(TOOLSDIR)/export.py

# Pandoc flags
PANDOC_PDF_FLAGS := -f markdown -s -t latex --pdf-engine=xelatex
PANDOC_DOCX_FLAGS := -s -t docx -f markdown --toc --columns 10000 \
	--reference-doc=$(TEMPLATEDIR)/reference.docx

.PHONY: all pdf docx json json_flat csv xml cdx_json md clean verify

all: md pdf docx json json_flat csv xml cdx_json

$(BUILDDIR):
	mkdir -p $@

$(DISTDIR):
	mkdir -p $@

# Stage source MD for the build
$(BUILDDIR)/%.md: $(SOURCEDIR)/%.md | $(BUILDDIR)
	cp $< $@

$(BUILDDIR)/%.yaml: $(SOURCEDIR)/%.yaml | $(BUILDDIR)
	cp $< $@

# Merged Markdown
md: $(MD_FILE)
$(MD_FILE): $(BUILD_FILES) | $(DISTDIR)
	pandoc -f gfm -s -t markdown -o $@ $(BUILDDIR)/0x*.md

# PDF via LaTeX
pdf: $(PDF_FILE)
$(PDF_FILE): $(BUILD_FILES) | $(DISTDIR)
	pandoc $(PANDOC_PDF_FLAGS) \
		--include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex \
		-o $@ --template $(TEMPLATEDIR)/eisvogel.tex \
		$(BUILDDIR)/0x*.md $(SOURCEDIR)/0x00-Header.yaml

# DOCX
docx: $(DOCX_FILE)
$(DOCX_FILE): $(BUILD_FILES) | $(DISTDIR)
	pandoc $(PANDOC_DOCX_FLAGS) -o $@ $(BUILDDIR)/0x*.md $(SOURCEDIR)/0x00-Header.yaml

# Structured exports via Python
json: $(JSON_FILE)
$(JSON_FILE): $(SOURCE_FILES) | $(DISTDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --format json --language $(SOURCEDIR) > $@

json_flat: $(JSON_FLAT_FILE)
$(JSON_FLAT_FILE): $(SOURCE_FILES) | $(DISTDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --format json_flat --language $(SOURCEDIR) > $@

csv: $(CSV_FILE)
$(CSV_FILE): $(SOURCE_FILES) | $(DISTDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --format csv --language $(SOURCEDIR) > $@

xml: $(XML_FILE)
$(XML_FILE): $(SOURCE_FILES) | $(DISTDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --format xml --language $(SOURCEDIR) > $@

cdx_json: $(CDX_FILE)
$(CDX_FILE): $(SOURCE_FILES) | $(DISTDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --format cdx_json --language $(SOURCEDIR) > $@

# Verification
verify: $(SOURCE_FILES)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --verify-only --format json --language $(SOURCEDIR)
	cd $(PROJDIR) && python3 $(EXPORT_TOOL) --verify-only --format csv --language $(SOURCEDIR)

# Clean
clean:
	rm -rf $(BUILDDIR) $(DISTDIR)
