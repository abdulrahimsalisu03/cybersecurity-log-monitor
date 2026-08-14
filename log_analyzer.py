# Cybersecurity Log Monitor
# Analyzes system logs and detects suspicious login activity

failed_attempts = 0

with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    if "FAILED" in log:
        failed_attempts += 1

print("Total failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("ALERT: Possible brute-force attack detected!")
else:
    print("No suspicious activity detected.")
