import yaml
from Core import constants as const

def loadBallSet(fileName) -> dict:
    with open(fileName, "r") as read_file:
        loadedFile = yaml.safe_load(read_file)

    ballPosition = loadedFile['ball']['position']
    if loadedFile['ball']['positionCentered']:
        ballPosition = (const.SCREENSIZE[0]/2, const.SCREENSIZE[1]/2)

    loadedSet = {
        "mass": loadedFile['ball']['mass'],
        "moment": loadedFile['ball']['moment'],
        "friction": loadedFile['ball']['friction'],
        "elasticity": loadedFile['ball']['elasticity'],
        "radius": loadedFile['ball']['radius'],
        "width": loadedFile['ball']['width'],
        "position": ballPosition,
        "color": loadedFile['ball']['color'],
        "amount": loadedFile['ball']['amount'],
    }

    return loadedSet

def loadArcSet(fileName) -> dict:
    with open(fileName, "r") as read_file:
        loadedFile = yaml.safe_load(read_file)
    
    arcCenter = loadedFile['arc']['position']
    if loadedFile['arc']['positionCentered']:
        arcCenter = (const.SCREENSIZE[0]/2, const.SCREENSIZE[1]/2)

    loadedSet = {
        "friction": loadedFile['arc']['friction'],
        "elasticity": loadedFile['arc']['elasticity'],
        "radius": loadedFile['arc']['radius'],
        "width": loadedFile['arc']['width'],
        "position": arcCenter,
        "color": loadedFile['arc']['color'],
        "amount": loadedFile['arc']['amount'],
        "segments": loadedFile['arc']['segments'],
        "rotation_speed": loadedFile['arc']['rotation_speed'],
        "start_angle": loadedFile['arc']['start_angle'],
        "end_angle": loadedFile['arc']['end_angle'],
        "offset": loadedFile['arc']['offset'],
    }

    return loadedSet

