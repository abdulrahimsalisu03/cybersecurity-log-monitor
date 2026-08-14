# Cybersecurity Log Monitor
# Analyzes security logs and detects suspicious login activity.

LOG_FILE = "sample_logs.txt"

failed_attempts = 0
successful_logins = 0

print("=== Cybersecurity Log Monitor ===")
print()

try:
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    for log in logs:
        log = log.strip()

        if "SUCCESS" in log:
            successful_logins += 1

        elif "FAILED" in log:
            failed_attempts += 1

    print("Total successful logins:", successful_logins)
    print("Total failed login attempts:", failed_attempts)
    print()

    if failed_attempts >= 3:
        print("ALERT: Suspicious login activity detected!")
        print("Possible brute-force attack.")
    else:
        print("No suspicious activity detected.")

except FileNotFoundError:
    print("ERROR: sample_logs.txt was not found.")
