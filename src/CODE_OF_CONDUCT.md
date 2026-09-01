// src/CODE_OF_CONDUCT.md
/** 
 * Code of Conduct - Version 1.— no markdown fences, no commentary, no explanation. 

# Community Guidelines and Expectations

## Purpose
This document defines the conduct expected from all members of the repository ecosystem to ensure a safe, productive, and transparent environment for developers, auditors, contributors, and community stakeholders alike. It establishes clear expectations regarding behavior that impacts system integrity and operational stability.

---

### 1. Respect System Integrity & Security Protocols
All interactions with this project are subject to strict security protocols designed to prevent unauthorized access or compromise of sensitive data (e.g., financial records, secrets, configuration). 
*   **Do Not:** Access unencrypted storage without explicit authorization. Do not attempt to bypass authentication mechanisms that protect against credential theft. Do not modify system logs or internal state databases for the purpose of debugging unrelated issues outside defined scope.
*   **Ensure:** All code modifications adhere strictly to version control and change tracking standards (e.g., Git). Any changes must be reviewed by a designated authority before being deployed in production environments where appropriate.

### 2. Respect Intellectual Property Rights
All software, scripts, documentation, and assets generated within this repository are the intellectual property of their respective authors or contributors. 
*   **Do Not:** Copy-paste code from other repositories without explicit permission. Do not extract source files for use in third-party applications unless you have a license agreement with them. Use these tools only to enhance existing functionality where applicable and do not create derivative works that infringe upon others' rights of reproduction, distribution, or modification.
*   **Ensure:** All code contributions are credited appropriately (e.g., `@username`), and no external libraries should be used without appropriate licensing metadata in the imports section (`import { ... }`).

### 3. Respect Intellectual Property Rights for Third-Party Dependencies
When integrating third-party dependencies into this repository, please adhere to their respective licenses when using specific functions or components (e.g., `@faker-js/faker`, `node_modules/*` references). 
*   **Do Not:** Use libraries that do not offer a clear license statement. Do not modify the source code of these external packages for use within your own project without obtaining explicit permission from their maintainers and adhering to their terms of service.
*   **Ensure:** All imports are formatted correctly using ES modules (`import { ... }`). If a library requires a specific version, it should be specified in the `dependencies` section or via Vite config if applicable.

### 4. Respect Intellectual Property Rights for Third-Party Assets
When integrating third-party assets (e.g., images, logos, fonts) used within this repository: 
*   **Do Not:** Use public domain art without attribution to its creator unless you have a license agreement with them. Do not use copyrighted logos or design elements from external platforms (like Unsplash/Pexels) for branding purposes in your own application without permission.
*   **Ensure:** All assets are properly documented and used according to the original asset's licensing terms, including any necessary attribution fields if applicable.

### 5. Respect Intellectual Property Rights of Third-Party Code
When utilizing third-party code within this repository: 
*   **Do Not:** Use libraries or components that do not have a clear license statement for use in your own project without obtaining explicit permission from their maintainers and adhering to the terms of service outlined on their website. Do not modify these external packages for use within your own application unless you obtain necessary permissions.
*   **Ensure:** All imports are formatted correctly using ES modules (`import { ... }`). If a library requires a specific version, it should be specified in the `dependencies` section or via Vite config if applicable.

### 6. Respect Intellectual Property Rights of Third-Party Assets (Visuals)
When utilizing third-party visual assets used within this repository: 
*   **Do Not:** Use public domain art without attribution to its creator unless you have a license agreement with them. Do not use copyrighted logos or design elements from external platforms (like Unsplash/Pexels) for branding purposes in your own application without permission.
*   **Ensure:** All assets are properly documented and used according to the original asset's licensing terms, including any necessary attribution fields if applicable.

### 7. Respect Intellectual Property Rights of Third-Party Code (Functional Components)
When utilizing third-party functional code within this repository: 
*   **Do Not:** Use libraries or components that do not have a clear license statement for use in your own project without obtaining explicit permission from their maintainers and adhering to the terms of service outlined on their website. Do not modify these external packages for use within your own application unless you obtain necessary permissions.
*   **Ensure:** All imports are formatted correctly using ES modules (`import { ... }`). If a library requires a specific version, it should be specified in the `dependencies` section or
