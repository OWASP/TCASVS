# OWASP Thick Client Application Security Verification Standard (TCASVS)

[![Downloads](https://img.shields.io/github/downloads/owasp/TCASVS/total?logo=github&logoColor=white&style=flat-square)](https://github.com/owasp/TCASVS/releases)
[![GitHub contributors](https://img.shields.io/github/contributors/owasp/TCASVS)](https://github.com/owasp/TCASVS/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/owasp/TCASVS)](https://github.com/owasp/TCASVS/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/owasp/TCASVS)](https://github.com/owasp/TCASVS/pulls)
[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

## Introduction

The OWASP Thick Client Application Security Verification Standard (TCASVS) provides a comprehensive set of security requirements for designing, building, and testing thick client applications — desktop software, native applications, and other locally-executed programs that operate outside a browser sandbox.

The TCASVS fills the gap between the [OWASP Application Security Verification Standard (ASVS)](https://github.com/OWASP/ASVS) for web applications and the [Mobile Application Security Verification Standard (MASVS)](https://github.com/OWASP/owasp-masvs). While the MASVS can be applied to thick client testing, it is not an ideal fit. The TCASVS provides a standard purpose-built for thick client scenarios.

## Latest Stable Version — 5.0.0

The standard source is available in the [`5.0/en/`](5.0/en/) folder. It includes 6 chapters covering 130+ security requirements across three verification levels.

| Chapter | Title |
|---------|-------|
| V1 | [Architecture and Threat Modeling](5.0/en/0x10-V1-Architecture-and-Threat-Modeling.md) |
| V2 | [Build, Deployment, and Environment Hardening](5.0/en/0x11-V2-Build-Deployment-and-Environment-Hardening.md) |
| V3 | [Data Storage and Protection](5.0/en/0x12-V3-Data-Storage-and-Protection.md) |
| V4 | [Code Quality and Exploit Mitigation](5.0/en/0x13-V4-Code-Quality-and-Exploit-Mitigation.md) |
| V5 | [Cryptography](5.0/en/0x14-V5-Cryptography.md) |
| V6 | [Network Communication](5.0/en/0x15-V6-Network-Communication.md) |

## Project Leaders and Working Group

The project is led by [Dave Hanson](https://github.com/JeffreyShran) and [Samuel Aubert](https://github.com/matreurai), supported by some former and other active AppSec team members at Bentley Systems: [Einaras Bartkus](https://github.com/eb-bsi), [Thomas Chauchefoin](https://www.linkedin.com/in/thomaschauchefoin), and [John Cotter](https://www.linkedin.com/in/john-cotter-40338612/).

The project is also supported by the OWASP community and the OWASP Foundation. Special thanks to [Starr Brown](https://github.com/mamicidal) for her support in her capacity as Director of Projects.

## Standard Objectives

- Help organizations adopt or adapt a high quality secure coding standard for thick client applications.
- Help architects and developers build secure thick client software by designing and building security in, and verifying that controls are in place and effective.
- Help security reviewers use a comprehensive, consistent, high quality standard for thick client security assessments, code reviews, and penetration testing.
- Provide a framework for procurement and vendor assessment of thick client application security.

## Contributing

Please [log issues](https://github.com/OWASP/TCASVS/issues) if you find bugs or have ideas. We welcome pull requests based on discussion in issues.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Contributors

<a href="https://github.com/OWASP/TCASVS/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OWASP/TCASVS" />
</a>

## Sponsors

<a href="https://www.bentley.com/company/about-us/">
  <div>
    <img src="images/BentleyLOGO_BLK_type.jpg" width="230" alt="Bentley Systems" />
  </div>
  <b>
    Bentley is the leading provider of infrastructure engineering software, advancing infrastructure for better quality of life and sustainability.
  </b>
  <div>
    <sup>Visit <u>bentley.com</u> to learn more.</sup>
  </div>
</a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=OWASP/TCASVS&type=Date)](https://star-history.com/#OWASP/TCASVS&Date)

## License

The entire project content is under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Related Projects

- [OWASP Application Security Verification Standard (ASVS)](https://github.com/OWASP/ASVS)
- [OWASP Mobile Application Security Verification Standard (MASVS)](https://github.com/OWASP/owasp-masvs)
- [OWASP Software Assurance Maturity Model (SAMM)](https://github.com/OWASP/samm)