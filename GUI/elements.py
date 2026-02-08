from Core import app
from GUI import pygameGUI as pGUI
from Core import constants as const
from GUI import actions as act

# region Standard GUI
def settingsElement(manager) -> pGUI.button:
    return pGUI.button(left=10, top=700, width=0, height=0, backgroundColor=(255,255,255),autoSize=True, label="Settings", paddingX=10, paddingY=10, func=lambda: act.settingsAction(manager))

def presetOptionsElement(menu, manager) -> pGUI.dropDownMenu:
    return pGUI.dropDownMenu(left=10, top=10, width=150, height=25, backgroundColor=(255,255,255), label="Presets", autoSize=True, paddingX=10, paddingY=10, func=act.presetAction, menu=menu, manager=manager)

def versionElement() -> pGUI.labelFrame:
    return pGUI.labelFrame(left=const.SCREENSIZE[0]-pGUI.getFontSize(20, const.VERSION)[0] - 10, top=const.SCREENSIZE[1]-pGUI.getFontSize(20, const.VERSION)[1] - 10, width=0, height=0, autoSize=True, textSize=20, label=const.VERSION, paddingX=10, paddingY=10)

def presetElement(name, fileName, manager, textSize) -> pGUI.button:
    return pGUI.button(left=10, top=10, width=150, height=25, backgroundColor=(255,255,255), label=name, textSize=textSize,autoSize=False, paddingX=10, paddingY=10, func=lambda: act.presetAction(fileName, manager))

def closeElement() -> pGUI.button:
    return pGUI.button(left=0, top=0, width=50, height=50, backgroundColor=(255,0,0), autoSize=False)

# endregion

def settingsFrame() -> pGUI.Frame:
    return pGUI.Frame(left=50, top=50, width=700, height=700, backgroundColor=(200,200,200))

def stopSimulationElement() -> pGUI.button:
    return pGUI.button(left=0, top=0, width=250, height=100, backgroundColor=(255,0,0), autoSize=True, label="Stop Simulation", textSize=20, paddingX=10, paddingY=10, func=lambda: act.stopSimulationAction(app))