# Security Finding 001 — Database Information Disclosure

## Target
OWASP Juice Shop — Local Docker Environment

## Affected Endpoint
GET /rest/products/search

## Vulnerability Classification
CWE-209 — Generation of Error Message Containing Sensitive Information

## Status
Confirmed

## Description
The product search endpoint returns detailed database error messages when processing certain user inputs containing apostrophes.

## Evidence
- Test ID: TC-008
- HTTP status: 500 Internal Server Error
- Database technology: SQLite
- Internal SQL query exposed: Yes
- Screenshot: evidence/TC-008-apostrophe-handling.png

## Potential Impact
An attacker could obtain information about the application's database structure and backend implementation, supporting further vulnerability investigation.

## Recommended Remediation
- Implement parameterised SQL queries.
- Implement centralised exception handling.
- Return generic error messages to users.
- Restrict detailed database errors to internal application logs.

## Further Investigation
Potential SQL injection (CWE-89) due to apparent unsafe handling of user-controlled input. Full exploitability has not yet been established.

## Reproducibility

- Original test: TC-008
- Reproduction test: TC-009
- Result: Successfully reproduced
- HTTP status: 500 Internal Server Error
- Response body size: 313 bytes
- Evidence: evidence/TC-009-vulnerability-reproduction.png

The application consistently exposes internal SQL
queries and database error information when
processing the tested input.

## Additional Vulnerability Investigation

- TC-010: Removing the apostrophe returned HTTP 200.
- TC-011: A different input containing an apostrophe
  reproduced the database error.
- TC-012: Using two consecutive apostrophes returned
  HTTP 200 without a database error.

## Technical Analysis

The results indicate that user-controlled input is
being incorporated into SQL queries without adequate
parameterisation.

The application also exposes internal database
information through verbose error responses.

## Associated Vulnerability Classifications

- CWE-209: Sensitive Information in Error Messages
  (Confirmed)
- CWE-89: SQL Injection
  (Strong evidence; full impact not yet validated)