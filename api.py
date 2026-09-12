from fastapi import FastAPI
from shuttle import validate_event
from shuttle import get_occupancy

app = FastAPI(title="aitu campus shuttle api")

@app.get("/")
def home():
    return {
        "message": "shuttle api is running"
    }

@app.post("/events")
def receive_event(event: dict):
    check = validate_event(event)

    if not check["valid"]:
        return {
            "accepted": False,
            "rejected": True,
            "validation_errors": check["errors"],
            "occupancy_category": None
        }

    valid_event = check["event"]

    return {
        "accepted": True,
        "rejected": False,
        "validation_errors": [],
        "occupancy_category": get_occupancy(
            valid_event["passengers"]
        )
    }