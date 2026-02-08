from GUI import frames

def settingsAction(objectManager) -> None:
    frames.loadSettingsGUI(objectManager)

def presetAction(fileName, objectManager) -> None:
    print("LOADING SET: " + fileName)
    objectManager.loadSets(fileName)

def closeAction(parent, objectManager) -> None:
    print("Closing")
    objectManager.removeGUI(parent)

def stopSimulationAction(app) -> None:
    app.runningSimulation = False