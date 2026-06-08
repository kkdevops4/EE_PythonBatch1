from config.firebase_config import db
from dashboard.dashboard import run_dashboard

data = {
    "vehicle": "BMWM4",
    "speed": 60,
    "latitude": 28.61,
    "longitude": 77.20
}

db.collection("telemetry").add(data)

print("Data sent to Firebase")