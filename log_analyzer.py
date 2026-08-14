# Cybersecurity Log Monitor
# First version: detect failed login attempts

logs = [
    "SUCCESS: user abdulrahim logged in",
    "FAILED: user unknown login attempt",
    "FAILED: user unknown login attempt",
    "SUCCESS: user admin logged in",
    "FAILED: user unknown login attempt"
]

failed_attempts = 0

for log in logs:
    if "FAILED" in log:
        failed_attempts += 1

print("Total failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("ALERT: Possible brute-force attack detected!")
else:
    print("No suspicious activity detected.")
