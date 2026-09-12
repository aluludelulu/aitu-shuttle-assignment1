from datetime import datetime

def parse_event(event):
    parsed_event = {
        "timestamp": datetime.strptime(str(event["timestamp"]), "%H:%M").time(),
        "route": str(event["route"]).strip(),
        "bus": str(event["bus"]).strip(),
        "passengers": int(event["passengers"]),
        "speed_kmh": int(event["speed_kmh"]),
        "status": str(event["status"]).strip().upper()
    }

    return parsed_event

def validate_event(event):
    try:
        parsed_event = parse_event(event)

    except KeyError as error:
        return {
            "valid": False,
            "event": None,
            "errors": [f"missing field: {error}"]
        }

    except ValueError as error:
        return {
            "valid": False,
            "event": None,
            "errors": [f"invalid value: {error}"]
        }

    except TypeError as error:
        return {
            "valid": False,
            "event": None,
            "errors": [f"invalid type: {error}"]
        }

    errors = []

    if parsed_event["passengers"] < 0:
        errors.append("passengers cannot be negative")

    if (
        parsed_event["speed_kmh"] < 0
        or parsed_event["speed_kmh"] > 120
    ):
        errors.append("speed must be between 0 and 120")

    if parsed_event["status"] not in ["ON_ROUTE", "STOPPED"]:
        errors.append("status must be ON_ROUTE or STOPPED")

    if parsed_event["route"] == "":
        errors.append("route cannot be empty")

    if parsed_event["bus"] == "":
        errors.append("bus cannot be empty")

    return {
        "valid": len(errors) == 0,
        "event": parsed_event,
        "errors": errors
    }

def event_stream(events):
    for event in events:
        yield event

def get_occupancy(passengers):
    if passengers <= 10:
        return "low"

    elif passengers <= 20:
        return "medium"

    elif passengers <= 30:
        return "high"

    else:
        return "over_capacity"