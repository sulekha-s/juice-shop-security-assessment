import requests
import json
from pathlib import Path

BASE_URL = "http://localhost:3000"
RESULTS_FILE = Path(__file__).resolve().parent / "test_results.json"

try:
    response = requests.get(BASE_URL, timeout=10)
except requests.exceptions.RequestException:
    print("Unable to connect to the target application.")
    raise SystemExit(1)

print("HTTP status:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))

if response.status_code == 200:
    print("PASS: Application is reachable")
else:
    print("FAIL: Unexpected HTTP status code")

if "text/html" in response.headers.get("Content-Type", ""):
    print("PASS: Expected content type received")
else:
    print("FAIL: Unexpected content type")

results = {
    "target": BASE_URL,
    "status_code": response.status_code,
    "content_type": response.headers.get("Content-Type"),
    "availability_check": response.status_code == 200,
    "content_type_check": "text/html" in response.headers.get("Content-Type", "")
}
security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]
header_results = {}

print("\nSecurity header assessment:")

for header in security_headers:
    value = response.headers.get(header)

    header_results[header] = {
        "present": value is not None,
        "value": value
    }

    if value is not None:
        print(f"PRESENT: {header}")
    else:
        print(f"MISSING: {header}")

results["security_headers"] = header_results

cors_headers = [
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Credentials",
    "Access-Control-Allow-Methods",
    "Access-Control-Allow-Headers"
]

cors_results = {}

print("\nCORS assessment:")

for header in cors_headers:
    value = response.headers.get(header)
    cors_results[header] = value
    print(f"{header}: {value}")

results["cors_headers"] = cors_results

with open(RESULTS_FILE, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print("Test results saved successfully")