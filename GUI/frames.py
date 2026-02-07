import os
from Core import objects as obj
from GUI import elements as gui

def loadStandardGUI(objectManager) -> None:
    presetButtons = []
    for file in os.listdir(os.fsencode("Presets")):
        filename = os.fsdecode(file)
        if filename.endswith(".yaml"):
            newButton = gui.presetElement(filename.split('.')[0].capitalize(), objectManager)
            presetButtons.append(newButton)


    objectManager.addGUI(gui.versionElement())
    objectManager.addGUI(gui.settingsElement())
    objectManager.addGUI(gui.presetOptionsElement(presetButtons, objectManager))