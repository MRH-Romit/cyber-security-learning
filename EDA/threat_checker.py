import csv
import os

def hunt_threats(log_file: str, threat_file: str):
    print("--- 🕵️‍♂️ Starting Threat Hunt ---")

    # 1) Load bad IPs with risk levels into a dict for O(1) lookups
    bad_ip_risk = {}
    try:
        with open(threat_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ip = (row.get('ip') or '').strip()
                risk = (row.get('risk_level') or '').strip()
                if ip:
                    bad_ip_risk[ip] = risk or 'Unknown'
    except FileNotFoundError:
        print(f"Error: Threat file not found: {threat_file}")
        return

    if not bad_ip_risk:
        print("No bad IPs loaded; nothing to match against.")
        return

    # 2) Scan server logs against the bad IP list
    total_rows = 0
    hits = 0
    try:
        with open(log_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_rows += 1
                visitor_ip = (row.get('src_ip') or '').strip()
                if not visitor_ip:
                    continue

                risk = bad_ip_risk.get(visitor_ip)
                if risk is not None:
                    hits += 1
                    print("🚨 ALARM: Known Threat Detected!")
                    print(f"   - Time: {row.get('timestamp', '')}")
                    print(f"   - User: {row.get('user', '')}")
                    print(f"   - IP: {visitor_ip}")
                    print(f"   - Risk: {risk}\n")
    except FileNotFoundError:
        print(f"Error: Log file not found: {log_file}")
        return

    print("--- Summary ---")
    print(f"Scanned rows: {total_rows}")
    print(f"Matches found: {hits}")


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    log_path = os.path.join(base_dir, "server_access.csv")
    threat_path = os.path.join(base_dir, "bad_ips.csv")
    hunt_threats(log_path, threat_path)
