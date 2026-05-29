# Preface

## Welcome to TCASVS 1.0

The OWASP Thick Client Application Security Verification Standard (TCASVS) provides a comprehensive set of security requirements for designing, developing, and testing thick client applications — desktop software, native applications, and other locally-executed programs that operate outside a browser sandbox.

This standard fills the gap between the [OWASP Application Security Verification Standard (ASVS)](https://github.com/OWASP/ASVS) for web applications and the [Mobile Application Security Verification Standard (MASVS)](https://github.com/OWASP/owasp-masvs). While these standards cover their respective domains well, thick client applications face a distinct combination of threats: they execute on user-controlled hardware, interact with local operating system resources, communicate over untrusted networks, and often run with elevated privileges.

## What Changed from TASVS

TCASVS 1.0 represents a complete restructuring of the original Thick Application Security Verification Standard (TASVS). Key changes include:

- **Requirement ID format**: Adopted ASVS numbering (`V{chapter}.{section}.{item}`) replacing the old `TASVS-{CATEGORY}-{group}.{item}` scheme.
- **Level definitions**: Clarified L1/L2/L3 applicability per requirement with explicit checkmarks, replacing the old X/blank notation.
- **CWE traceability**: Every requirement now maps to a CWE identifier.
- **Expanded coverage**: From 79 original requirements to over 130 across 6 chapters, with significant gap-fills for build security, memory safety, IPC, and runtime integrity.
- **Chapter restructuring**: Reorganized into chapters that align with ASVS conventions while remaining specific to thick client threats.

## Chapter Structure

| Chapter | Title | Focus |
|---------|-------|-------|
| V1 | Architecture and Threat Modeling | Threat models, security architecture, attack surface management |
| V2 | Build, Deployment, and Environment Hardening | Supply chain, compiler mitigations, installers, privilege management |
| V3 | Data Storage and Protection | Data classification, file storage, credentials, memory, temp data |
| V4 | Code Quality and Exploit Mitigation | Input validation, memory safety, deserialization, runtime integrity |
| V5 | Cryptography | Algorithms, key management, random values, transport crypto |
| V6 | Network Communication | TLS, service exposure, data leakage, IPC, license validation |

## Security Verification Levels

The TCASVS defines three verification levels:

- **Level 1 (L1)** — Baseline security appropriate for all thick client applications. These requirements address the most common and easily exploitable weaknesses.
- **Level 2 (L2)** — Standard security for applications that handle sensitive data or operate in higher-risk environments. Includes defense-in-depth measures and assumes a more capable adversary.
- **Level 3 (L3)** — Advanced security for applications operating in hostile environments, handling highly sensitive data, or requiring resistance to targeted attacks by skilled adversaries with physical access and reverse engineering capabilities.

## How to Use This Standard

The TCASVS can be used as:

1. **A development guide** — Requirements inform secure design decisions during architecture and implementation.
2. **A verification checklist** — Security testers use requirements as test cases during assessments.
3. **A procurement specification** — Organizations include TCASVS compliance in vendor security requirements.
4. **A maturity benchmark** — Teams assess their current security posture against defined levels and plan improvements.

Select the appropriate level based on the application's risk profile, then verify all requirements at that level and below are met.

\newpage{}
