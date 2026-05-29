# V3 Data Storage and Protection

## Control Objective

Thick client applications operate in environments where the local filesystem, process memory, OS registries, and inter-process channels are all potential attack surfaces. Unlike server-side applications running in controlled data centres, thick clients execute on endpoints that may be shared between users, physically accessible to adversaries, or subject to forensic recovery. Data stored locally — whether in configuration files, databases, memory, or temporary files — is exposed to extraction by malware, co-resident applications, privileged users, and offline analysis of disk images.

Ensure that the thick client correctly classifies sensitive data, protects it at rest using platform-provided secure storage mechanisms, minimizes the window of exposure in process memory, and performs thorough cleanup of residual data. The controls in this chapter address the full local data lifecycle: classification, file and configuration storage, credential management, memory protection, and temporary data hygiene.

## V3.1 — Data Classification and Policy

Effective data protection begins with understanding what data the application handles and how sensitive it is. Without explicit classification and retention policies, developers cannot make informed decisions about which storage mechanisms and protections are appropriate. This section ensures that sensitive data is identified, categorized, and subject to defined lifecycle management — preventing accumulation of unprotected data that outlives its purpose.

| # | Description | L1 | L2 | L3 | CWE | Source |
|---|-------------|:--:|:--:|:--:|-----|--------|
| V3.1.1 | Verify that all sensitive data created, processed, or stored by the application has been identified, classified into protection levels, and that documented protection requirements exist for each level. | | ✓ | ✓ | 922 | TASVS |
| V3.1.2 | Verify that a data retention policy is defined and enforced, ensuring that sensitive data is automatically deleted or anonymized when no longer required for its stated purpose. | | ✓ | ✓ | 922 | New |

## V3.2 — Sensitive Data in Files and Configuration

Thick clients store data across numerous local surfaces: application binaries, configuration files, OS registries, property lists, log files, and embedded databases. Each of these is readable by local users, backup tools, and forensic analysis unless explicitly protected. Hardcoded secrets are trivially extractable through static analysis tools. This section ensures that no sensitive data is exposed in plaintext through any local file or configuration store.

| # | Description | L1 | L2 | L3 | CWE | Source |
|---|-------------|:--:|:--:|:--:|-----|--------|
| V3.2.1 | Verify that binaries, configuration files, and application data files do not contain plaintext credentials, connection strings, API keys, or other secrets. | ✓ | ✓ | ✓ | 798 | TASVS |
| V3.2.2 | Verify that registry entries, property lists (plists), and other OS-level configuration stores do not contain plaintext credentials, connection strings, API keys, or other secrets. | ✓ | ✓ | ✓ | 798 | TASVS |
| V3.2.3 | Verify that application logs do not capture or persist sensitive data, including PII, credentials, session tokens, or connection strings used for internal or external resources. | ✓ | ✓ | ✓ | 532 | TASVS |
| V3.2.4 | Verify that sensitive data embedded in application binaries (such as hardcoded keys, certificates, or configuration) is not discoverable through trivial static analysis or string extraction. | ✓ | ✓ | ✓ | 798 | TASVS |
| V3.2.5 | Verify that local databases (SQLite, LevelDB, Realm, etc.) containing sensitive data are stored in protected directories with restrictive filesystem permissions and, where supported, use database-level encryption. | ✓ | ✓ | ✓ | 311 | New |
| V3.2.6 | Verify that application backup or export functionality excludes or encrypts sensitive data, and that backup files are stored with restrictive permissions. | | ✓ | ✓ | 530 | New |

## V3.3 — Credential and Secret Storage

Credentials, tokens, and cryptographic keys require stronger protection than general application data. Thick clients must leverage OS-provided secure storage mechanisms rather than implementing custom solutions that are likely to be weaker and less audited. On multi-user systems, secrets stored insecurely are accessible to other user accounts or malware running at the same privilege level. This section ensures that all authentication material and sensitive keys are stored using platform security primitives.

| # | Description | L1 | L2 | L3 | CWE | Source |
|---|-------------|:--:|:--:|:--:|-----|--------|
| V3.3.1 | Verify that authentication tokens and session identifiers are stored using OS-provided secure storage mechanisms (e.g., Windows Credential Manager, macOS Keychain, Linux Secret Service) and are not accessible to other applications or lower-privileged users. | ✓ | ✓ | ✓ | 522 | TASVS |
| V3.3.2 | Verify that regulated private, health, or financial data is stored encrypted at rest using approved algorithms and key management practices, compliant with applicable data protection regulations (e.g., GDPR, HIPAA, PCI DSS). | ✓ | ✓ | ✓ | 311 | TASVS |
| V3.3.3 | Verify that the application uses OS-provided credential storage APIs (e.g., Windows DPAPI, macOS Keychain, Linux libsecret) for persisting secrets, rather than custom or plaintext storage mechanisms. | ✓ | ✓ | ✓ | 522 | New |
| V3.3.4 | Verify that cryptographic keys stored locally are protected by hardware-backed keystores where available (e.g., TPM, Secure Enclave, platform keystore APIs) and are not exportable in plaintext. | | | ✓ | 321 | New |

## V3.4 — Memory Protection

Process memory is a high-value target for attackers with local access. Sensitive data that remains in memory after use can be recovered through memory dumps, debugger attachment, swap file analysis, or crash dump collection. On multi-user workstations, clipboard contents are shared across all applications. This section ensures that the application minimizes the time sensitive data spends in memory and prevents leakage through memory-adjacent channels such as swap, clipboard, and crash dumps.

| # | Description | L1 | L2 | L3 | CWE | Source |
|---|-------------|:--:|:--:|:--:|-----|--------|
| V3.4.1 | Verify that the application does not retain sensitive data in process memory longer than necessary, and that memory containing secrets is explicitly zeroed or overwritten immediately after use. | ✓ | ✓ | ✓ | 316 | TASVS |
| V3.4.2 | Verify that the application marks memory pages containing sensitive data as non-pageable (e.g., VirtualLock on Windows, mlock on Linux) to prevent secrets from being written to swap/pagefile. | | ✓ | ✓ | 316 | New |
| V3.4.3 | Verify that the application prevents sensitive data from being exposed through clipboard operations, either by clearing the clipboard after a short timeout or by preventing copy operations on sensitive fields. | ✓ | ✓ | ✓ | 200 | New |
| V3.4.4 | Verify that crash dumps and core files generated by the application do not contain sensitive data, or that crash dump generation is configured to exclude sensitive memory regions. | | ✓ | ✓ | 215 | New |

## V3.5 — Temporary and Residual Data

Thick clients frequently create temporary files for caching, inter-process data exchange, or intermediate processing. These files persist on disk after the process exits and can be recovered by other users, malware, or forensic tools. Shared system temp directories are particularly dangerous as they are writable and readable by all local users, enabling symlink attacks and data theft. This section ensures that the application manages temporary data securely and leaves no sensitive residuals after logout or uninstall.

| # | Description | L1 | L2 | L3 | CWE | Source |
|---|-------------|:--:|:--:|:--:|-----|--------|
| V3.5.1 | Verify that the application removes temporary files containing sensitive data immediately after use, using secure deletion where the OS supports it. | ✓ | ✓ | ✓ | 459 | New |
| V3.5.2 | Verify that temporary files are created in application-specific directories with restrictive permissions, not in shared system temp directories accessible to other users. | ✓ | ✓ | ✓ | 377 | New |
| V3.5.3 | Verify that the application performs secure cleanup of all locally stored sensitive data (including cached credentials, tokens, and session state) upon user logout or application uninstall. | ✓ | ✓ | ✓ | 459 | New |
| V3.5.4 | Verify that inter-process communication of sensitive data between application components uses authenticated, encrypted channels rather than world-readable shared files or environment variables. | | ✓ | ✓ | 319 | New |

## References

- [OWASP Credential Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Storage_Cheat_Sheet.html)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [CWE-922: Insecure Storage of Sensitive Information](https://cwe.mitre.org/data/definitions/922.html)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-316: Cleartext Storage of Sensitive Information in Memory](https://cwe.mitre.org/data/definitions/316.html)
- [CWE-522: Insufficiently Protected Credentials](https://cwe.mitre.org/data/definitions/522.html)
- [CWE-311: Missing Encryption of Sensitive Data](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-459: Incomplete Cleanup](https://cwe.mitre.org/data/definitions/459.html)
- [Microsoft DPAPI Documentation](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-dpapi)
- [Apple Keychain Services](https://developer.apple.com/documentation/security/keychain_services)

\newpage{}
