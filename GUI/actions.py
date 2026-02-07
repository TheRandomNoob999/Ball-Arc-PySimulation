def settingsAction() -> None:
    print("This is the settings button")

def presetAction(name, objectManager) -> None:
    fileName = "Presets\\" + name + ".yaml"
    print("LOADING SET: " + fileName)
    objectManager.loadSets(fileName)