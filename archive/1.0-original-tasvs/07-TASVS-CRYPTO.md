# TASVS-CRYPTO: Cryptography

## Control Objective

Ensure that all cryptographic operations, including communication, storage, and general usage, adhere to current best practices and standards to maintain data confidentiality, integrity, and security.

## Testing Checklist

| TASVS-ID         | Description                                                                                                                                       | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-CRYPTO-1   | Communication                                                                                                                                     |    |    |    |
| TASVS-CRYPTO-1.1 | The TLS settings are in line with current best practices.                                                                                         | X  | X  | X  |
| TASVS-CRYPTO-2   | Storage                                                                                                                                           |    |    |    |
| TASVS-CRYPTO-2.1 | The thick client doesn't re-use the same cryptographic key for multiple purposes.                                                                 | X  | X  | X  |
| TASVS-CRYPTO-2.2 | All random values are generated using a sufficiently secure random number generator.                                                              |    | X  | X  |
| TASVS-CRYPTO-2.3 | The thick client does not use cryptographic protocols or algorithms that are widely considered deprecated for security purposes.                  | X  | X  | X  |
| TASVS-CRYPTO-2.4 | The thick client does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.                                      | X  | X  | X  |
| TASVS-CRYPTO-3   | General                                                                                                                                           |    |    |    |
| TASVS-CRYPTO-3.1 | Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.                 | X  | X  | X  |
| TASVS-CRYPTO-3.2 | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography. |    | X  | X  |


## Control Group Definitions

### *TASVS-CRYPTO-1 - Communication*

### TASVS-CRYPTO-1.1 - The TLS settings are in line with current best practices.

TLS should be version 1.2 or higher, with secure cipher suites and secure configurations. This includes disabling insecure protocols and cipher suites, enabling Perfect Forward Secrecy (PFS), and using strong cryptographic algorithms. TLS should be configured to provide secure communication between the thick client and the server, protecting data confidentiality and integrity.

### TASVS-CRYPTO-2.1 - The thick client doesn't re-use the same cryptographic key for multiple purposes.

Cryptographic keys should not be re-used for multiple purposes, as this can weaken the security of the encryption. Each key should be used for a specific purpose and should not be shared between different cryptographic operations. Re-using keys can increase the risk of key compromise and make it easier for attackers to decrypt sensitive data.

### TASVS-CRYPTO-2.2 - All random values are generated using a sufficiently secure random number generator.

Random values should be generated using a secure random number generator (RNG) that provides sufficient entropy to ensure randomness and unpredictability. Insecure or predictable random values can weaken the security of cryptographic operations and make it easier for attackers to guess or manipulate sensitive data.

### TASVS-CRYPTO-2.3 - The thick client does not use cryptographic protocols or algorithms that are widely considered deprecated for security purposes.

Cryptographic protocols and algorithms that are widely considered deprecated or insecure should not be used in the thick client. This includes algorithms with known vulnerabilities, weak key lengths, or insecure modes of operation.

### TASVS-CRYPTO-2.4 - The thick client does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.

Symmetric cryptography should not rely on hardcoded keys as the sole method of encryption in the thick client. Hardcoded keys can be easily extracted by attackers and used to decrypt sensitive data. Instead, cryptographic keys should be securely managed, stored, and protected to ensure the confidentiality and integrity of the encryption.

### *TASVS-CRYPTO-3 - General*

### TASVS-CRYPTO-3.1 - Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.

Cryptographic modules should fail securely and handle errors in a way that does not enable Padding Oracle attacks. Error handling should be implemented securely to prevent attackers from exploiting vulnerabilities in the encryption and decryption process.

### TASVS-CRYPTO-3.2 - Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography.

Industry-proven or government-approved cryptographic algorithms, modes, and libraries should be used in the thick client instead of custom-coded cryptography. Using standardized cryptographic algorithms and libraries helps ensure the security and reliability of the encryption, as these algorithms have been rigorously tested and validated by security experts.


\newpage{}