# Security Findings Register

## Assessment Scope

- Target: Locally hosted OWASP Juice Shop
- Environment: Docker
- Application URL: http://localhost:3000
- Assessment type: Application security and software dependency assessment

## Findings Register

| ID | Finding | Classification | Status | Evidence |
|---|---|---|---|---|
| F-001 | Unsafe SQL query construction | Strong evidence | Remediation demonstrated separately | TC-006–TC-012 |
| F-002 | Verbose database error disclosure | Confirmed vulnerability | Remediation demonstrated separately | TC-008, TC-009, TC-011 |
| F-003 | Missing Content Security Policy | Hardening recommendation | Open | TC-023, TC-024 |
| F-004 | Missing Referrer-Policy | Hardening recommendation | Open | TC-023, TC-024 |
| F-005 | Missing HSTS | Not applicable to local HTTP | N/A | TC-023, TC-024 |
| F-006 | Wildcard CORS configuration | Potential weakness | Further investigation required | TC-025 |
| F-007 | Authentication token stored in local storage | Potential weakness | Further investigation required | TC-026–TC-028 |
| F-008 | Vulnerable Python dependencies | Confirmed by SCA | Remediated and verified | TC-029–TC-031 |

## Positive Security Observations

- X-Frame-Options header present with SAMEORIGIN.
- X-Content-Type-Options header present with nosniff.
- Authentication token removed from local storage following logout.
- All six standalone remediation tests passed.
- No known vulnerabilities reported in the updated automation dependency configuration.
- Automation functionality remained operational following dependency remediation.

## Assessment Limitations

- Full SQL injection exploitability was not established.
- SQL remediation was demonstrated in a standalone Python implementation rather than applied directly to Juice Shop.
- CORS exploitability was not established.
- Server-side authentication token invalidation was not verified.
- Dependency scanning was limited to the Python automation dependencies.
- The assessment was conducted in a local testing environment rather than a production deployment.