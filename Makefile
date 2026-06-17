# TCASVS top-level build driver.
#
# Builds (or pulls) the document builder image defined in docker/Dockerfile and
# runs the chapter build (5.0/Makefile) inside it, so PDF/DOCX output uses the
# correct pandoc, LaTeX packages, and pinned fonts.
#
# Usage:
#   make 5.0                 # build all output formats for English
#   make 5.0 FORMATS=pdf     # build only the PDF
#   make verify              # parse-check the requirements
#   make 5.0-clean           # remove build/ and dist/
#

FORMATS ?= all
LANGS ?= en
IMAGE := ghcr.io/owasp/tcasvs/documentbuilder:latest

MOUNTS = -v "$(CURDIR)/5.0:/data" -v "$(CURDIR)/docker:/scripts"

.PHONY: all latest 5.0 5.0-clean verify docker

latest: 5.0
all: 5.0

5.0: docker
	docker run --rm --user $$(id -u):$$(id -g) $(MOUNTS) \
		-e "TARGET=5.0" -e "FORMATS=$(FORMATS)" -e "LANGS=$(LANGS)" $(IMAGE)

verify: docker
	docker run --rm --user $$(id -u):$$(id -g) $(MOUNTS) \
		-e "TARGET=verify" $(IMAGE)

5.0-clean: docker
	docker run --rm --user $$(id -u):$$(id -g) $(MOUNTS) \
		-e "TARGET=clean" $(IMAGE)

docker:
	docker pull $(IMAGE) || docker build --pull --tag $(IMAGE) --network host docker
