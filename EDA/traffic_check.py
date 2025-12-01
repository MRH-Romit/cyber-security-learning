import csv
from collections import Counter
import statistics
import os

def perform_eda(file_path: str):
    print(f"--- 📊 Starting EDA on {file_path} ---")

    ips = []
    bytes_list = []
    hours = []

    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row:  # skip empty rows
                    continue
                ips.append(row.get('ip', '').strip())
                try:
                    bytes_sent = int(row.get('bytes_sent', '0'))
                except ValueError:
                    bytes_sent = 0
                bytes_list.append(bytes_sent)
                hour_raw = row.get('time', '00:00')
                hour = hour_raw.split(":")[0]
                hours.append(hour)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not ips:
        print("No data rows found.")
        return

    # --- Analysis 1: Top Talkers (Volume) ---
    ip_counts = Counter(ips)
    most_active_ip, count = ip_counts.most_common(1)[0]
    print(f"\n1️⃣  Most Active Device: {most_active_ip} ({count} requests)")

    # --- Analysis 2: Data Stats (Outliers) ---
    if bytes_list:
        avg_bytes = statistics.mean(bytes_list)
        max_bytes = max(bytes_list)
        print(f"\n2️⃣  Data Transfer Stats:")
        print(f"   - Average size: {avg_bytes} bytes")
        print(f"   - Max size: {max_bytes} bytes")
        if max_bytes > (avg_bytes * 5):
            print("   ⚠️  ANOMALY DETECTED: Max size is huge compared to average!")
    else:
        print("\n2️⃣  Data Transfer Stats: No byte data available.")

    # --- Analysis 3: Time Distribution (Habits) ---
    print(f"\n3️⃣  Activity by Hour:")
    hour_counts = Counter(hours)
    for hour, h_count in sorted(hour_counts.items()):
        bar = "█" * h_count
        print(f"   {hour}:00 | {bar} ({h_count})")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "traffic.csv")
    perform_eda(csv_path)
