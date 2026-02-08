import os
import yaml
from GUI import elements as gui
from GUI import actions as act

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
    objectManager.addGUI(gui.settingsElement(objectManager))
    objectManager.addGUI(gui.presetOptionsElement(presetButtons, objectManager))

def loadSettingsGUI(objectManager) -> None:
    mainFrame = gui.settingsFrame()
    closeButton = gui.closeElement()
    stopSimulationButton = gui.stopSimulationElement()

    closeButton.update(650, 0, 50, 50)
    closeButton.setFunc(lambda: act.closeAction(closeButton.parent, objectManager))

    mainFrame.addChild(closeButton)
    mainFrame.addChild(stopSimulationButton)

    objectManager.addGUI(mainFrame)