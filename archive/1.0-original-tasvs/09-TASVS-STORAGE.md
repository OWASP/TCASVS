# TASVS-STORAGE: Data Storage

## Control Objective


## Testing Checklist

| TASVS-ID          | Description                                                                                                                                                                                                                       | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-STORAGE-1   | Sensitive Information Review                                                                                                                                                                                                      |    |    |    |
| TASVS-STORAGE-1.1 | Binaries or config files contain usernames, password, connection strings or API keys etc.                                                                                                                                          | X  | X  | X  |
| TASVS-STORAGE-1.2 | Registry entires contain usernames, password, connection strings or API keys etc.                                                                                                                                                  | X  | X  | X  |
| TASVS-STORAGE-1.3 | Make sure that logs are not capturing or saving sensitive data such as PII or any types of credentials used for connecting to external resources or even other resources on the machine where the application is running.         | X  | X  | X  |
| TASVS-STORAGE-1.4 | The thick client does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.                                                                                                        | X  | X  | X  |
| TASVS-STORAGE-1.5 | Trivial static analysis does not reveal important code or data.                                                                                                                                                                   | X  | X  | X  |
| TASVS-STORAGE-1.6 | Verify that regulated private, health or financial data is stored encrypted while at rest, such as Personally Identifiable Information (PII), sensitive personal information, or data assessed likely to be subject to EU's GDPR. | X  | X  | X  |
| TASVS-STORAGE-1.7 | Authentication or session tokens cannot be easily obtained.                                                                                                                                                                       | X  | X  | X  |
| TASVS-STORAGE-2   | DLL Hijacking (Trusted application manipulation into loading a malicious DLL).                                                                                                                                                     |    |    |    |
| TASVS-STORAGE-2.1 | DLL Replacement: Swapping a genuine DLL with a malicious one, optionally using DLL Proxying to preserve the original DLL's functionality.                                                                                         | X  | X  | X  |
| TASVS-STORAGE-2.2 | DLL Search Order Hijacking: Placing the malicious DLL in a search path ahead of the legitimate one, exploiting the application's search pattern.                                                                              | X  | X  | X  |

## Control Group Definitions

### *TASVS-STORAGE-1 - Sensitive Information Review*

### TASVS-STORAGE-1.1 - Binaries or config files contain usernames, password, connection strings or API keys etc.

Analyze the thick client's binaries and configuration files to identify any sensitive information such as usernames, passwords, connection strings, or API keys. Ensure that this information is not stored in plaintext or exposed in a way that could be easily extracted by an attacker.

### TASVS-STORAGE-1.2 - Registry entires contain usernames, password, connection strings or API keys etc.

Review the thick client's registry entries to identify any sensitive information such as usernames, passwords, connection strings, or API keys. Ensure that this information is not stored in plaintext or exposed in a way that could be easily extracted by an attacker.

### TASVS-STORAGE-1.3 - Make sure that logs are not capturing or saving sensitive data such as PII or any types of credentials used for connecting to external resources or even other resources on the machine where the application is running.

Review the thick client's logging mechanisms to ensure that sensitive data such as Personally Identifiable Information (PII) or credentials used for connecting to external resources are not captured or saved in logs. Ensure that logs are properly sanitized and do not expose sensitive information that could be used by an attacker.

### TASVS-STORAGE-1.4 - The thick client does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.

Ensure that the thick client does not hold sensitive data in memory longer than necessary and that memory is cleared explicitly after use. This helps prevent sensitive data from being exposed to unauthorized users who may attempt to access memory contents.

### TASVS-STORAGE-1.5 - Trivial static analysis does not reveal important code or data.

A casual observer should not be able to easily extract important code or data from the thick client through trivial static analysis. Ensure that sensitive information is obfuscated or protected in a way that makes it difficult to extract or manipulate.

### TASVS-STORAGE-1.6 - Verify that regulated private, health or financial data is stored encrypted while at rest, such as Personally Identifiable Information (PII), sensitive personal information, or data assessed likely to be subject to EU's GDPR.

Ensure that regulated private, health, or financial data is stored encrypted while at rest, such as Personally Identifiable Information (PII), sensitive personal information, or data assessed likely to be subject to the EU's General Data Protection Regulation (GDPR). Encryption helps protect sensitive data from unauthorized access and ensures compliance with data protection regulations.

### TASVS-STORAGE-1.7 - Authentication or session tokens cannot be easily obtained.

Ensure that authentication or session tokens used by the thick client cannot be easily obtained. Tokens should be securely managed and protected to prevent unauthorized access to sensitive resources or data.

### *TASVS-STORAGE-2 - DLL Hijacking*

### TASVS-STORAGE-2.1 - DLL Replacement: Swapping a genuine DLL with a malicious one, optionally using DLL Proxying to preserve the original DLL's functionality.

DLL Hijacking is when a trusted application manipulation into loading a malicious DLL. Try to swap a genuine DLL with a malicious one, optionally using DLL Proxying to preserve the original DLL's functionality.

### TASVS-STORAGE-2.2 - DLL Search Order Hijacking: Placing the malicious DLL in a search path ahead of the legitimate one, exploiting the application's search pattern.

DLL Hijacking is when a trusted application manipulation into loading a malicious DLL. Try to place the malicious DLL in a search path ahead of the legitimate one, exploiting the application's search pattern.



\newpage{}