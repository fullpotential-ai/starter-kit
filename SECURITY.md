# Security Policy

## Public Repository Policy

This is a **PUBLIC** repository. It is visible to the entire world.

### What Belongs Here
- Generic templates
- Documentation
- Interface definitions
- Example code with placeholders

### What NEVER Belongs Here
- **Real Credentials:** API keys, passwords, tokens, secrets.
- **Internal URLs:** Development server addresses, private registry URLs.
- **Server IPs:** Specific IP addresses of our infrastructure.
- **PII:** Personally Identifiable Information.

### Using Placeholders
Always use standard placeholders for sensitive data:
- `[PROVIDED BY COORDINATOR]`
- `your-secret-here`
- `https://registry.example.com`

## Reporting Security Issues

If you discover a security vulnerability in this starter kit or inadvertently exposed secrets:

1.  **DO NOT** open a public GitHub issue.
2.  Contact the security coordinator directly via private channel.
3.  If you pushed a secret, immediately rotate the credential and rewrite git history if possible (or squash the commit).

