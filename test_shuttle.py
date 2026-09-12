from shuttle import validate_event
from shuttle import get_occupancy
from shuttle import event_stream

def test_valid_event():
    event = {
        "timestamp": "08:00",
        "route": "aitu-campus-residence",
        "bus": "b29",
        "passengers": 18,
        "speed_kmh": 0,
        "status": "stopped"
    }

    result = validate_event(event)
    assert result["valid"] is True
    assert result["errors"] == []

def test_negative_passengers():
    event = {
        "timestamp": "08:59",
        "route": "aitu-campus-residence",
        "bus": "b31",
        "passengers": -57,
        "speed_kmh": 31,
        "status": "on_route"
    }

    result = validate_event(event)
    assert result["valid"] is False
    assert "passengers cannot be negative" in result["errors"]

def test_invalid_speed():
    event = {
        "timestamp": "08:30",
        "route": "aitu-campus-residence",
        "bus": "b17",
        "passengers": 18,
        "speed_kmh": 150,
        "status": "on_route"
    }

    result = validate_event(event)
    assert result["valid"] is False
    assert "speed must be between 0 and 120" in result["errors"]

def test_invalid_status():
    event = {
        "timestamp": "08:23",
        "route": "aitu-campus-residence",
        "bus": "b70",
        "passengers": 14,
        "speed_kmh": 60,
        "status": "moving"
    }

    result = validate_event(event)
    assert result["valid"] is False
    assert "status must be on_route or stopped" in result["errors"]

def test_high_occupancy():
    assert get_occupancy(30) == "high"

def test_over_capacity():
    assert get_occupancy(45) == "over_capacity"

