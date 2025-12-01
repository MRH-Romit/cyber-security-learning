import csv
import os

def generate_ssh_report(input_file: str, output_file: str):
    print(f"Reading {input_file}...")

    attacks_found = []

    # 1. READ the firewall logs
    try:
        with open(input_file, 'r', newline='') as f_in:
            reader = csv.DictReader(f_in)

            for row in reader:
                if not row:
                    continue
                # Logic: If port is 22 AND action is BLOCK
                if row.get('dst_port') == '22' and row.get('action') == 'BLOCK':
                    attacks_found.append({
                        'time': row.get('time', ''),
                        'src_ip': row.get('src_ip', ''),
                        'dst_port': row.get('dst_port', ''),
                        'action': row.get('action', ''),
                    })
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        return

    # 2. WRITE the report (Only if we found attacks)
    if attacks_found:
        print(f"Found {len(attacks_found)} SSH attacks. Saving report...")

        with open(output_file, 'w', newline='') as f_out:
            headers = ['time', 'src_ip', 'dst_port', 'action']
            writer = csv.DictWriter(f_out, fieldnames=headers)
            writer.writeheader()
            writer.writerows(attacks_found)

        print(f"✅ Report saved to {output_file}")
    else:
        print("No SSH attacks found.")


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, 'firewall.csv')
    output_path = os.path.join(base_dir, 'ssh_report.csv')
    generate_ssh_report(input_path, output_path)