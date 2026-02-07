import os
import yaml
from Core import objects as obj
from GUI import elements as gui

def loadStandardGUI(objectManager) -> None:
    presetButtons = []
    for file in os.listdir(os.fsencode("Presets")):
        filename = "Presets\\" + os.fsdecode(file)
        if filename.endswith(".yaml"):
            with open(filename, "r") as read_file:
                loadedFile = yaml.safe_load(read_file)
            newButton = gui.presetElement(loadedFile["name"], filename, objectManager,loadedFile["fontSize"])
            presetButtons.append(newButton)


    objectManager.addGUI(gui.versionElement())
    objectManager.addGUI(gui.settingsElement())
    objectManager.addGUI(gui.presetOptionsElement(presetButtons, objectManager))