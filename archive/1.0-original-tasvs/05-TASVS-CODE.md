# TASVS-CODE: Code Quality and Exploit Mitigation

## Control Objective

To ensure that the application's source code is developed and maintained in a manner that minimizes the introduction of security vulnerabilities. 

## Testing Checklist


| TASVS-ID        | Description                                                                                                                                                                                                                                                                                    | L1 | L2 | L3 |
| ---- | ------------- | - | - | - |
| TASVS-CODE-1    | Server Side                                                                                                                                                                                                                                                                                    |    |    |    |
| TASVS-CODE-1.1  | If the thick client relies on server side API's or services, defer that testing to the appropriate application security verification standard (ASVS). If testing has begun using that guide, mark this item as reviewed.                                                                       | X  | X  | X  |
| TASVS-CODE-2    | Client Side - Signing and Integrity                                                                                                                                                                                                                                                            |    |    |    |
| TASVS-CODE-2.1  | Making Sure that the thick client binary is properly signed.                                                                                                                                                                                                                                    |    |    | X  |
| TASVS-CODE-2.2  | Testing File Integrity Checks.                                                                                                                                                                                                                                                                  |    |    | X  |
| TASVS-CODE-2.3  | Testing Runtime Integrity Checks.                                                                                                                                                                                                                                                               | X  | X  | X  |
| TASVS-CODE-2.4  | The client has been built in release mode, with settings appropriate for a release build.                                                                                                                                                                                                      | X  | X  | X  |
| TASVS-CODE-2.5  | Enable framework applicable security features like byte-code minification and stack protection.                                                                                                                                                                                                | X  | X  | X  |
| TASVS-CODE-3    | Client Side - Static Code Analysis.                                                                                                                                                                                                                                                             |    |    |    |
| TASVS-CODE-3.1  | All third party components used by the thick client, such as libraries and frameworks, are identified, and checked for known vulnerabilities and are up to date, they should not be unsupported, deprecated or legacy.                                                                         | X  | X  | X  |
| TASVS-CODE-3.2  | Search the source code for cases where exceptions are thrown and not properly handled. E.g for C# use 'findstr /N /s /c:"throw;" \*.cs'. Also be on the lookout to see if the exception allows a bypass of authentication or some other critical operation.                                    | X  | X  | X  |
| TASVS-CODE-3.3  | Perform binary static analysis. (verify that the binaries are compiled with the latest compiler, examine compilation settings and validates binary signing).                                                                                                                                    | X  | X  | X  |
| TASVS-CODE-3.4  | Depending on the language(s) in use, choose appropriate static application security testing (SAST) tooling to analyze source code to identify vulnerabilities.                                                                                                                                 | X  | X  | X  |
| TASVS-CODE-3.5  | If applicable, ensure any internal tooling, policies and test cases are being implemented and evaluated correctly.                                                                                                                                                                             | X  | X  | X  |
| TASVS-CODE-3.6  | Identify and clear out any unused code. Remember, it stays in the source code repository history if needed later. Use README/changelog files for preserving high value historical context or deprecated details. Do not keep obsolete project repositories, consider archiving the repository. | X  | X  | X  |
| TASVS-CODE-4    | Client Side - Validation, Sanitization and Encoding.                                                                                                                                                                                                                                            |    |    |    |
| TASVS-CODE-4.1  | Untrusted data through features such as macros or templating is protected from code & command injection attacks. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed.                                                            | X  | X  | X  |
| TASVS-CODE-4.2  | Verify that the application protects against OS command injection.                                                                                                                                                                                                                             | X  | X  | X  |
| TASVS-CODE-4.3  | Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length.                                                                                                                                                                                   | X  | X  | X  |
| TASVS-CODE-4.4  | Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks.                                          | X  | X  | X  |
| TASVS-CODE-4.5  | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows.                                                                                                                                           | X  | X  | X  |
| TASVS-CODE-4.6  | Verify that format strings do not take potentially hostile input, and are constant.                                                                                                                                                                                                            | X  | X  | X  |
| TASVS-CODE-4.7  | Verify that sign, range, and input validation techniques are used to prevent integer overflows.                                                                                                                                                                                                | X  | X  | X  |
| TASVS-CODE-4.8  | Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.                                                                                                                                                                     | X  | X  | X  |
| TASVS-CODE-4.9  | Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).                                                                                                                                   | X  | X  | X  |
| TASVS-CODE-4.10 | Is the thick client's handling of spawning processes done securely. (Validating and sanitizing process arguments)                                                                                                                                                                              | X  | X  | X  |
| TASVS-CODE-4.11 | Verify that user-submitted filename metadata is not used directly by system or framework filesystems to protect against path traversal. One example is "ZipSlip" style attacks.                                                                                                                | X  | X  | X  |
| TASVS-CODE-4.12 | In unmanaged code, memory is allocated, freed and used securely.                                                                                                                                                                                                                               | X  | X  | X  |
| TASVS-CODE-5    | Client Side - Business Logic.                                                                                                                                                                                                                                                                   |    |    |    |
| TASVS-CODE-5.1  | No sensitive data, such as passwords or pins, is exposed through the user interface.                                                                                                                                                                                                           | X  | X  | X  |
| TASVS-CODE-5.2  | Check for design practices that trick or manipulate users into making choices they would not otherwise have made and that may cause harm. AKA "deceptive patterns". See https://www.deceptive.design/types for examples.                                                                       | X  | X  | X  |
| TASVS-CODE-5.3  | Is the thick client only using workflows that do not violate common security advice?                                                                                                                                                                                                           | X  | X  | X  |
| TASVS-CODE-5.4  | Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application.                                                                                                                                     | X  | X  | X  |
| TASVS-CODE-5.5  | Check that any imported files cannot be utilized to attack the thick client.                                                                                                                                                                                                                                                    | X  | X  | X  |
| TASVS-CODE-5.6  | If the thick client registers a URL handler / protocol handler, verify that it can't trigger dangerous action or introduces common vulnerabilities (memory corruption, command and argument injection, etc.).                                                                                   | X  | X  | X  |
| TASVS-CODE-6    | Client Side - Fuzzing.                                                                                                                                                                                                                                                                          |    |    |    |
| TASVS-CODE-6.1  | Perform "dumb fuzzing" of the application with randomised input to try to cause a crash.                                                                                                                                                                                                       |    | X  | X  |
| TASVS-CODE-6.2  | Perform "smart fuzzing". Intelligently generate test cases that maximize code coverage and explore complex program states to increasing the likelihood of finding vulnerabilities over "dumb fuzzing".                                                                                         |    |    | X  |
| TASVS-CODE-7    | Client Side - Secure Coding Practices.                                                                                                                                                                                                                                                             |    |    |    |
| TASVS-CODE-7.1  | Ensure that fully qualified paths are specified when calling/loading executables or DLL files to prevent the OS from searching in other directories that could contain malicious files or for files in the wrong location and help prevents Dynamic Link Libraries (DLL) and EXE Hijacking attacks.                                                                         | X  | X  | X  |

## Control Group Definitions

### *TASVS-CODE-1 - Server Side*

### TASVS-CODE-1.1 - If the thick client relies on server side API's or services, defer that testing to the appropriate application security verification standard (ASVS). If testing has begun using that guide, mark this item as reviewed.

In an effort to avoid unnecesary cross over between the TASVS and the ASVS, this control is merely a reminder to test the server side components of the thick client using the ASVS.

### *TASVS-CODE-2 - Client Side - Signing and Integrity*

### TASVS-CODE-2.1 - Making Sure that the thick client binary is properly signed.

The thick client binary should be signed to ensure that it has not been tampered with. This is especially important for thick clients that are distributed to end users, as it provides a way to verify the authenticity of the software.

### TASVS-CODE-2.2 - Testing File Integrity Checks.

File integrity checks are used to verify that the files used by the thick client have not been tampered with. This can help to detect unauthorized changes to the software, such as the introduction of malware or other malicious code.

### TASVS-CODE-2.3 - Testing Runtime Integrity Checks.

Runtime integrity checks are used to verify that the thick client has not been tampered with while it is *running*. This can help to detect attacks that attempt to modify the software's behavior while it is in use.

### TASVS-CODE-2.4 - The client has been built in release mode, with settings appropriate for a release build.

The thick client should be built in release mode with settings appropriate for a release build. This ensures that the software is optimized for performance and security, and that any debugging information or other unnecessary code is removed.

### TASVS-CODE-2.5 - Enable framework applicable security features like byte-code minification and stack protection.

Framework security features such as byte-code minification and stack protection should be enabled to help protect the thick client from common security vulnerabilities. These features can help to prevent attacks such as buffer overflows and stack smashing.

### *TASVS-CODE-3 - Client Side - Static Code Analysis*

### TASVS-CODE-3.1 - All third party components used by the thick client, such as libraries and frameworks, are identified, and checked for known vulnerabilities and are up to date, they should not be unsupported, deprecated or legacy.

All software components, libraries, frameworks, and runtimes used in the application should be up-to-date and not end-of-life or obsolete. Outdated or obsolete components can introduce security vulnerabilities, performance issues, and compatibility problems. Keeping software components up-to-date helps ensure that the application remains secure, reliable, and compliant with industry standards and best practices.

### TASVS-CODE-3.2 - Search the source code for cases where exceptions are thrown and not properly handled. E.g for C# use 'findstr /N /s /c:"throw;" \*.cs'. Also be on the lookout to see if the exception allows a bypass of authentication or some other critical operation.

Exceptions that are thrown and not properly handled can lead to security vulnerabilities in the thick client. It is important to search the source code for cases where exceptions are thrown and not properly handled, as these can allow malicious actions to be performed.

### TASVS-CODE-3.3 - Perform binary static analysis. (verify that the binaries are compiled with the latest compiler, examine compilation settings and validates binary signing).

#### What is binary static analysis?

Binary static analysis is used to verify that the thick client binaries are compiled with the latest compiler and that the compilation settings are appropriate for security. This can help to identify security vulnerabilities in the thick client that may be introduced during the compilation process.

Framework specific tools like [dnSpy]() or [ILSpy]() can be used to decompile and analyze .NET binaries. Alternatively, tools like [Ghidra](https://ghidra-sre.org/) or [IDA Pro](https://www.hex-rays.com/products/ida/) can be used to analyze binaries in other languages.


### TASVS-CODE-3.4 - Depending on the language(s) in use, choose appropriate static application security testing (SAST) tooling to analyze source code to identify vulnerabilities.

Depending on the language(s) in use, appropriate static application security testing (SAST) tooling should be used to analyze the source code of the thick client. This can help to identify vulnerabilities in the code that may be missed during manual code review.

Tools such as [SonarQube](https://www.sonarqube.org/), [Checkmarx](https://www.checkmarx.com/), and [Veracode](https://www.veracode.com/) can be used to perform static code analysis on the thick client codebase. Plus framework specific tools like [Brakeman](https://brakemanscanner.org/) for Ruby on Rails, [Bandit](https://bandit.readthedocs.io/en/latest/) for Python, and [FindBugs](http://findbugs.sourceforge.net/) for Java.

### TASVS-CODE-3.5 - If applicable, ensure any internal tooling, policies and test cases are being implemented and evaluated correctly.

Internal tooling, policies, and test cases should be implemented and evaluated to ensure that they are working correctly. This can help to ensure that the thick client is developed and maintained in a manner that minimizes the introduction of security vulnerabilities.

These might include code review processes, automated testing tools, and security training for developers. It is important to regularly review and update these tools and processes to ensure that they are effective in identifying and mitigating security vulnerabilities.

### TASVS-CODE-3.6 - Identify and clear out any unused code. Remember, it stays in the source code repository history if needed later. Use README/changelog files for preserving high value historical context or deprecated details. Do not keep obsolete project repositories, consider archiving the repository.

Unused code should be identified and removed from the thick client codebase. This can help to reduce the attack surface of the thick client and minimize the risk of security vulnerabilities. It is important to use README and changelog files to preserve high-value historical context or deprecated details. Obsolote project repositories should be archived because they risk being used as a source of vulnerabilities in future projects.

### *TASVS-CODE-4 - Client Side - Validation, Sanitization and Encoding*

### TASVS-CODE-4.1 - Untrusted data through features such as macros or templating is protected from code & command injection attacks. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed.

Untrusted data should be protected from code and command injection attacks. This can be done by sanitizing or sandboxing user input before it is executed. If there is no alternative to including user input in the thick client, it should be sanitized or sandboxed to prevent code and command injection attacks.


### TASVS-CODE-4.2 - Verify that the application protects against OS command injection.

The thick client should protect against OS command injection attacks. This can be done by validating and sanitizing user input before it is executed, and by using secure coding practices to prevent command injection vulnerabilities.

### TASVS-CODE-4.3 - Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length.

Unstructured data should be sanitized to enforce safety measures such as allowed characters and length. This can help to prevent security vulnerabilities that may be introduced by unstructured data, such as buffer overflows or injection attacks.

### TASVS-CODE-4.4 - Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks.

The thick client should restrict XML parsers to use the most restrictive configuration possible to prevent XML eXternal Entity (XXE) attacks. This can help to prevent attackers from exploiting XML parsers to read sensitive data or execute arbitrary code on the thick client.

### TASVS-CODE-4.5 - Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows.

The thick client should use memory-safe string, safer memory copy, and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. This can help to prevent attackers from exploiting memory vulnerabilities to execute arbitrary code on the thick client.

Safe alternatives to common string functions like `strcpy` and `strcat` should be used to prevent buffer overflows. Memory-safe string functions like `strlcpy` and `strlcat` are available in many programming languages and can help to prevent buffer overflows.

### TASVS-CODE-4.6 - Verify that format strings do not take potentially hostile input, and are constant.

Format strings should not take potentially hostile input, and should be constant. This can help to prevent attackers from exploiting format string vulnerabilities to read sensitive data or execute arbitrary code on the thick client.

An attack might look like this:

```c
char buffer[100];
snprintf(buffer, sizeof(buffer), user_input);
```

If `user_input` contains a format string specifier like `%s`, an attacker could use it to read sensitive data or execute arbitrary code on the thick client.

For example if `user_input` is `"%s"`, the `snprintf` function will try to read a string from memory and write it to the buffer. This can lead to a buffer overflow or other memory corruption vulnerability.

If user_input is `"%x %x %x %x"`, `snprintf` will interpret this as reading four hexadecimal values from the stack, potentially leaking stack contents.

To mitigate this, the format string should be constant, like this:

```c
snprintf(buffer, sizeof(buffer), "%s", user_input);
```

Notice that the format string is constant i.e. `"%s"` and not `user_input`.


### TASVS-CODE-4.7 - Verify that sign, range, and input validation techniques are used to prevent integer overflows.

Sign, range, and input validation techniques should be used to prevent integer overflows. This can help to prevent attackers from exploiting integer overflows to execute arbitrary code on the thick client.

For exmaple in C/C++:

```c
int a = 100;
int b = 200;
int c = a + b;
```

If `a` and `b` are user-controlled, an attacker could set them to values that cause an integer overflow, resulting in `c` being a negative value. This can lead to unexpected behavior or security vulnerabilities in the thick client.

To mitigate this, input validation should be used to ensure that `a` and `b` are within a valid range before performing the addition:

```c
if (a > INT_MAX - b) {
    // handle error
}
int c = a + b;
```


### TASVS-CODE-4.8 - Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.

Serialized objects should use integrity checks or be encrypted to prevent hostile object creation or data tampering. This can help to prevent attackers from exploiting serialization vulnerabilities to execute arbitrary code on the thick client.

For example, if an attacker can modify a serialized object before it is deserialized, they could introduce malicious code or data into the thick client. By using integrity checks or encryption, the thick client can verify that the serialized object has not been tampered with before deserializing it.

In C# a bad example might look like this:

```csharp
using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

public class Program
{
    public static void Main()
    {
        // Serialize an object
        var obj = new MyClass();
        var formatter = new BinaryFormatter();
        var stream = new MemoryStream();
        formatter.Serialize(stream, obj);
        var serialized = stream.ToArray();

        // Deserialize the object
        var deserialized = (MyClass)formatter.Deserialize(new MemoryStream(serialized));
    }
}

[Serializable]
public class MyClass
{
    public string Name { get; set; }
}
```

In this example, an attacker could modify the `serialized` object before it is deserialized, potentially introducing malicious code or data into the thick client. To mitigate this, integrity checks or encryption should be used to verify that the serialized object has not been tampered with before deserializing it.

A good implementation might look like this:

```csharp
using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Security.Cryptography;

public class Program
{
    public static void Main()
    {
        // Serialize an object
        var obj = new MyClass();
        var formatter = new BinaryFormatter();
        var stream = new MemoryStream();
        formatter.Serialize(stream, obj);
        var serialized = stream.ToArray();

        // Calculate a hash of the serialized object
        var hash = CalculateHash(serialized);

        // Deserialize the object
        var deserialized = (MyClass)formatter.Deserialize(new MemoryStream(serialized));

        // Verify the integrity of the deserialized object
        if (!VerifyHash(serialized, hash))
        {
            // handle error
        }
    }

    public static byte[] CalculateHash(byte[] data)
    {
        using (var sha256 = SHA256.Create())
        {
            return sha256.ComputeHash(data);
        }
    }

    public static bool VerifyHash(byte[] data, byte[] hash)
    {
        using (var sha256 = SHA256.Create())
        {
            var computedHash = sha256.ComputeHash(data);
            return StructuralComparisons.StructuralEqualityComparer.Equals(computedHash, hash);
        }
    }
}

[Serializable]
public class MyClass
{
    public string Name { get; set; }
}
```

In this example, a hash of the serialized object is calculated before it is deserialized, and the hash is verified after deserialization to ensure that the object has not been tampered with. This can help to prevent attackers from exploiting serialization vulnerabilities to execute arbitrary code on the thick client.


### TASVS-CODE-4.9 - Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).

Deserialization of untrusted data should be avoided or protected in both custom code and third-party libraries. This can help to prevent attackers from exploiting deserialization vulnerabilities to execute arbitrary code on the thick client.

For example, if an attacker can control the data that is deserialized by the thick client, they could introduce malicious code or data into the application. By avoiding deserialization of untrusted data or protecting it with integrity checks or encryption, the thick client can verify that the data has not been tampered with before deserializing it.

It is recommended to use safer libraries where possible and to validate the data before deserializing it. For example, in C# the `DataContractSerializer` class can be used to deserialize JSON data in a safer way than the `BinaryFormatter` class.

```csharp
using System;
using System.IO;
using System.Runtime.Serialization.Json;

public class Program
{
    public static void Main()
    {
        // Deserialize JSON data
        var json = "{\"Name\":\"Alice\"}";
        var serializer = new DataContractJsonSerializer(typeof(MyClass));
        var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(json));
        var deserialized = (MyClass)serializer.ReadObject(stream);
    }
}

[DataContract]
public class MyClass
{
    [DataMember]
    public string Name { get; set; }
}
```

In this example, the `DataContractJsonSerializer` class is used to deserialize JSON data in a safer way than the `BinaryFormatter` class. This can help to prevent attackers from exploiting deserialization vulnerabilities to execute arbitrary code on the thick client.


### TASVS-CODE-4.10 - Is the thick client's handling of spawning processes done securely. (Validating and sanitizing process arguments)

The thick client's handling of spawning processes should be done securely. This can help to prevent attackers from exploiting process spawning vulnerabilities to execute arbitrary code on the thick client.

For example, if the thick client spawns a process with user-controlled arguments, an attacker could use this to execute arbitrary code on the thick client. By validating and sanitizing process arguments before spawning a process, the thick client can prevent attackers from exploiting process spawning vulnerabilities.

In C# a bad example might look like this:

```csharp
using System;
using System.Diagnostics;

public class Program
{
    public static void Main()
    {
        // Spawn a process with user-controlled arguments
        var process = new Process();
        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.Arguments = "/c " + user_input;
        process.Start();
    }
}
```

In this example, the `user_input` variable is used to construct the arguments for the `cmd.exe` process, potentially allowing an attacker to execute arbitrary code on the thick client. A malicious user could set `user_input` to something like `"; calc.exe;` to execute the Windows Calculator application. To mitigate this, process arguments should be validated and sanitized before spawning a process:

```csharp
using System;
using System.Diagnostics;

public class Program
{
    public static void Main()
    {
        // Validate and sanitize process arguments
        if (!IsValid(user_input))
        {
            // handle error
        }

        // Spawn a process with validated and sanitized arguments
        var process = new Process();
        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.Arguments = "/c " + user_input;
        process.Start();
    }

    public static bool IsValid(string input)
    {
        // Validate and sanitize input
        // For example, check for allowed characters and length
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        if (input.Length > 10 || input.Any(c => !allowed.Contains(c)))
        {
            return false;
        }
    
        return true;
    }
}
```

In this example, the `IsValid` function is used to validate and sanitize the `user_input` variable before it is used to construct the arguments for the `cmd.exe` process. This can help to prevent attackers from exploiting process spawning vulnerabilities to execute arbitrary code on the thick client.

### TASVS-CODE-4.11 - Verify that user-submitted filename metadata is not used directly by system or framework filesystems to protect against path traversal. One example is "ZipSlip" style attacks.

User-submitted filename metadata should not be used directly by system or framework filesystems to prevent path traversal attacks. This can help to prevent attackers from exploiting path traversal vulnerabilities to read sensitive data or execute arbitrary code on the thick client.

For example, if the thick client uses user-submitted filenames to access files on the filesystem, an attacker could use this to read sensitive data or execute arbitrary code on the thick client. By validating and sanitizing user-submitted filenames before using them to access files, the thick client can prevent attackers from exploiting path traversal vulnerabilities.

In C# a bad example might look like this:

```csharp
using System;
using System.IO;

public class Program
{
    public static void Main()
    {
        // Use user-submitted filename to access a file
        var filename = user_input;
        var path = Path.Combine("C:\\files", filename);
        var contents = File.ReadAllText(path);
    }
}
```

In this example, the `user_input` variable is used to construct the path to a file on the filesystem, potentially allowing an attacker to read sensitive data or execute arbitrary code on the thick client. A malicious user could set `user_input` to something like `..\..\..\Windows\System32\cmd.exe` to execute the Windows Command Prompt application. To mitigate this, user-submitted filenames should be validated and sanitized before using them to access files, in C# Path.GetFullPath can be used to resolve the path and more generally a known good list of paths can be used to validate the input.

```csharp
using System;
using System.IO;

public class Program
{
    public static void Main()
    {
        // Validate and sanitize user-submitted filename
        if (!IsValid(user_input))
        {
            // handle error
        }

        // Use validated and sanitized filename to access a file
        var filename = user_input;
        var path = Path.Combine("C:\\files", filename);
        var contents = File.ReadAllText(path);
    }

    public static bool IsValid(string input)
    {
        // Validate and sanitize input
        // For example, check for deny listed characters and defined list of allowed directories

        good-directories = new string[] {"C:\\files", "D:\\data"};
        deny-list = new string[] {"..", "/", "\\"};

        if (input.Any(c => deny-list.Contains(c)) || !good-directories.Contains(Path.GetDirectoryName(input)))
        {
            return false;
        }

        return true;
    }
}
```

### TASVS-CODE-4.12 - In unmanaged code, memory is allocated, freed and used securely.

Memory should be allocated, freed, and used securely in unmanaged code. This can help to prevent attackers from exploiting memory vulnerabilities to execute arbitrary code on the thick client.

For example, if memory is not allocated, freed, and used securely in unmanaged code, an attacker could exploit memory vulnerabilities to execute arbitrary code on the thick client. By using secure memory allocation, freeing, and usage practices, the thick client can prevent attackers from exploiting memory vulnerabilities.

In C/C++ a bad example might look like this:

```c
#include <stdlib.h>

void foo()
{
    // Allocate memory
    char* buffer = (char*)malloc(100);

    // Use memory
    strcpy(buffer, "Hello, world!");

    // Free memory
    free(buffer);
}
```

In this example, the `buffer` variable is allocated, used, and freed in an insecure way, potentially allowing an attacker to exploit memory vulnerabilities to execute arbitrary code on the thick client. To mitigate this, memory should be allocated, used, and freed securely:

```c
#include <stdlib.h>

void foo()
{
    // Allocate memory
    char* buffer = (char*)malloc(100);

    // Check for allocation failure
    if (buffer == NULL)
    {
        // handle error
    }

    // Use memory
    strncpy(buffer, "Hello, world!", 100);

    // Free memory
    free(buffer);
}
```

In this example, the `buffer` variable is allocated, used, and freed securely, with checks for allocation failure and bounds checking to prevent memory vulnerabilities. This can help to prevent attackers from exploiting memory vulnerabilities to execute arbitrary code on the thick client.

### *TASVS-CODE-5 - Client Side - Business Logic*

### TASVS-CODE-5.1 - No sensitive data, such as passwords or pins, is exposed through the user interface.

If passwords or pins are displayed in clear text on the user interface of the thick client, an attacker could easily steal them and use them to access sensitive information. By ensuring that sensitive data is not exposed through the user interface, the thick client can protect sensitive information from unauthorized access.


### TASVS-CODE-5.2 - Check for design practices that trick or manipulate users into making choices they would not otherwise have made and that may cause harm. AKA "deceptive patterns". See https://www.deceptive.design/types for examples.

In thick client implementations, users face significant risks due to deceptive design patterns. These include tactics like fake scarcity, forced actions, hidden costs, and trick wording, which manipulate users into making unintended decisions. For instance, users might encounter fake urgency to rush purchases or hidden subscriptions they didn't consent to. Such practices undermine user autonomy, increase the likelihood of inadvertent commitments, and obscure critical information, leading to potential financial and security implications. Ensuring transparency and user control is crucial to mitigate these risks.

For more details, visit [Deceptive Patterns.](https://www.deceptive.design/types)

### TASVS-CODE-5.3 - Is the thick client only using workflows that do not violate common security advice?

The thick client should only use workflows that do not violate common security advice. This can help to prevent attackers from exploiting security vulnerabilities in the thick client. For example, if the thick client uses insecure authentication methods or insecure data storage practices. This control is a reminder to the tester to allow intuition and experience to guide the testing process.

### TASVS-CODE-5.4 - Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application.

The attack surface of the thick client should be reduced to be as small as possible. Sandboxing or encapsulation can help to prevent attackers from exploiting vulnerabilities in third-party libraries. For example, if a third-party library has a vulnerability that allows an attacker to execute arbitrary code, sandboxing or encapsulating the library can prevent the attacker from exploiting the vulnerability to compromise the thick client. We can limit the risk by using encapsulation or sandboxing to expose only the required behavior of the third-party library to the thick client. This allows us to better test and understand the functionality consumed by the application.

An example of sandboxing a third-party library might look like this:

```csharp
using System;
using ThirdPartyLibrary;

public class Program
{
    public static void Main()
    {
        // Sandbox the third-party library
        using (var sandbox = new Sandbox())
        {
            // Use the third-party library in the sandbox
            sandbox.DoSomething();
        }
    }
}
```

In this example, the `Sandbox` class is used to encapsulate the `ThirdPartyLibrary` and prevent it from accessing code outside of the sandbox.


### TASVS-CODE-5.5 - Check that any imported files cannot be utilized to attack the thick client.

To prevent attackers from exploiting vulnerabilities in imported files to compromise the thick client, validation and sanitizing of any files should occur before using them. For example, if the thick client imports data from a CSV file, the file should be validated and sanitized.

### TASVS-CODE-5.6 - If the thick client registers a URL handler / protocol handler, verify that it can't trigger dangerous action or introduces common vulnerabilities (memory corruption, command and argument injection, etc.).

If the thick client registers a URL handler or protocol handler, it is important to verify that it cannot trigger dangerous actions or introduce common vulnerabilities. For example, if the thick client registers a URL handler that allows it to open a file or execute a command, an attacker could use this to exploit memory corruption, command and argument injection, or other vulnerabilities. To mitigiate this, the thick client should validate and sanitize the URL handler or protocol handler before registering it or alternatively use an allow list of known good URLs or handlers.

### *TASVS-CODE-6 - Client Side - Fuzzing*

### TASVS-CODE-6.1 - Perform "dumb fuzzing" of the application with randomised input to try to cause a crash.

Performing "dumb fuzzing" of the thick client with randomized input can help to identify security vulnerabilities that may be missed during manual code review. By generating random input and testing the thick client with it, the tester can identify potential security vulnerabilities that may be exploitable by an attacker.

One way to do this quickly is to use a fuzzer like [AFL]() or [libFuzzer](). These tools can automatically generate test cases and run them against the thick client to identify security vulnerabilities.

### TASVS-CODE-6.2 - Perform "smart fuzzing". Intelligently generate test cases that maximize code coverage and explore complex program states to increasing the likelihood of finding vulnerabilities over "dumb fuzzing".

Performing "smart fuzzing" of the thick client can help to identify security vulnerabilities that may be missed during manual code review. By intelligently generating test cases that maximize code coverage and explore complex program states, the tester can increase the likelihood of finding vulnerabilities over "dumb fuzzing".

One way to do this is to use a fuzzer like [AFL]() or [libFuzzer]() with custom test case generation strategies, such as harnesses or mutators. These tools can automatically generate test cases and run them against the thick client to identify security vulnerabilities.


### *TASVS-CODE-7 - Client Side - Secure Coding Practices*

### TASVS-CODE-7.1 - Ensure that fully qualified paths are specified when calling/loading executables or DLL files to prevent the OS from searching in other directories that could contain malicious files or for files in the wrong location and help prevents Dynamic Link Libraries (DLL) and EXE Hijacking attacks.

DLL Hijacking is an attack technique that consists of tricking an application into loading an altered DLL file. Under normal operation, when an application depends on a DLL file, it loads it into memory. However, a malicious actor can take advantage of this process by injecting malicious code into the DLL file. As a result, the application unknowingly executes the malicious code, altering its behavior. EXE Hijacking is the same idea, but for EXEs calls on runtime.

For example, if the program is running with elevated privileges, DLL Hijacking may lead to privilege escalation. DLL hijacking can also be used to evade anti-malware detection, by leveraging a legitimate, whitelisted application to load a malicious DLL. Furthermore, since many applications load DLL files during startup, the attacker can gain access each time the system boots. Therefore, ensuring persistence.

Example:
```c
LoadLibrary("example.dll"); // Unsafe, instead use:
LoadLibrary("C:\\Program Files\\MyApp\\example.dll"); // Safer
```


### TASVS-CODE-7.2 - Ensure that safe file operations, such as when creating or opening files, are used to prevent Symlinks attacks.



\newpage{}
