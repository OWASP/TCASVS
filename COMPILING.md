# Compiling the TCASVS

## Using GitHub Actions (Recommended)

The repository includes a GitHub Actions workflow that automatically compiles the standard into PDF format on push and pull requests. This is the recommended approach as it ensures reproducible builds.

## Local Build

### Prerequisites

- Docker (recommended) OR:
  - Pandoc 3.x+
  - LaTeX distribution (texlive-full or equivalent)
  - Python 3.10+

### Using Docker

```bash
cd 5.0
docker run --rm -v "$(pwd):/data" pandoc/extra:latest \
  --defaults=defaults.yaml -o TCASVS_5.0.0_en.pdf
```

### Using Make (when available)

```bash
make
```

## Output Formats

The build system generates:
- **PDF** — For reading and distribution
- **CSV** — For importing into testing tools and spreadsheets
- **JSON** — For programmatic consumption and tooling integration

## Folder Structure

```
5.0/
├── en/           ← Markdown source files (edit these)
├── mappings/     ← ID mapping from old TASVS to TCASVS
├── templates/    ← LaTeX and Word templates for PDF/DOCX generation
└── tools/        ← Build scripts (export.py, cyclonedx.py, etc.)
```
