import re


CATEGORY_MAP = {
    'P': 'Powertrain',
    'C': 'Chassis',
    'B': 'Body',
    'U': 'Network'
}


raw_data = input("Enter OBD-II data:\n")


pattern = r'\b[PCBU][0-9]{4}\b'
valid_codes = re.findall(pattern, raw_data.upper())


categorized = {
    'Powertrain': [],
    'Chassis': [],
    'Body': [],
    'Network': []
}

for code in valid_codes:
    category_letter = code[0]
    category_name = CATEGORY_MAP[category_letter]
    categorized[category_name].append(code)


print("\n== OBD-II REPORT ==\n")

print("Total Valid Codes:", len(valid_codes), "\n")

for category in categorized:
    codes = categorized[category]
    print(category, "(", len(codes), "):")
    
    for c in codes:
        print("  -", c)