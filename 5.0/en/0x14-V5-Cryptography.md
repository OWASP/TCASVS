# V5 Cryptography

## Control Objective

Ensure that the thick client application implements cryptography in accordance with current industry best practices. This includes using approved algorithms and protocols, managing keys securely throughout their lifecycle, generating cryptographically strong random values, and establishing secure transport channels. Cryptographic controls must protect data confidentiality, integrity, and authenticity both at rest and in transit, while remaining agile enough to accommodate algorithm deprecation and key rotation without requiring full application rebuilds.

## V5.1 Cryptographic Policy and Inventory

A documented cryptographic policy and complete inventory provide the foundation for managing cryptographic risk in thick client applications. Without visibility into which algorithms, keys, and certificates are in use, organizations cannot assess exposure when weaknesses are discovered.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.1.1 | Verify that there is a documented policy for cryptographic key management, including key generation, distribution, storage, rotation, and revocation, following a standard such as NIST SP 800-57. | 2 | 320 | New |
| V5.1.2 | Verify that a cryptographic inventory is maintained, covering all keys, algorithms, and certificates used by the thick client, including those embedded in the binary or configuration files. | 3 | 311 | New |

## V5.2 Secure Cryptographic Implementation

Correct implementation of cryptographic primitives is as important as algorithm selection. Failure modes, library choices, and architectural flexibility determine whether cryptography provides real protection or a false sense of security.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.2.1 | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities such as Padding Oracle attacks. | 2 | 310 | TASVS |
| V5.2.2 | Verify that industry-validated or government-approved cryptographic algorithms, modes, and libraries are used instead of custom-coded cryptography. | 2 | 327 | TASVS |
| V5.2.3 | Verify that the application is designed with crypto agility such that algorithms, key lengths, and modes can be reconfigured or upgraded without requiring a full application rebuild. | 2 | 327 | New |

## V5.3 Encryption Algorithms and Protocols

Thick clients must avoid deprecated cryptographic primitives and enforce minimum security strengths. Algorithm and mode selection directly determines the effective security of data protection mechanisms.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.3.1 | Verify that the thick client does not use cryptographic protocols or algorithms that are widely considered deprecated or insecure (e.g., DES, 3DES, RC4, MD5, SHA-1 for signing). | 1 | 327 | TASVS |
| V5.3.2 | Verify that only approved ciphers and authenticated encryption modes (e.g., AES-GCM, ChaCha20-Poly1305) are used, and insecure block modes (e.g., ECB) or weak padding schemes (e.g., PKCS#1 v1.5) are not used. | 1 | 327 | New |
| V5.3.3 | Verify that all cryptographic primitives utilize a minimum of 128 bits of security based on the algorithm, key size, and configuration. | 2 | 326 | New |

## V5.4 Random Values

Thick clients frequently generate random values for session tokens, nonces, initialization vectors, and key material. Weak or predictable randomness undermines the security of all dependent cryptographic operations.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.4.1 | Verify that all random numbers and strings intended to be non-guessable are generated using a cryptographically secure pseudo-random number generator (CSPRNG) with at least 128 bits of entropy. | 2 | 338 | TASVS |
| V5.4.2 | Verify that the random number generation mechanism works securely under heavy demand and does not degrade to predictable output when entropy is low. | 3 | 332 | New |

## V5.5 Key Management and Storage

Cryptographic keys require protection throughout their lifecycle. Thick clients present unique challenges because keys may be embedded in binaries, stored on user-controlled filesystems, or held in process memory accessible to local attackers.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.5.1 | Verify that the thick client does not reuse the same cryptographic key for multiple purposes (e.g., encryption and authentication). | 2 | 323 | TASVS |
| V5.5.2 | Verify that the thick client does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption, and that keys are not extractable from the binary. | 1 | 321 | TASVS |
| V5.5.3 | Verify that cryptographic keys stored locally are protected using platform-provided secure storage mechanisms (e.g., Windows DPAPI, macOS Keychain, Linux kernel keyring) rather than plaintext files or application-level obfuscation. | 1 | 312 | New |
| V5.5.4 | Verify that cryptographic keys are protected in memory during runtime, using techniques such as zeroing after use, avoiding swap/page-out of key material, or leveraging hardware-backed key isolation where available. | 3 | 316 | New |

## V5.6 Transport Cryptography

Thick clients communicate with backend services over networks that may be hostile. Transport layer protections must ensure confidentiality, integrity, and server authenticity while preventing downgrade attacks and certificate validation bypasses.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V5.6.1 | Verify that TLS settings are in line with current best practices, including TLS 1.2+ with secure cipher suites and Perfect Forward Secrecy enabled. | 1 | 326 | TASVS |
| V5.6.2 | Verify that the thick client validates server certificates correctly, including checking certificate chains, revocation status, and hostname matching, and does not silently bypass certificate errors. | 1 | 295 | New |
| V5.6.3 | Verify that certificate pinning is implemented for connections to known backend services, with a documented update mechanism for pin rotation. | 2 | 295 | New |
| V5.6.4 | Verify that code signing is used for application binaries and updates, and that the thick client validates signatures before executing downloaded code or applying updates. | 2 | 494 | New |

## References

For more information, see:

* [NIST SP 800-57 — Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
* [NIST SP 800-131A — Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://csrc.nist.gov/publications/detail/sp/800-131a/rev-2/final)
* [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
* [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
* [CWE-310 — Cryptographic Issues](https://cwe.mitre.org/data/definitions/310.html)
* [CWE-327 — Use of a Broken or Risky Cryptographic Algorithm](https://cwe.mitre.org/data/definitions/327.html)
