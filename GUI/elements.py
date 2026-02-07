from GUI import pygameGUI as pGUI
from Core import constants as const
from GUI import actions as act

def settingsElement() -> pGUI.button:
    return pGUI.button(left=10, top=700, width=0, height=0, backgroundColor=(192,192,192),autoSize=True, label="Settings", paddingX=10, paddingY=10, func=act.settingsAction)

def presetOptionsElement(menu, manager) -> pGUI.dropDownMenu:
    return pGUI.dropDownMenu(left=10, top=10, width=150, height=25, backgroundColor=(192,192,192), label="Presets", autoSize=True, paddingX=10, paddingY=10, func=act.presetAction, menu=menu, manager=manager)

def versionElement() -> pGUI.labelFrame:
    return pGUI.labelFrame(left=const.SCREENSIZE[0]-pGUI.getFontSize(20, const.VERSION)[0] - 10, top=const.SCREENSIZE[1]-pGUI.getFontSize(20, const.VERSION)[1] - 10, width=0, height=0, autoSize=True, textSize=20, label=const.VERSION, paddingX=10, paddingY=10)

def presetElement(name, fileName, manager) -> pGUI.button:
    return  pGUI.button(left=10, top=10, width=150, height=25, backgroundColor=(192,192,192), label=name, autoSize=True, paddingX=10, paddingY=10, func=lambda: act.presetAction(fileName, manager))