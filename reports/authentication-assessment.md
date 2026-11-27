# Authentication and Session Security Assessment

## Objective

Assess the authentication process, token storage
and logout behaviour of OWASP Juice Shop.

## Testing Methodology

- HTTP traffic inspection using Burp Suite
- Browser storage inspection using Developer Tools
- Manual login and logout testing
- Dedicated fictional test account

## Findings

### Authentication Mechanism

The application accepts login credentials through
POST /rest/user/login and returns an authentication
token following successful authentication.

### Authentication Token Storage

The application stores an authentication token
in browser local storage.

This exposes the token to same-origin JavaScript
and could increase the impact of an XSS vulnerability.

Classification: Potential security weakness.

### Logout Behaviour

The authentication token was removed from local
storage following logout.

Result: PASS - Client-side session cleanup.

## Recommendations

- Consider HttpOnly, Secure and SameSite cookies
  with appropriate CSRF protection.
- Enforce HTTPS in production environments.
- Implement appropriate token expiry and
  server-side invalidation mechanisms.

## Evidence

- TC-026-authentication-request-response.png
- TC-027-authentication-token-storage.png
- TC-028-logout-token-removal.png

## Limitations

Server-side token invalidation, token expiry,
signature validation and XSS exploitability
were not verified during this assessment.