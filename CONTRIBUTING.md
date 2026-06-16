# Contributing to TCASVS

Thank you for your interest in contributing to the OWASP Thick Client Application Security Verification Standard (TCASVS).

## Getting Started

1. [Join](http://owasp.org/slack/invite) the [OWASP Slack workspace](https://owasp.slack.com) to connect with the community.
2. Review the standard in [`5.0/en/`](5.0/en/) to understand the current state.
3. Check [open issues](https://github.com/OWASP/TCASVS/issues) for tasks that need help.
4. Fork the repository and create a feature branch for your changes.

## How to Contribute

### Proposing New Requirements

1. Open an issue describing the security concern and why it belongs in the TCASVS.
2. Reference real-world attack scenarios or industry standards.
3. Propose a draft requirement following the format below.

### Requirement Format

All requirements must follow the ASVS 5.0.0 format conventions:

```markdown
| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V{ch}.{sec}.{item} | Verify that... | 1 | New |
```

- **IDs** follow `V{chapter}.{section}.{item}` numbering (e.g., V1.2.3)
- **Descriptions** start with "Verify that..."
- **Level** is the lowest level at which the requirement applies (`1`, `2`, or `3`)
- **Source** records the requirement's origin (`TASVS` for migrated, `New` for added)

### Level Definitions

- **L1** — Baseline: applicable to all thick client applications
- **L2** — Standard: for applications handling sensitive data
- **L3** — Advanced: for applications in hostile environments or high-security contexts

### Change Tracking

When modifying requirements in a PR, include change tags in the PR description:

- `[ADDED]` — New requirement
- `[MODIFIED]` — Wording change to existing requirement
- `[MOVED]` — Requirement moved between sections/chapters
- `[REMOVED]` — Requirement deleted (must include rationale)
- `[LEVEL_CHANGED]` — Level assignment changed

## Pull Request Guidelines

1. Reference the related issue in your PR description.
2. Changes to requirements must include rationale.
3. Do not modify the `archive/` folder (historical reference only).
4. Run markdown lint before submitting (see `.markdownlint.jsonc`).
5. One logical change per PR — don't mix requirement changes with formatting fixes.

## Code of Conduct

All contributors must abide by the [OWASP Code of Conduct](https://owasp.org/www-policy/operational/code-of-conduct).

Thank you for your interest in contributing to an OWASP project. We appreciate your efforts to help us improve and grow our projects.
