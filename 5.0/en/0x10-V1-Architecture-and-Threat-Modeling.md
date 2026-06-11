# V1 Architecture and Threat Modeling

## Control Objective

Thick client applications operate in uniquely hostile environments: they execute on hardware controlled by end users, communicate across untrusted networks, interact with local operating system resources, and often run with elevated privileges. Unlike web applications confined to a browser sandbox, thick clients expose a broad and heterogeneous attack surface spanning local filesystems, inter-process communication, kernel interfaces, and network endpoints. Without a structured threat model and deliberate architecture security design, teams cannot systematically identify, prioritize, or mitigate the risks specific to this deployment model. This chapter ensures that thick client applications are designed with security as a first-class architectural concern, that threats are identified and tracked throughout the development lifecycle, and that the full attack surface — including client-specific vectors such as binary tampering, memory manipulation, and privilege escalation — is documented and managed.

## V1.1 Threat Model Documentation

A threat model is only useful if it is documented, accessible, and specific enough to drive security decisions. For thick client applications, threat models must account for attack surfaces that do not exist in server-only architectures: local storage, IPC mechanisms, OS-level interactions, and the reality that attackers have full physical access to the client binary. These requirements ensure that threat models exist, are appropriately detailed for the application's risk level, and cover the full scope of thick client deployment.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V1.1.1 | Verify that a threat model exists for the thick client application, identifying at minimum the application's entry points, assets, trust boundaries, and high-level threats relevant to client-side, server-side, network, and local attack surfaces. | 1 | 1053 | TASVS |
| V1.1.2 | Verify that a detailed threat model is maintained for the production application, including data flow diagrams, STRIDE or equivalent threat classification for each component, and risk-rated threat scenarios with documented mitigations. | 2 | 1053 | TASVS |
| V1.1.3 | Verify that the threat model scope explicitly includes all server-side components, third-party dependencies, cloud service integrations (APIs, OIDC providers, file storage), and the communication channels between client and server. | 2 | 1053 | TASVS |
| V1.1.4 | Verify that threat model artifacts are stored in the source code repository alongside the application code, versioned, and reviewable as part of the standard change process. | 1 | 1053 | TASVS |
| V1.1.5 | Verify that the threat model documents all trust boundaries in the application, including boundaries between user-mode and kernel-mode components, between processes of different privilege levels, and between the client application and backend services. | 2 | 501 | New |
| V1.1.6 | Verify that data flow diagrams identify all paths where sensitive data (credentials, tokens, PII, business-critical data) traverses trust boundaries, and document the protection mechanisms applied at each crossing. | 2 | 319 | New |

## V1.2 Threat Modeling Process

Creating a threat model once and filing it away provides little ongoing value. Thick client applications evolve rapidly — new features expose new IPC channels, dependency updates introduce new attack surface, and architectural changes shift trust boundaries. These requirements ensure that threat modeling is a living process integrated into the secure development lifecycle, not a one-time compliance exercise.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V1.2.1 | Verify that the threat modeling process encompasses all phases: system modeling (architecture decomposition), automated threat identification (tooling-assisted), manual threat identification (expert review), and threat mitigation planning with assigned owners. | 2 | 1053 | TASVS |
| V1.2.2 | Verify that the threat model is reviewed and updated at defined intervals and upon significant architectural changes, as part of the development team's documented secure development lifecycle (SSDLC). | 2 | 1053 | TASVS |
| V1.2.3 | Verify that the threat model is validated against the implemented application by confirming that documented mitigations are present and effective, and that no undocumented attack surfaces exist. | 3 | 1053 | New |
| V1.2.4 | Verify that threat modeling outputs are used as input for security test planning, with each identified threat having at least one corresponding test case or verification activity. | 2 | 1053 | New |

## V1.3 Architecture Security Design

Thick clients face architectural challenges that server-side applications do not: they must manage privilege separation across local processes, isolate plugin subsystems that run untrusted code, secure their own update mechanisms against tampering, and sometimes operate in adversarial environments where the local OS itself cannot be trusted. These requirements ensure that security is designed into the architecture rather than bolted on after deployment.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V1.3.1 | Verify that architecture documentation describes the privilege separation model, including which components run at elevated privilege, what IPC mechanisms connect them, and how the principle of least privilege is applied to each process. | 1 | 250 | New |
| V1.3.2 | Verify that the architecture documents security design principles applied to the thick client, including defense in depth, fail-secure defaults, complete mediation, and economy of mechanism. | 2 | 657 | New |
| V1.3.3 | Verify that the architecture documents how plugin, extension, or scripting subsystems are isolated from the host application, including what APIs are exposed, what permissions are required, and how malicious plugins are prevented from accessing privileged functionality. | 2 | 284 | New |
| V1.3.4 | Verify that the architecture documents the application's update and patching mechanism design, including the trust chain for update verification, rollback capabilities, and how partial or failed updates are handled securely. | 2 | 494 | New |
| V1.3.5 | Verify that the architecture documents how the application handles execution in an adversarial local environment where the OS, other processes, and the user may be hostile (e.g., anti-cheat, DRM, or security-sensitive applications). | 3 | 693 | New |

## V1.4 Attack Surface Management

Thick clients expose attack surface across multiple dimensions simultaneously: local filesystem paths, registry keys, named pipes, shared memory, COM objects, listening network ports, outbound connections, and user-facing input vectors. Unlike server applications where the attack surface is primarily network-facing, thick clients must defend against local attackers with debugger access, binary analysis tools, and the ability to inject code into the process. These requirements ensure the full attack surface is identified, documented, and actively managed as the application evolves.

| # | Description | Level | CWE | Source |
|---|-------------|:-----:|-----|--------|
| V1.4.1 | Verify that the application's attack surface is documented, including all local interfaces (filesystem paths, registry keys, named pipes, shared memory, COM objects), network interfaces (listening ports, outbound connections), and user-facing input vectors. | 1 | 1059 | New |
| V1.4.2 | Verify that the attack surface documentation identifies which interfaces are exposed to unauthenticated or low-privilege callers, and that each such interface has documented input validation and access control expectations. | 2 | 306 | New |
| V1.4.3 | Verify that the threat model explicitly addresses thick-client-specific attack vectors, including binary reverse engineering, memory tampering, local privilege escalation, DLL/dylib injection, debugger attachment, and inter-process communication abuse. | 1 | 693 | New |
| V1.4.4 | Verify that attack surface changes introduced by new features or dependency updates are assessed and the threat model is updated before deployment to production. | 2 | 1053 | New |

## References

- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [Microsoft STRIDE Threat Model](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [OWASP Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
- [CWE-1053: Missing Documentation for Design](https://cwe.mitre.org/data/definitions/1053.html)
- [CWE-250: Execution with Unnecessary Privileges](https://cwe.mitre.org/data/definitions/250.html)
- [CWE-494: Download of Code Without Integrity Check](https://cwe.mitre.org/data/definitions/494.html)
