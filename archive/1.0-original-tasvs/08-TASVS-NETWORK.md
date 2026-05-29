# TASVS-NETWORK: Communication and Privacy

## Control Objective

 Ensure that all network communications and services are secure, encrypted, and protected against unauthorized access, data leakage, and injection attacks.

## Testing Checklist

| TASVS-ID          | Description                                                                                                                                                                                                                                                                            | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-NETWORK-1   | Data leakage                                                                                                                                                                                                                                                                           |    |    |    |
| TASVS-NETWORK-1.1 | Verify that tokens and keys are not sent in plain text or otherwise easily decodable/decryptable by MITM attack.                                                                                                                                                                                            | X  | X  | X  |
| TASVS-NETWORK-1.2 | Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.                                                                                                                                                                                | X  | X  | X  |
| TASVS-NETWORK-2   | Licensing & Authentication Servers                                                                                                                                                                                                                                        |    |    |    |
| TASVS-NETWORK-2.1 | Verify that session tokens possess at least 64 bits of entropy.                                                                                                                                                                                                                        | X  | X  | X  |
| TASVS-NETWORK-2.2 | Verify the application generates a new session token on user authentication.                                                                                                                                                                                                           | X  | X  | X  |
| TASVS-NETWORK-2.3 | Verify that session tokens are generated using approved cryptographic algorithms.                                                                                                                                                                                                      | X  | X  | X  |
| TASVS-NETWORK-2.4 | If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period.                                                                                                                                 | X  | X  | X  |
| TASVS-NETWORK-2.5 | Verify shared or default accounts are not present (e.g. "root" or "admin").                                                                                                                                                                                                            | X  | X  | X  |
| TASVS-NETWORK-2.6 | Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations.                                                                                                                                                                | X  | X  | X  |
| TASVS-NETWORK-2.7 | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. | X  | X  | X  |
| TASVS-NETWORK-3   | Piracy Detection                                                                                                                                                                                                                                                                       |    |    |    |
| TASVS-NETWORK-3.1 | Memory monitoring in place.                                                                                                                                                                                                                                                             | X  | X  | X  |
| TASVS-NETWORK-3.2 | Telemetery capturing data when binary tampering detected, the software's behavior is unusual or when the internet connection is lost or the license is invalid.                                                                                                                        | X  | X  | X  |
| TASVS-NETWORK-4   | Connected Services                                                                                                                                                                                                                                                                     |    |    |    |
| TASVS-NETWORK-4.1 | Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection.                                                                                                                                                             | X  | X  | X  |
| TASVS-NETWORK-4.2 | Verify that the application sanitizes user input before passing to AD systems to protect against LDAP injection.                                                                                                                                                                       | X  | X  | X  |
| TASVS-NETWORK-4.3 | Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL injection attacks.                                                                                                  | X  | X  | X  |
| TASVS-NETWORK-4.4 | Verify that the thick client doesn't expose services on the network like debugging features, even if bound to the local host.                                                                                                                                                          | X  | X  | X  |


## Control Group Definitions

### *TASVS-NETWORK-1 - Data leakage*

### TASVS-NETWORK-1.1 - Verify that tokens and keys are not sent in plain text or otherwise easily decodable/decryptable by MITM attack.

Easily discoverable tokens and keys can be used to compromise the security of the application. Sending tokens and keys in plain text or using weak encryption can expose sensitive information to attackers.

### TASVS-NETWORK-1.2 - Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.

Data should be encrypted on the network using Transport Layer Security (TLS) to protect it from eavesdropping and interception by attackers. TLS provides secure communication between the thick client and the server, ensuring the confidentiality and integrity of data transmitted over the network.

### *TASVS-NETWORK-2 - Licensing & Authentication Servers*

### TASVS-NETWORK-2.1 - Verify that session tokens possess at least 64 bits of entropy.

Session tokens should possess sufficient entropy to prevent brute force attacks and guessing by attackers. Tokens with at least 64 bits of entropy are considered secure and can help protect against unauthorized access and session hijacking.

### TASVS-NETWORK-2.2 - Verify the application generates a new session token on user authentication.

Generating a new session token on user authentication helps prevent session fixation attacks and ensures that each user session is unique and secure. It is essential to create a new session token for each user authentication to protect against session hijacking and unauthorized access to user accounts.

### TASVS-NETWORK-2.3 - Verify that session tokens are generated using approved cryptographic algorithms.

Session tokens should be generated using approved cryptographic algorithms to ensure their security and integrity. Using strong cryptographic algorithms helps protect session tokens from tampering and unauthorized access by attackers.

### TASVS-NETWORK-2.4 - If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period.

Re-authentication helps protect user accounts from unauthorized access and session hijacking by requiring users to verify their identity periodically. Re-authentication should occur both when actively used and after an idle period to ensure the security of user sessions and prevent unauthorized access to user accounts.

### TASVS-NETWORK-2.5 - Verify shared or default accounts are not present (e.g. "root" or "admin").

Shared or default accounts can pose a security risk to the application by providing unauthorized access to sensitive information and resources. It is essential to ensure that shared or default accounts are not present in the application to prevent unauthorized access and protect user accounts from compromise.

### TASVS-NETWORK-2.6 - Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations.

Session tokens provide a secure and reliable method for user authentication and authorization in the application. Using session tokens instead of static API secrets and keys helps protect sensitive information from unauthorized access and session hijacking.

### TASVS-NETWORK-2.7 - Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.

The principle of least privilege helps protect the application from unauthorized access and privilege escalation by restricting user access to only the resources and functions they need to perform their tasks. Users should only be able to access functions, data files, URLs, controllers, services, and other resources for which they possess specific authorization.

### *TASVS-NETWORK-3 - Piracy Detection*

### TASVS-NETWORK-3.1 - Memory monitoring in place.

Memory monitoring helps detect and prevent unauthorized access to sensitive information stored in memory. Monitoring memory usage and access can help identify and mitigate memory-related vulnerabilities and attacks, such as buffer overflows, memory leaks, and injection attacks.

### TASVS-NETWORK-3.2 - Telemetery capturing data when binary tampering detected, the software's behavior is unusual or when the internet connection is lost or the license is invalid.

Telemetry capturing helps detect and respond to suspicious activities, unusual behavior, and security incidents in the application. Capturing telemetry data when binary tampering is detected, the software's behavior is unusual, or the internet connection is lost can help identify and mitigate security threats and attacks.

### *TASVS-NETWORK-4 - Connected Services*

### TASVS-NETWORK-4.1 - Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection.

Sanitization of user input helps prevent injection attacks and protect the application from unauthorized access and data leakage. Sanitizing user input before passing it to mail systems can help prevent SMTP or IMAP injection attacks and ensure the security of the application.

### TASVS-NETWORK-4.2 - Verify that the application sanitizes user input before passing to AD systems to protect against LDAP injection.

Sanitization of user input helps prevent injection attacks and protect the application from unauthorized access and data leakage. Sanitizing user input before passing it to Active Directory (AD) systems can help prevent LDAP injection attacks and ensure the security of the application.

### TASVS-NETWORK-4.3 - Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL injection attacks.

Data selection or database queries should use parameterized queries, Object-Relational Mapping (ORM), entity frameworks, or other secure methods to protect against SQL injection attacks. Using parameterized queries and secure data access methods can help prevent SQL injection attacks and ensure the security of the application.

### TASVS-NETWORK-4.4 - Verify that the thick client doesn't expose services on the network like debugging features, even if bound to the local host.

Exposing services on the network can pose a security risk to the application by providing unauthorized access to sensitive information and resources. It is essential to ensure that the thick client does not expose services on the network, even if bound to the local host, to prevent unauthorized access and protect user accounts from compromise.




\newpage{}