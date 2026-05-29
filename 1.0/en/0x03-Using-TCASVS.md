# Using the TCASVS

## Thick Client Application Security Verification Levels

The TCASVS defines three security verification levels, with each level increasing in depth and rigour.

### TCASVS Level 1 — Baseline

Level 1 is the minimum security standard that all thick client applications should achieve. It focuses on requirements that address the most common and easily exploitable vulnerabilities: hardcoded credentials, missing TLS enforcement, disabled exploit mitigations, and unsafe input handling.

A Level 1 assessment can typically be performed through a combination of automated scanning, binary analysis, and targeted manual testing.

### TCASVS Level 2 — Standard

Level 2 is appropriate for applications that handle sensitive data (PII, financial data, health records), operate in enterprise environments, or face a moderately capable adversary. It adds defense-in-depth requirements including threat modeling, privilege separation, certificate pinning, secure IPC, and runtime integrity checks.

A Level 2 assessment requires access to source code or debug symbols, architecture documentation, and a thorough security review process.

### TCASVS Level 3 — Advanced

Level 3 is reserved for applications operating in hostile environments where the local OS cannot be trusted, where targeted attacks by skilled adversaries are expected, or where compromise would result in significant harm. This includes applications with DRM, anti-cheat, financial trading, critical infrastructure control, or handling classified data.

Level 3 adds requirements for hardware-backed security, advanced tamper resistance, coverage-guided fuzzing, and cryptographic agility.

## Applying the Standard

### For Developers

Use TCASVS requirements as security acceptance criteria during development:

1. Identify your target level based on the application's risk profile.
2. Review relevant chapter requirements during design and implementation.
3. Implement requirements as verifiable security controls.
4. Write test cases that validate each requirement is met.

### For Security Testers

Use TCASVS as a testing framework:

1. Scope the assessment to the appropriate level.
2. Use chapter requirements as test cases.
3. Document findings against specific requirement IDs.
4. Report gaps as deviations from the target level.

### For Organizations

Use TCASVS as a governance tool:

1. Define the target level in security policies.
2. Include TCASVS compliance in vendor assessments and procurement.
3. Track compliance over time as a maturity metric.
4. Use gaps between current state and target level to prioritize security investment.

## Scope

The TCASVS covers security requirements specific to thick client applications — software that executes locally on user-controlled endpoints. This includes:

- Desktop applications (Windows, macOS, Linux)
- Native applications with local installation
- Client-server applications where the client runs outside a browser
- Electron, Qt, WPF, WinForms, Swing, and similar framework applications
- Games and multimedia applications
- Enterprise tools and productivity software

The TCASVS does **not** cover:

- Server-side API security (use [OWASP ASVS](https://github.com/OWASP/ASVS))
- Mobile applications (use [OWASP MASVS](https://github.com/OWASP/owasp-masvs))
- Web applications running in a browser (use OWASP ASVS)
- IoT firmware (specialized standards apply)

Where thick clients communicate with backend services, the TCASVS covers the client-side implementation of that communication. Server-side security should be verified independently using the ASVS.

\newpage{}
