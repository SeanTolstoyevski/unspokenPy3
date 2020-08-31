import os
import gui
import wx
from .soundtheme import *
from logHandler import log


class UnspokenSettingsPanel(gui.SettingsPanel):
    title = _(' unspoken  setting')

    def makeSettings(self, settingsSizer):
        soundThemes = getAvailableSoundThemes()
        self.soundSelectorLbl = wx.StaticText(self, wx.ID_ANY, "sound theme")
        self.SoundSelector = wx.Choice(self, wx.ID_ANY, choices=soundThemes)
        self.SoundSelector.SetSelection(0)

    def onSave(self):
        log.info("ok is pressed")
