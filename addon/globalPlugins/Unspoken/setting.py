import os 
import gui 
import wx 

UNSPOKEN_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
UNSPOKEN_SOUNDS_PATH = os.path.join(UNSPOKEN_ROOT_PATH, "sounds")

def getAvailableSoundThemes():
    soundThemes = []
    dirs = os.listdir(UNSPOKEN_SOUNDS_PATH)
    for d in dirs:
        if os.path.isdir(os.path.join(UNSPOKEN_SOUNDS_PATH, d))
        soundThemes.append(d)
    return soundThemes


class UnspokenSettingsPanel(gui.SettingsPanel):
    title = _(' unspoken  setting')

    def makeSettings(self, settingsSizer):
        self.soundSelectorLbl = wx.StaticText(self, wx.ID_ANY, "sound theme")
        self.SoundSelector = wx.Choice(self, wx.ID_ANY, choices=["default theme", "forest", "rain"])
        self.SoundSelector.SetSelection(0)

    def onSave(self):
        pass
