import csv
import json

def find_admins(csv_file):
    """
    Reads a CSV and finds all users with 'admin' in their role.
    """
    admins = []

    try:
        with open(csv_file, mode='r') as file:
            # key step: DictReader treats the first row as headers
            csv_reader = csv.DictReader(file)
            
            print(f"--- Scanning {csv_file} ---")
            
            for row in csv_reader:
                # Check if 'admin' is inside the 'role' column
                if "admin" in row['role']:
                    print(f"🚨 High Privilege User Found: {row['username']}")
                    admins.append(row) # Add the whole row to our list

    except FileNotFoundError:
        print("Error: users.csv not found!")
        return []

    return admins

# --- Main Execution ---
admin_list = find_admins("users.csv")

if admin_list:
    # Save the sensitive accounts to a new JSON file for the security team
    with open("high_risk_users.json", "w") as json_file:
        json.dump(admin_list, json_file, indent=4)
        print(f"\n✅ Exported {len(admin_list)} admin accounts to 'high_risk_users.json'")