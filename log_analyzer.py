import json # Importing library to handle JSON 

def parse_logs(file_path):
    """
    Reads a log file and counts event types.
    """
    # Initialize counters (Variables/Dictionaries) [cite: 242]
    stats = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "suspicious_ips": []
    }

    try:
        # Opening the file 
        with open(file_path, 'r') as file:
            print(f"--- Scanning {file_path} ---")
            
            # Loop through each line [cite: 242]
            for line in file:
                line = line.strip() # Clean whitespace
                
                # Check for keywords (Basic String Parsing)
                if "[ERROR]" in line:
                    stats["ERROR"] += 1
                    print(f"🚨 ALERT FOUND: {line}")
                elif "[WARNING]" in line:
                    stats["WARNING"] += 1
                elif "[INFO]" in line:
                    stats["INFO"] += 1
                
                # Simple Logic: Capture IPs involved in errors (String manipulation)
                if "from" in line and "[ERROR]" in line:
                    parts = line.split(" ") # Splits sentence into words
                    ip_address = parts[-1]  # Grabs the last word (the IP)
                    stats["suspicious_ips"].append(ip_address)

    except FileNotFoundError:
        print("Error: File not found. Make sure server.log exists!")
        return None

    return stats

# --- Main Execution ---
log_file = "server.log"
results = parse_logs(log_file)

if results:
    print("\n--- Final Report ---")
    print(json.dumps(results, indent=4)) # Pretty print JSON 
    
    # Bonus: Write report to a new file 
    with open("daily_report.json", "w") as f:
        json.dump(results, f, indent=4)
        print("Report saved to 'daily_report.json'")