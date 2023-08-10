import re

# Read data from the input file
with open('input.txt', 'r') as file:
    data = file.read()

# Find all occurrences of <policy_member> sections
policy_members = re.findall(r'<policy_member>(.*?)<\/policy_member>', data, re.DOTALL)

# Loop through each <policy_member> section and extract <sender> and <receiver> tags
for policy_member in policy_members:
    senders = re.findall(r'<sender>(.*?)<\/sender>', policy_member)
    receivers = re.findall(r'<receiver>(.*?)<\/receiver>', policy_member)
    
    print("Sender(s):", senders)
    print("Receiver(s):", receivers)
    print("-" * 30)
