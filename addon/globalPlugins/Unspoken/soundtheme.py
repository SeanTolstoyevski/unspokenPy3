import os
from .camlorn_audio import *
import controlTypes

UNSPOKEN_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
UNSPOKEN_SOUNDS_PATH = os.path.join(UNSPOKEN_ROOT_PATH, "sounds")

sound_files = {
	controlTypes.ROLE_CHECKBOX: "checkbox.wav",
	controlTypes.ROLE_RADIOBUTTON: "radiobutton.wav",
	controlTypes.ROLE_STATICTEXT: "editabletext.wav",
	controlTypes.ROLE_EDITABLETEXT: "editabletext.wav",
	controlTypes.ROLE_BUTTON: "button.wav",
	controlTypes.ROLE_MENUBAR: "menuitem.wav",
	controlTypes.ROLE_MENUITEM: "menuitem.wav",
	controlTypes.ROLE_MENU: "menuitem.wav",
	controlTypes.ROLE_COMBOBOX: "combobox.wav",
	controlTypes.ROLE_LISTITEM: "listitem.wav",
	controlTypes.ROLE_GRAPHIC: "icon.wav",
	controlTypes.ROLE_LINK: "link.wav",
	controlTypes.ROLE_TREEVIEWITEM: "treeviewitem.wav",
	controlTypes.ROLE_TAB: "tab.wav",
	controlTypes.ROLE_TABCONTROL: "tab.wav",
	controlTypes.ROLE_SLIDER: "slider.wav",
	controlTypes.ROLE_DROPDOWNBUTTON: "combobox.wav",
	controlTypes.ROLE_CLOCK: "clock.wav",
	controlTypes.ROLE_ANIMATION: "icon.wav",
	controlTypes.ROLE_ICON: "icon.wav",
	controlTypes.ROLE_IMAGEMAP: "icon.wav",
	controlTypes.ROLE_RADIOMENUITEM: "radiobutton.wav",
	controlTypes.ROLE_RICHEDIT: "editabletext.wav",
	controlTypes.ROLE_SHAPE: "icon.wav",
	controlTypes.ROLE_TEAROFFMENU: "menuitem.wav",
	controlTypes.ROLE_TOGGLEBUTTON: "checkbox.wav",
	controlTypes.ROLE_CHART: "icon.wav",
	controlTypes.ROLE_DIAGRAM: "icon.wav",
	controlTypes.ROLE_DIAL: "slider.wav",
	controlTypes.ROLE_DROPLIST: "combobox.wav",
	controlTypes.ROLE_MENUBUTTON: "button.wav",
	controlTypes.ROLE_DROPDOWNBUTTONGRID: "button.wav",
	controlTypes.ROLE_HOTKEYFIELD: "editabletext.wav",
	controlTypes.ROLE_INDICATOR: "icon.wav",
	controlTypes.ROLE_SPINBUTTON: "slider.wav",
	controlTypes.ROLE_TREEVIEWBUTTON: "button.wav",
	controlTypes.ROLE_DESKTOPICON: "icon.wav",
	controlTypes.ROLE_PASSWORDEDIT: "editabletext.wav",
	controlTypes.ROLE_CHECKMENUITEM: "checkbox.wav",
	controlTypes.ROLE_SPLITBUTTON: "splitbutton.wav",
}

sounds = dict()


def loadSoundTheme(soundTheme):
	for key in sound_files:
		sounds[key] = Sound3D(os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme,  sound_files[key]))
		sounds[key].set_rolloff_factor(0)


def getAvailableSoundThemes():
	soundThemes = []
	dirs = os.listdir(UNSPOKEN_SOUNDS_PATH)
	for d in dirs:
		if os.path.isdir(os.path.join(UNSPOKEN_SOUNDS_PATH, d)):
			soundThemes.append(d)
	return soundThemes
