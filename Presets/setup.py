import json

def loadBallSet() -> dict:
    with open("Presets\default.json", mode="r", encoding="utf-8") as read_file:
        loadedFile = json.load(read_file)
    
    x = loadedFile["ball"][0]
    pos = (x["positionx"], x["positiony"])
    color = (x["red"], x["green"], x["blue"])

    loadedSet = {
        "mass": x["mass"],
        "moment": x["moment"],
        "friction": x["friction"],
        "elasticity": x["elasticity"],
        "radius": x["radius"],
        "width": x["width"],
        "position": pos,
        "color": color,
        "amount": x["amount"]
    }

    return loadedSet

def loadArcSet() -> dict:
    with open("Presets\default.json", mode="r", encoding="utf-8") as read_file:
        loadedFile = json.load(read_file)
    
    x = loadedFile["arc"][0]
    pos = (x["positionx"], x["positiony"])
    color = (x["red"], x["green"], x["blue"])

    loadedSet = {
        "friction": x["friction"],
        "elasticity": x["elasticity"],
        "radius": x["radius"],
        "width": x["width"],
        "position": pos,
        "color": color,
        "amount": x["amount"],
        "segments": x["segments"],
        "rotation_speed": x["rotation_speed"],
        "start_angle": x["start_angle"],
        "end_angle": x["end_angle"]
    }

    return loadedSet