# V6 Network Communication Security

## Control Objective

Thick client applications frequently communicate over networks with backend services, license servers, update mechanisms, and third-party APIs. Unlike web applications where the browser enforces transport security policies, thick clients must implement and enforce their own network security controls, making them susceptible to interception, downgrade attacks, and unintended service exposure.

Ensure that all network communication channels used by the thick client are protected against eavesdropping, tampering, and unauthorized access. This includes enforcing modern transport encryption, minimizing network attack surface, preventing data leakage through side channels, securing local inter-process communication, and protecting license validation flows from manipulation.

## V6.1 Transport Layer Security

Thick clients often manage their own TLS stack or rely on platform libraries that may be misconfigured. Attackers with network access can exploit missing or weak TLS enforcement to intercept credentials, session tokens, and business-critical data. This section ensures all network-facing channels enforce modern authenticated encryption without fallback to insecure transports.

| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V6.1.1 | Verify that all network communication channels used by the thick client enforce TLS consistently, with no fallback to unencrypted transport. | 1 | TASVS |
| V6.1.2 | Verify that all connections to backend services, update servers, telemetry endpoints, and third-party APIs enforce TLS 1.2 or higher with no protocol downgrade possible. | 1 | New |
| V6.1.3 | Verify that custom or proprietary protocols used by the thick client are wrapped in TLS or provide equivalent authenticated encryption for data in transit. | 2 | New |

## V6.2 Network Service Exposure

Thick clients may inadvertently expose debugging interfaces, plugin APIs, or management ports on local or external network interfaces. Attackers on the same network or local machine can discover and exploit these exposed services for privilege escalation or remote code execution. This section ensures the application minimizes its network attack surface.

| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V6.2.1 | Verify that the thick client does not expose network services (e.g., debugging interfaces, management ports) on any interface, including localhost, unless explicitly required and authenticated. | 1 | TASVS |
| V6.2.2 | Verify that the application does not bind listener sockets to all interfaces (0.0.0.0/::) when only local communication is required. | 1 | New |
| V6.2.3 | Verify that any network services intentionally exposed by the thick client require authentication before accepting commands or data. | 2 | New |

## V6.3 Network Data Leakage Prevention

Thick clients may leak sensitive information through unencrypted channels, URL parameters, HTTP headers, or verbose error messages visible on the wire. Unlike server-side applications, thick clients often lack centralized egress controls, making it critical to validate that no sensitive data escapes through network side channels.

| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V6.3.1 | Verify that sensitive tokens, keys, and credentials are not transmitted in plaintext or weakly encoded forms susceptible to interception by man-in-the-middle attacks. | 1 | TASVS |
| V6.3.2 | Verify that sensitive data (credentials, tokens, PII) is not leaked through URL parameters, HTTP referrer headers, or unencrypted DNS queries. | 1 | New |
| V6.3.3 | Verify that network traffic does not expose unnecessary metadata or debug information (e.g., internal hostnames, stack traces, software version strings) in cleartext. | 2 | New |

## V6.4 Inter-Process and Local Network Communication

Thick clients commonly use IPC mechanisms such as named pipes, Unix sockets, shared memory, or loopback TCP connections to coordinate between components or plugins. Malicious local processes can inject commands or tamper with data flowing through unprotected IPC channels, particularly in multi-user or shared workstation environments.

| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V6.4.1 | Verify that inter-process communication channels (named pipes, Unix sockets, shared memory, local TCP) implement authentication to prevent unauthorized local processes from connecting. | 2 | New |
| V6.4.2 | Verify that data exchanged over local IPC channels is integrity-protected to prevent tampering by other local processes running at the same privilege level. | 3 | New |

## V6.5 License Server Communication

Many thick clients depend on network-based license validation to enforce access controls and feature gating. Attackers commonly target license server communications to bypass restrictions through replay attacks, response manipulation, or exploiting offline fallback behavior. This section ensures license-related network flows are resistant to tampering and bypass.

| # | Description | Level | Source |
|---|-------------|:-----:|--------|
| V6.5.1 | Verify that license validation communications are performed over authenticated, encrypted channels and include replay protection (e.g., nonces or timestamps). | 1 | New |
| V6.5.2 | Verify that the thick client handles license server unavailability securely without exposing premium functionality or bypassing access controls during the outage. | 2 | New |

## References

- [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
- [NIST SP 800-52 Rev. 2: Guidelines for the Selection, Configuration, and Use of TLS Implementations](https://csrc.nist.gov/publications/detail/sp/800-52/rev-2/final)
- [NIST SP 800-77 Rev. 1: Guide to IPsec VPNs](https://csrc.nist.gov/publications/detail/sp/800-77/rev-1/final)
