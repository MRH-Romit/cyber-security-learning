

echo "------------------------------"
echo "  System Health Report"
echo "------------------------------"


echo "Current User: $(whoami)"
echo ""

echo "System Uptime:"
uptime -p
echo ""

echo "Disk Space Usage:"
df -h | grep --color=never /dev/
echo ""


echo "Memory Usage:"
free -h
echo ""

echo "------------------------------"
echo "  Report Complete"
echo "------------------------------"