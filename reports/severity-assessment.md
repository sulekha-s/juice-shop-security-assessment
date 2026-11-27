# Vulnerability Severity Assessment

## Scoring Methodology

CVSS v3.1 was selected as the standardised framework for assessing technical vulnerability severity.

## F-002 — Verbose Database Error Disclosure

**CVSS Base Score:** 5.3

**Severity:** Medium

**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N

| Metric | Selection | Justification |
|---|---|---|
| Attack Vector | Network | Vulnerable functionality is accessible through HTTP requests. |
| Attack Complexity | Low | The error disclosure was reliably reproduced without special conditions. |
| Privileges Required | None | Authentication was not required. |
| User Interaction | None | No interaction from another user was required. |
| Scope | Unchanged | No impact beyond the application's security authority was demonstrated. |
| Confidentiality | Low | Internal SQL queries and database errors were disclosed. |
| Integrity | None | No unauthorised data modification was demonstrated. |
| Availability | None | No service disruption was demonstrated. |

## Supporting Evidence

- TC-008: Apostrophe handling
- TC-009: Vulnerability reproduction
- TC-011: Apostrophe variation

## Limitations

The score is provisional and based on the observed information disclosure vulnerability.

The potential SQL injection vulnerability was not assigned a definitive CVSS score because its full impact was not established.

Hardening recommendations and unverified security weaknesses were not assigned definitive CVSS scores.

Dependency vulnerabilities should be assessed individually using their corresponding security advisories.

CVSS measures technical severity and does not independently determine overall business risk.