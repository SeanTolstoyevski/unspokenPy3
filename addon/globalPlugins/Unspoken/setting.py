import os
import config
import gui
import wx
from .soundtheme import *
from logHandler import log
from zipfile import ZipFile


class UnspokenSettingsPanel(gui.SettingsPanel):
	title = _(' unspoken  setting')

	def makeSettings(self, settingsSizer):
		curSoundTheme = config.conf.spec["unspokenpy3"]["soundtheme"]
		self.soundThemes = getAvailableSoundThemes()
		self.soundSelectorLbl = wx.StaticText(self, wx.ID_ANY, "sound theme")
		self.soundThemeSelector = wx.Choice(self, wx.ID_ANY, choices=self.soundThemes)
		self.soundThemeSelector.SetSelection(self.soundThemes.index(curSoundTheme))
		self.importBtn = wx.Button(self, wx.ID_ANY, "import sound theme")
		self.Bind(wx.EVT_BUTTON, self.onImportTheme,  self.importBtn)

	def onSave(self):
		selSoundThemeIndex = self.soundThemeSelector.GetCurrentSelection()
		selSoundTheme = self.soundThemes[selSoundThemeIndex]
		config.conf.spec["unspokenpy3"]["soundtheme"] = selSoundTheme
		log.info("sound theme: " + config.conf.spec["unspokenpy3"]["soundtheme"])
		loadSoundTheme(selSoundTheme)

	def onImportTheme(self, evt):
		log.info("import button pressed")
		wildcard = "zip file containing sound theme(*.zip) |*.zip|"
		dlg = wx.FileDialog(self, wildcard=wildcard, style=wx.FD_CHANGE_DIR |
							wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, defaultDir=os.getcwd())
		if dlg.ShowModal() == wx.ID_OK:
			importSoundThemePath = dlg.GetPath()
		log.info("importing theme" + importSoundThemePath)
		dlg.Destroy()
		self.importTheme(importSoundThemePath)
		self.soundThemes = getAvailableSoundThemes()
		self.soundThemeSelector.Set(self.soundThemes)

	def importTheme(self, path):
		soundThemeFile = ZipFile(path)
		os.chdir(UNSPOKEN_SOUNDS_PATH)
		soundThemeFile.extractall()
