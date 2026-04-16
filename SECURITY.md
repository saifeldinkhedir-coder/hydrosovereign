# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 6.5.x   | ✅ Yes    |
| < 6.5   | ❌ No     |

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public issue.

Instead, email: **saifeldinkhedir@gmail.com**

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

We aim to respond within 48 hours and release a fix within 7 days.

## API Keys & Credentials

HSAE uses only **free, public APIs** (Open-Meteo, NASA GPM).
No API keys are stored in the package. The GEE service account is
only used in the companion Streamlit application, not this package.
