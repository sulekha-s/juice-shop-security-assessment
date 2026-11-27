# Security Testing Automation

## Overview

This Python tool automates baseline HTTP response and security configuration checks against a locally hosted OWASP Juice Shop instance.

## Requirements

- Python 3.14 (tested with Python 3.14.6)
- Requests library
- Running OWASP Juice Shop instance

## Installation

From the main project directory, with the virtual environment activated:

    python -m pip install -r automation/requirements.txt

## Execution

    python automation/api_security_tests.py

## Current Checks

- Application availability
- HTTP status code validation
- Content type validation
- HTTP security header presence
- CORS response header inspection
- Structured JSON result generation
- Connection failure handling

## Error Handling

The script implements a 10-second HTTP request timeout.

If the target application is unavailable, the script displays a generic error message and terminates with an exit code of 1.

Connection failure handling was validated by deliberately stopping the target application.

## Output

Results are displayed in the terminal and saved to:

    automation/test_results.json

The output uses a structured, machine-readable JSON format.

The output file path is resolved relative to the script location using Python's pathlib module.

## Dependency Security

Python dependencies were assessed using pip-audit. Known vulnerable dependencies were updated and baseline HTTP functionality was successfully retested.

The baseline requirements file is retained for historical comparison only.

## Testing Scope

Testing is restricted to the local OWASP Juice Shop environment for educational security research.

## Limitations

- Security header checks establish presence rather than effectiveness.
- CORS observations do not establish exploitability.
- The script does not perform comprehensive vulnerability scanning.
- Passing baseline HTTP checks does not establish that the application is secure.
- A failed connection does not overwrite previously saved JSON results.