import re
import time

# Define the log file to monitor
LOG_FILE = "auth.log"  # Change this to the actual path of your system log file (e.g., /var/log/auth.log)

# Define patterns to detect attacks
FAILED_LOGIN_PATTERN = r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"
SQL_INJECTION_PATTERN = r"(?:\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b).*?(?:\bFROM\b|\bWHERE\b)"

def detect_intrusions():
    """ Monitors the log file for intrusion attempts. """
    print(f"Monitoring {LOG_FILE} for suspicious activity...\n")
    
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
    
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new logs
                continue
            
            # Check for failed login attempts
            failed_login = re.search(FAILED_LOGIN_PATTERN, line)
            if failed_login:
                username, ip = failed_login.groups()
                print(f"🚨 ALERT: Failed login attempt detected! Username: {username}, IP: {ip}")
            
            # Check for SQL injection attempts
            if re.search(SQL_INJECTION_PATTERN, line, re.IGNORECASE):
                print(f"🚨 ALERT: Possible SQL Injection detected! Log entry: {line.strip()}")

# Run the IDS
if __name__ == "__main__":
    detect_intrusions()
