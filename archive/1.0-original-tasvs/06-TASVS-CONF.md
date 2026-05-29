# TASVS-CONF: Configuration and Building


## Control Objective

Ensure that the application's configuration management processes are secure, reliable, and automated. This includes verifying secure build and deployment processes, proper compiler flag configurations, automated deployment scripts, removal of unnecessary features, sourcing third-party components from trusted repositories, maintaining a Software Bill of Materials (SBOM), and keeping all software components up-to-date.

This control objective helps mitigate security vulnerabilities, ensures compliance, and maintains the integrity and availability of the application.

## Testing Checklist

| TASVS-ID       | Description                                                                                                                                                                                                                                                                        | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-CONF-1   | General Configuration Checks                                                                                                                                                                                                                                                       |    |    |    |
| TASVS-CONF-1.1 | Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI/CD automation, automated configuration management, and automated deployment scripts.                                                                           | X  | X  | X  |
| TASVS-CONF-1.2 | Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. | X  | X  | X  |
| TASVS-CONF-1.3 | Verify that the application, configuration, and all dependencies can be re-deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.                                             |    | X  | X  |
| TASVS-CONF-1.4 | Verify that all unneeded features, documentation, sample applications and configurations are removed.                                                                                                                                                                              | X  | X  | X  |
| TASVS-CONF-1.5 | Verify that third party components come from pre-defined, trusted and continually maintained repositories.                                                                                                                                                                         | X  | X  | X  |
| TASVS-CONF-1.6 | Verify that a Software Bill of Materials (SBOM) is maintained of all third party libraries in use.                                                                                                                                                                                 | X  | X  | X  |
| TASVS-CONF-2    | Privileges and Permissions.                                                                                                                                                                                                                                                        |    |    |    |
| TASVS-CONF-2.1  | Ensure that the software follows the principle of least privileges and runs with the lowest level of privileges for it to work as expected. If several levels of privileges are required, their IPC interfaces are well-defined and do not expose more features than required.                 | X  | X  | X  |
| TASVS-CONF-2.2  | The thick client follows the "Rule of 2", where it cannot have more than 2 of: works with untrustworthy inputs, is written in memory unsafe language, runs with high privileges / without a sandbox.                                                                                           | X  | X  | X  |
| TASVS-CONF-2.3  | Permissions are properly configured on all folders opened, deleted, modified or created during the installation process, upon using a feature (e.g. Logs created locally on demand) and at runtime.                                                                                           | X  | X  | X  |


## Control Group Definitions

### *TASVS-CONF-1 - General Configuration Checks*

### TASVS-CONF-1.1 - Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI/CD automation, automated configuration management, and automated deployment scripts.

Build and deployments processes should be automated, secure, and repeatable. This includes using CI/CD automation, automated configuration management, and automated deployment scripts. These processes help ensure that the application is built and deployed consistently and securely, reducing the risk of errors and vulnerabilities.

### TASVS-CONF-1.2 - Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found.

Compiler flags should be configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. These protections help prevent common security vulnerabilities such as buffer overflows and format string vulnerabilities.

### TASVS-CONF-1.3 - Verify that the application, configuration, and all dependencies can be re-deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.

The application, configuration, and all dependencies should be able to be re-deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion. This ensures that the application can be quickly restored in the event of a failure or disaster, reducing downtime and ensuring business continuity.

### TASVS-CONF-1.4 - Verify that all unneeded features, documentation, sample applications and configurations are removed.

Unneeded features, documentation, sample applications, and configurations should be removed from the application. This helps reduce the attack surface of the application, improve performance, and simplify maintenance. Removing unnecessary features also reduces the risk of security vulnerabilities and compliance issues.

### TASVS-CONF-1.5 - Verify that third party components come from pre-defined, trusted and continually maintained repositories.

Third-party components should come from pre-defined, trusted, and continually maintained repositories. This helps ensure that the components are secure, reliable, and up-to-date. Sourcing components from trusted repositories reduces the risk of introducing security vulnerabilities, malware, or other issues into the application.

### TASVS-CONF-1.6 - Verify that a Software Bill of Materials (SBOM) is maintained of all third party libraries in use.

A Software Bill of Materials (SBOM) should be maintained of all third-party libraries in use. An SBOM provides a detailed inventory of all software components used in the application, including third-party libraries, frameworks, and runtimes. This helps track dependencies, identify vulnerabilities, and ensure compliance with licensing requirements.


### *TASVS-CONF-2 - Privileges and Permissions*

### TASVS-CONF-2.1 - Ensure that the software follows the principle of least privileges and runs with the lowest level of privileges for it to work as expected. If several levels of privileges are required, their IPC interfaces are well-defined and do not expose more features than required.

The thick client should follow the principle of least privileges and run with the lowest level of privileges required for it to work as expected. If several levels of privileges are required, their IPC interfaces should be well-defined and not expose more features than required. This can help to prevent attackers from exploiting privilege escalation vulnerabilities to compromise the thick client.

For example, if the thick client runs with elevated privileges, an attacker could exploit a vulnerability in the thick client to gain access to sensitive information or execute arbitrary code. By running the thick client with the lowest level of privileges required for it to work as expected, the attack surface is reduced and the risk of privilege escalation vulnerabilities is minimized.


### TASVS-CONF-2.2 - The thick client follows the "Rule of 2", where it cannot have more than 2 of: works with untrustworthy inputs, is written in memory unsafe language, runs with high privileges / without a sandbox.

The thick client should follow the "Rule of 2", where it cannot have more than 2 of the following characteristics:

- Works with untrustworthy inputs
- Is written in a memory-unsafe language
- Runs with high privileges or without a sandbox

This can help to prevent attackers from exploiting security vulnerabilities in the thick client. For example, if the thick client works with untrustworthy inputs and is written in a memory-unsafe language, an attacker could exploit memory vulnerabilities to execute arbitrary code. By following the "Rule of 2", the thick client can reduce the risk of security vulnerabilities and protect sensitive information from unauthorized access.


### TASVS-CONF-2.3 - Permissions are properly configured on all folders opened, deleted, modified or created during the installation process, upon using a feature (e.g. Logs created locally on demand) and at runtime.

The thick client should restrict permissions on all folders created during its installation and at runtime to reduce the risks of Symlinks attacks and other persistence or privilege escalation scenarios.

Processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.

When creating or opening files:
- Check if the file already exists before creating it
- Depending on the programming language, use flags to prevent following symlinks (e.g. O_NOFOLLOW in Golang)
- Implement proper error handling
- Be cautious of race conditions between checking file existence and performing operations. Use atomic operations where possible in order to mitigate risks of Time-of-Check-to-Time-of-Use (TOCTOU) Vulnerabilities.

For example:
```go
file, err := os.OpenFile("filename", 
os.O_RDWR|os.O_CREATE|syscall.O_NOFOLLOW, 0666)
if err != nil {
  // Handle error
}
```

\newpage{}