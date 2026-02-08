import yaml

def loadBallSet(fileName) -> dict:
    with open(fileName, "r") as read_file:
        loadedFile = yaml.safe_load(read_file)

    loadedSet = {
        "mass": loadedFile['ball']['mass'],
        "moment": loadedFile['ball']['moment'],
        "friction": loadedFile['ball']['friction'],
        "elasticity": loadedFile['ball']['elasticity'],
        "radius": loadedFile['ball']['radius'],
        "width": loadedFile['ball']['width'],
        "position": loadedFile['ball']['position'],
        "color": loadedFile['ball']['color'],
        "amount": loadedFile['ball']['amount']
    }

    return loadedSet

def loadArcSet(fileName) -> dict:
    with open(fileName, "r") as read_file:
        loadedFile = yaml.safe_load(read_file)
    
    loadedSet = {
        "friction": loadedFile['arc']['friction'],
        "elasticity": loadedFile['arc']['elasticity'],
        "radius": loadedFile['arc']['radius'],
        "width": loadedFile['arc']['width'],
        "position": loadedFile['arc']['position'],
        "color": loadedFile['arc']['color'],
        "amount": loadedFile['arc']['amount'],
        "segments": loadedFile['arc']['segments'],
        "rotation_speed": loadedFile['arc']['rotation_speed'],
        "start_angle": loadedFile['arc']['start_angle'],
        "end_angle": loadedFile['arc']['end_angle'],
        "offset": loadedFile['arc']['offset']
    }

    return loadedSet

