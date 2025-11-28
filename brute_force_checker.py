
logs = [
    "Login failed from 192.168.1.5",
    "Login success from 192.168.1.10",
    "Login failed from 192.168.1.5",
    "Login failed from 192.168.1.5", 
    "Login failed from 192.168.1.5", 
]

failed_counts = {} 
THRESHOLD = 3

print("--- Starting Intrusion Detection ---")

for line in logs:
    if "failed" in line:
 
        ip = line.split(" ")[-1]
        
      
        failed_counts[ip] = failed_counts.get(ip, 0) + 1

        
        if failed_counts[ip] > THRESHOLD:
            print(f"🚨 BRUTE FORCE ALERT: IP {ip} has failed {failed_counts[ip]} times!")

print("--- Scan Complete ---")