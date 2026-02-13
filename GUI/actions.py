from GUI import frames

def settingsAction(objectManager) -> None:
    alreadyLoaded = False
    for guiObject in objectManager.GUI_ELEMENTS:
        if guiObject.id == "SettingsFrame":
            alreadyLoaded = True

    if not alreadyLoaded:
        frames.loadSettingsGUI(objectManager)

def presetAction(fileName, objectManager) -> None:
    print("LOADING SET: " + fileName)
    objectManager.loadSets(fileName)

def closeAction(parent, objectManager) -> None:
    objectManager.removeGUI(parent)

def stopSimulationAction(app) -> None:
    app.runningSimulation = False

def closeGameAction(app) -> None:
    print("Closing Game")
    app.runningApp = False