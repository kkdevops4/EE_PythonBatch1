tyre_data = [
    ("Car1", 2.5),
    ("Car2", 1.2),
    ("Car3", 3.8),
    ("Car4", 0.9),
    ("Car5", 2.0)
]


def read_data(data):
    for item in data:
        yield item


wear_list = []

for vehicle, wear in read_data(tyre_data):
    wear_list.append((vehicle, wear))


sorted_wear = sorted(
    wear_list,
    key=lambda x: x[1],
    reverse=True
)


def get_severity(wear):
    if wear >= 3:
        return "High"
    elif wear >= 1.5:
        return "Medium"
    else:
        return "Low"


groups = {
    level: [vehicle for vehicle, wear in sorted_wear
            if get_severity(wear) == level]
    for level in ["High", "Medium", "Low"]
}


print("Sorted Tyre Wear Data:")
for vehicle, wear in sorted_wear:
    print(vehicle, "-", wear, "mm")

print("\nGrouped by Severity:")
for level, vehicles in groups.items():
    print(level, ":", vehicles)