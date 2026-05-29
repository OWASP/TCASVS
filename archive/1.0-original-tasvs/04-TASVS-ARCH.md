# TASVS-ARCH: Architecture & Threat Modelling

## Control Objective

Architecture and threat modeling are inextricably linked. Threat modeling informs architectural decisions, while architecture provides the context for identifying and addressing threats systematically. This symbiotic relationship is essential for delivering secure software and systems that meet their intended design goals.


## Testing Checklist

| TASVS-ID       | Description                                                                                                                                 | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-ARCH-1   | Threat Modeling                                                                                                                             |    |    |    |
| TASVS-ARCH-1.1 | Completed a low fidelity threat model for thick client.                                                                                     | X  | X  | X  |
| TASVS-ARCH-1.2 | Completed a high fidelity threat model for thick client which is currently in production.                                                   |    | X  | X  |
| TASVS-ARCH-1.3 | Threat model includes server-side components and dependencies (cloud APIs, OIDC provider, file storage, etc.).                              |    | X  | X  |
| TASVS-ARCH-1.4 | Threat modeling process included all phases (system modeling, auto-threat identification, manual threat identification, threat mitigation). |    | X  | X  |
| TASVS-ARCH-1.5 | Threat model checked-in to source code repository.                                                                                          | X  | X  | X  |
| TASVS-ARCH-1.6 | Threat model updated regularly as part of a documented process within development team's SSDLC.                                             |    | X  | X  |

## Control Group Definitions

### *TASVS-ARCH-1 - Threat Modeling*

### TASVS-ARCH-1.1 - Completed a low fidelity threat model for thick client.

#### What defines "Low Fidelity" Modeling?

"Low Fidelity" modeling greatly reduces the effort to create an initial threat model. A "Low Fidelity" system model still includes assets, links, and trust boundaries, but with limited attributes.
 
Recommended "Low Fidelity" baseline:
- Define data assets with CIA (confidentiality/integrity/availability)
- Define technical assets with technology.
- Define communication links with protocol.
- Place technical assets inside trust boundaries.

That's it! Later, continue to elaborate the model and raise fidelity score. Remember the system model is a means to an end - identifying threats.

### TASVS-ARCH-1.2 - Completed a high fidelity threat model for thick client which is currently in production.

"High fidelity" threat modeling is a more detailed and comprehensive approach to threat modeling which maximizes threat identification. High fidelity is appropriate for a production product where all aspects of the system are well-understood. It includes all the elements of a low fidelity model but adds additional detail and context to the model. This includes:

- Define data assets processed and stored on technical assets
- Define data assets flowing on communication links
- Optional attributes defined on data assets and technical assets

### TASVS-ARCH-1.3 - Threat model includes server-side components and dependencies (cloud APIs, OIDC provider, file storage, etc.).

Server-side components and dependencies should be included in the threat modeling process to ensure that all potential threats are identified and addressed. This includes cloud APIs, OIDC providers, file storage, and any other external services that the thick client interacts with. By including these components in the threat model, you can identify potential vulnerabilities and design security controls to mitigate them.

### TASVS-ARCH-1.4 - Threat modeling process included all phases (system modeling, auto-threat identification, manual threat identification, threat mitigation).

Phases of threat modeling include system modeling, auto-threat identification, manual threat identification, and threat mitigation. Each phase is essential to the overall threat modeling process and should be completed thoroughly to ensure that all potential threats are identified and addressed.

### TASVS-ARCH-1.5 - Threat model checked-in to source code repository.

The threat model should be checked into the source code repository to ensure that it is accessible to all members of the development team. This allows team members to review the threat model and provide feedback, as well as track changes to the model over time.


### TASVS-ARCH-1.6 - Threat model updated regularly as part of a documented process within development team's SSDLC.

The threat model should be updated regularly as part of a documented process within the development team's secure software development lifecycle (SSDLC). This ensures that the threat model remains current and relevant as the thick client evolves and new threats emerge. Regular updates to the threat model help to ensure that the thick client design remains secure and resilient to potential threats.


\newpage{}
