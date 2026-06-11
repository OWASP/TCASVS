# V2 Build, Deployment, and Environment Hardening

## Control Objective

Ensure that thick client applications are built, packaged, deployed, and configured in a manner that eliminates unnecessary attack surface and leverages available platform security features. This chapter covers supply chain integrity, compiler-level exploit mitigations, secure installation and update mechanisms, and runtime privilege minimization.

## V2.1 Build and Supply Chain Security

This section addresses the integrity of the build pipeline and third-party dependencies, ensuring that production artifacts are trustworthy, minimal, and traceable.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V2.1.1 | Verify that the application build and deployment processes are automated using CI/CD pipelines with integrity-protected build environments, producing reproducible artifacts. | 1 | 1127 | TASVS |
| V2.1.2 | Verify that the application and all dependencies can be re-deployed from automated scripts or restored from backups within a documented recovery timeframe. | 2 | 693 | TASVS |
| V2.1.3 | Verify that production builds exclude all unnecessary features, sample code, documentation, test utilities, and development configurations. | 1 | 489 | TASVS |
| V2.1.4 | Verify that all third-party components are sourced from pre-defined, trusted, and continuously maintained repositories with integrity verification of downloaded artifacts. | 1 | 829 | TASVS |
| V2.1.5 | Verify that a Software Bill of Materials (SBOM) is maintained for all third-party libraries in use, including transitive dependencies, and is updated on each release. | 1 | 1104 | TASVS |
| V2.1.6 | Verify that production builds do not contain debug symbols, verbose error strings, or embedded developer credentials. | 1 | 215 | New |
| V2.1.7 | Verify that released binaries and installers are code-signed with a valid, non-expired certificate, and that the signing key is protected by hardware (HSM or equivalent). | 2 | 494 | New |
| V2.1.8 | Verify that the build system is protected against dependency confusion attacks by pinning dependencies with integrity hashes and using private registry priority for internal packages. | 2 | 427 | New |

## V2.2 Environment Hardening

This section covers compiler and OS-level exploit mitigations that must be enabled in production builds to raise the cost of memory corruption exploitation.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V2.2.1 | Verify that compiler and linker flags enable all available exploit mitigations, including stack canaries, stack randomization, and data execution prevention, and that the build fails on unsafe pointer, memory, format string, integer, or string operations. | 1 | 120 | TASVS |
| V2.2.2 | Verify that the application binary enables Address Space Layout Randomization (ASLR) by being compiled as a position-independent executable (PIE) with a high-entropy base address. | 1 | 119 | New |
| V2.2.3 | Verify that Data Execution Prevention (DEP/NX) is enforced for all executable modules, preventing code execution from data segments. | 1 | 119 | New |
| V2.2.4 | Verify that Control Flow Integrity (CFI) protections are enabled where supported by the compiler toolchain, such as Control Flow Guard (CFG) on Windows or CFI on Clang/LLVM. | 2 | 691 | New |
| V2.2.5 | Verify that hardware-assisted exploit mitigations (such as Intel CET shadow stacks or ARM PAC/BTI) are enabled for builds targeting platforms that support them. | 3 | 119 | New |
| V2.2.6 | Verify that the application does not disable or weaken OS-level security features at runtime (e.g., calling SetProcessDEPPolicy to disable DEP, marking memory as RWX without justification). | 2 | 693 | New |

## V2.3 Installation and Update Security

This section ensures that installers and auto-update mechanisms cannot be subverted to deliver tampered code or escalate privileges beyond what is necessary.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V2.3.1 | Verify that the installer validates its own integrity before execution (e.g., embedded signature verification or checksum validation from a trusted manifest). | 1 | 354 | New |
| V2.3.2 | Verify that the installer does not create temporary files with insecure permissions in world-writable directories, or that such files are integrity-checked before use. | 1 | 377 | New |
| V2.3.3 | Verify that the application's auto-update mechanism validates cryptographic signatures on update packages before applying them, using a trust anchor independent of the downloaded package. | 1 | 494 | New |
| V2.3.4 | Verify that the auto-update mechanism uses TLS with certificate pinning or equivalent for update downloads, and fails closed if verification fails. | 2 | 295 | New |
| V2.3.5 | Verify that the installer and application use safe DLL search order and do not load libraries from user-writable or uncontrolled directories, preventing DLL sideloading and search-order hijacking. | 1 | 427 | New |
| V2.3.6 | Verify that installer privilege elevation (e.g., UAC prompts on Windows) is limited to the minimum operations that require elevated privileges, and that elevated child processes are not exposed to untrusted input. | 2 | 250 | New |

## V2.4 Privilege and Permission Management

This section addresses runtime privilege minimization, process isolation, and proper access control on filesystem and IPC objects created by the application.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V2.4.1 | Verify that the application runs with the minimum privileges required for its functionality, and that elevated components expose only the minimum necessary IPC interface surface. | 1 | 250 | TASVS |
| V2.4.2 | Verify that the application satisfies the "Rule of 2": it does not simultaneously process untrustworthy input, use a memory-unsafe language, and run with elevated privileges or without a sandbox. | 1 | 250 | TASVS |
| V2.4.3 | Verify that filesystem permissions are correctly restricted on all directories and files created, modified, or accessed during installation and at runtime, preventing unauthorized read, write, or execute access by lower-privileged users. | 1 | 732 | TASVS |
| V2.4.4 | Verify that Windows services or system daemons used by the application run under dedicated service accounts with minimal privileges, not as LocalSystem, root, or equivalent unless explicitly justified and documented. | 2 | 250 | New |
| V2.4.5 | Verify that configuration files, registry keys, and local databases used by the application are protected with restrictive ACLs preventing modification by non-administrative users. | 1 | 732 | New |
| V2.4.6 | Verify that the application implements sandboxing or process isolation for components that handle untrusted input (e.g., file parsers, protocol handlers, plugin hosts), limiting access to the filesystem, network, and system APIs. | 2 | 265 | New |
| V2.4.7 | Verify that named pipes, shared memory segments, and other OS IPC objects created by the application use restrictive security descriptors that prevent connection or modification by unauthorized processes. | 2 | 732 | New |

## References

- [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl)
- [NIST SP 800-218 - Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [SLSA Supply Chain Levels for Software Artifacts](https://slsa.dev/)
