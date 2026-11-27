# Executive Summary

## Assessment Overview

A security assessment was conducted against a locally hosted instance of OWASP Juice Shop to evaluate application security weaknesses, authentication practices, HTTP security controls and software dependency risks.

The assessment combined manual security testing, Python based automation, secure coding demonstrations and software composition analysis.

## Key Findings

The assessment identified verbose database error disclosure and strong evidence of unsafe SQL query construction within the application's product search functionality.

The confirmed information disclosure vulnerability received a provisional CVSS v3.1 score of 5.3 (Medium).

Additional security observations included missing security headers, a permissive CORS configuration and authentication token storage within browser local storage.

Software composition analysis identified 20 reported vulnerability entries across 11 unique advisory identifiers affecting two Python automation dependencies.

## Remediation and Verification

A standalone secure coding implementation demonstrated parameterised SQL queries, secure exception handling and internal error logging.

All six automated remediation tests passed successfully.

The vulnerable Python dependency configuration was updated, resulting in a 100% reduction in reported vulnerability entries during the subsequent scan. Regression testing confirmed that the existing security automation functionality remained operational.

## Recommendations

- Implement parameterised database queries within the application.
- Prevent internal database errors from being disclosed to users.
- Strengthen HTTP security headers and review CORS configuration.
- Review authentication token storage and server side session invalidation.
- Integrate dependency vulnerability scanning into CI/CD pipelines.
- Conduct regular security assessments and regression testing.

## Residual Risk

The original Juice Shop application was not modified. Application level remediation was demonstrated separately and full SQL injection exploitability was not established.

Further investigation is required to determine the practical impact of the identified authentication and browser security weaknesses.

## Conclusion

The assessment demonstrated an end-to-end security engineering workflow encompassing vulnerability identification, risk classification, remediation demonstrations, automated testing, dependency management and technical reporting.