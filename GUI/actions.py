def settingsAction() -> None:
    print("This is the settings button")

def presetAction(fileName, objectManager) -> None:
    print("LOADING SET: " + fileName)
    objectManager.loadSets(fileName)