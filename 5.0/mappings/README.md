# TCASVS Mapping Files

This directory contains machine-readable mappings between the original TASVS requirement IDs and the new TCASVS v5.0.0 structure.

## Files

| File | Direction | Format |
|------|-----------|--------|
| `mapping_tasvs_to_tcasvs_v5.0.0.yml` | TASVS → TCASVS v5.0.0 | YAML |

## Actions

Each entry specifies one of the following actions:

| Action | Meaning |
|--------|---------|
| `rename` | Requirement kept in the same logical location, reworded for ASVS format |
| `move` | Requirement moved to a different chapter (new ID in a different Vx.y.z) |
| `drop` | Requirement removed (not verifiable, out of scope, or absorbed by another) |
| `add` | New requirement with no TASVS predecessor (gap fill) |

## Usage

These mappings enable:
- Automated migration of existing TASVS assessment results to TCASVS IDs
- Traceability audits for compliance programs transitioning from TASVS to TCASVS
- Tooling that generates comparison reports between old and new assessments

## Format

```yaml
tasvs-arch-1-1:
  action: rename
  tcasvs-id: V1.1.1
  cwe: 1053
  notes: "Brief rationale for the change"
```

New requirements (no TASVS predecessor) use a `new-` prefix:

```yaml
new-V1.3.1:
  action: add
  tcasvs-id: V1.3.1
  cwe: 250
  rationale: "Gap: thick clients need privilege separation documentation"
```
