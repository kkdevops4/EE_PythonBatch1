# Step 1: Sample trip data
trips = [
    {"trip_id": 1, "driver": "A", "distance": 120, "fuel": 10},
    {"trip_id": 2, "driver": "B", "distance": 150, "fuel": 12},
    {"trip_id": 3, "driver": "A", "distance": 200, "fuel": 20},
    {"trip_id": 4, "driver": "C", "distance": 80, "fuel": 6},
    {"trip_id": 5, "driver": "B", "distance": 300, "fuel": 25}
]

# Step 2: Generator (stream trips one by one)
def trip_stream(data):
    for t in data:
        yield t

# Step 3: Calculate efficiency (km per liter)
processed = [
    {**t, "efficiency": t["distance"] / t["fuel"]}
    for t in trip_stream(trips)
]

# Step 4: Sort trips by efficiency (highest first)
ranked_trips = sorted(processed, key=lambda x: x["efficiency"], reverse=True)

# Step 5: Group trips into efficiency bands
groups = {"Low": [], "Medium": [], "High": []}

for t in processed:
    eff = t["efficiency"]
    
    if eff < 10:
        groups["Low"].append(t)
    elif eff <= 15:
        groups["Medium"].append(t)
    else:
        groups["High"].append(t)

# Step 6: Driver average efficiency
driver_data = {}

for t in processed:
    driver = t["driver"]
    if driver not in driver_data:
        driver_data[driver] = []
    driver_data[driver].append(t["efficiency"])

# Calculate average
driver_avg = {
    d: sum(vals) / len(vals)
    for d, vals in driver_data.items()
}

# Sort drivers
ranked_drivers = sorted(driver_avg.items(), key=lambda x: x[1], reverse=True)

# ---------------- OUTPUT ----------------

print("=== Ranked Trips ===")
for t in ranked_trips:
    print(t)

print("\n=== Efficiency Groups ===")
for k, v in groups.items():
    print(k, ":", len(v), "trips")

print("\n=== Driver Ranking ===")
for d, eff in ranked_drivers:
    print(d, "->", round(eff, 2), "km/l")