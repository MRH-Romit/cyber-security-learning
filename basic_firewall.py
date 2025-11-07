import random

def generate_random_ip():
    """Generates a random IP in the 192.168.1.x range."""
    return f"192.168.1.{random.randint(1, 20)}"

def check_firewall_rules(ip, rules):
    """Checks if an IP is in the firewall rules."""

    action = rules.get(ip, "ALLOW")
    return action

def main():

    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    # Test 10 random IPs
    for _ in range(10):
        ip = generate_random_ip()
        action = check_firewall_rules(ip, firewall_rules)
        print(f"IP: {ip}, Action: {action}")

if __name__ == "__main__":
    main()