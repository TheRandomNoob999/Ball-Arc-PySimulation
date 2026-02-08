from Core import app
from GUI import pygameGUI as pGUI
from Core import constants as const
from GUI import actions as act

# region Standard GUI
def settingsElement(manager) -> pGUI.button:
    settingsButton = pGUI.button(left=10, top=700, width=0, height=0) #Width and Height get set through autoSize
    settingsButton.autoSize = True
    settingsButton.backgroundColor = const.WHITE
    settingsButton.label = "Settings"
    settingsButton.changePadding(x=10, y=10)
    settingsButton.setFunc(lambda: act.settingsAction(manager))

    return settingsButton

def presetOptionsElement(menu, manager) -> pGUI.dropDownMenu:
    presetDropDown = pGUI.dropDownMenu(left=10, top=10, width=0, height=0) #Width and Height get set through autoSize
    presetDropDown.autoSize = True
    presetDropDown.backgroundColor = const.WHITE
    presetDropDown.label = "Presets"
    presetDropDown.changePadding(x=10, y=10)
    presetDropDown.objectManager = manager
    presetDropDown.menuOptions = menu

    return presetDropDown

def versionElement() -> pGUI.labelFrame:
    versionLabel = pGUI.labelFrame(left=const.SCREENSIZE[0]-pGUI.getFontSize(20, const.VERSION)[0] -10, top=const.SCREENSIZE[1]-pGUI.getFontSize(20, const.VERSION)[1] - 10, width=0, height=0) #Height and Width gets set with autoSize
    versionLabel.autoSize = True
    versionLabel.backgroundColor = const.WHITE
    versionLabel.label = const.VERSION
    versionLabel.textSize = 20
    versionLabel.changePadding(x=10, y=10)

    return versionLabel

def presetElement(name, fileName, manager, textSize) -> pGUI.button:
    presetButton = pGUI.button(left=10, top=10, width=150, height=25) #Width and Height gets set based on DropDownMenu
    presetButton.changePadding(x=10, y=10)
    presetButton.label = name
    presetButton.setFunc(lambda: act.presetAction(fileName, manager))
    presetButton.backgroundColor = const.WHITE
    presetButton.textSize = textSize

    return presetButton


def closeElement() -> pGUI.button:
    closeButton = pGUI.button(left=0, top=0, width=50, height=50) #Left and Top get set based on the parent object
    closeButton.backgroundColor = const.RED
    # Close function gets added on in frames.py
    return closeButton

# endregion

# region Settings
def settingsFrame() -> pGUI.Frame:
    settingsMainFrame = pGUI.Frame(left=50, top=50, width=700, height=700)
    settingsMainFrame.backgroundColor = const.GREY

    return settingsMainFrame

def stopSimulationElement() -> pGUI.button:
    stopSimulationButton = pGUI.button(left=0, top=0, width=250, height=100)
    stopSimulationButton.backgroundColor = const.RED
    stopSimulationButton.autoSize = True
    stopSimulationButton.label = "Stop Simulation"
    stopSimulationButton.textSize = 30
    stopSimulationButton.changePadding(x=10, y=10)
    stopSimulationButton.setFunc(lambda: act.stopSimulationAction(app))

    return stopSimulationButton

# endregion