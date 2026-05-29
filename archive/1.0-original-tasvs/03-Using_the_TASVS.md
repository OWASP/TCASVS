# The Thick Client Application Security Verification Standard

This verification standard should be useful to anyone trying to:

- Develop and maintain secure applications.
- Evaluate the security of applications.


## Thick Client Application Security Model

The standard is divided into various groups labelled `TASVS-{word}` that represent the most critical areas of a thick clients attack surface. These control groups are divided into sub groups, labeled `TASVS-{word}-{digit}`. Each of these control groups contains individual controls labeled `TASVS-{word}-{digit}.{digit}`, which provide specific guidance on the particular security measures that need to be implemented to meet the standard. For example `TASVS-ARCH-1.1`.

### Top Group

- TASVS-ARCH -  Architecture & threat modelling.
- TASVS-CODE - Code quality and exploit mitigation.
- TASVS-CONF - Configuration and building.
- TASVS-CRYPTO - Cryptography.
- TASVS-NETWORK - Communication and privacy.
- TASVS-STORAGE - Data storage considerations.
- TASVS-FUTURE - Coming soon General considerations for future cloud adoption strategies.

### Sub Group

- TASVS-ARCH-1 - Threat Modeling
- TASVS-CODE-1 - Server Side
- TASVS-CODE-2 - Client Side - Signing and Integrity
- TASVS-CODE-3 - Client Side - Static Code Analysis
- TASVS-CODE-4 - Client Side - Validation, Sanitization and Encoding
- TASVS-CODE-5 - Client Side - Business Logic
- TASVS-CODE-6 - Client Side - Fuzzing
- TASVS-CODE-7 - Client Side - Secure Coding Practices
- TASVS-CONF-1 - General Configuration Checks
- TASVS-CONF-2 - Privileges and Permissions
- TASVS-CRYPTO-1 - Communication
- TASVS-CRYPTO-2 - Storage
- TASVS-CRYPTO-3 - General
- TASVS-NETWORK-1 - Data leakage
- TASVS-NETWORK-2 - Licensing & Authentication Servers
- TASVS-NETWORK-3 - Piracy Detection
- TASVS-NETWORK-4 - Connected Services
- TASVS-STORAGE-1 - Sensitive Information Review
- TASVS-STORAGE-2 - DLL Hijacking


## Application Security Verification Levels

We follow the same levelling methodology as the [Web Application Security Verification Standard](https://github.com/OWASP/ASVS/tree/master). It defines three security verification levels, with each level increasing in depth.

- L1 - TASVS Level 1 is for low assurance levels and is completely verifiable through penetration testing.
- L2 - TASVS Level 2 is for applications that contain sensitive data, which requires protection and is the recommended level for most apps.
- L3 - TASVS Level 3 is intended for the most critical applications, such as those handling high-value transactions, containing sensitive medical data, or any application demanding the highest level of trust.



\newpage{}
