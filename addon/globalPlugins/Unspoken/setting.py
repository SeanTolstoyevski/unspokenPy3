import os
import config
import gui
import wx
from .soundtheme import *
from logHandler import log


class UnspokenSettingDialog(gui.SettingsDialog):
	title = _(' unspoken  setting')

	def makeSettings(self, settingsSizer):
		curSoundTheme = config.conf["unspokenpy3"]["soundtheme"]
		self.soundThemes = getAvailableSoundThemes()
		self.soundSelectorLbl = wx.StaticText(self, wx.ID_ANY, "sound theme")
		self.soundThemeSelector = wx.Choice(
			self, wx.ID_ANY, choices=self.soundThemes)
		self.soundThemeSelector.SetSelection(
			self.soundThemes.index(curSoundTheme))
		self.customiseSoundThemeBtn = wx.Button(
			self, wx.ID_ANY, "customise  sound theme")
		self.Bind(wx.EVT_BUTTON, self.onCustomiseSoundTheme,
				  self.customiseSoundThemeBtn)
		self.importBtn = wx.Button(self, wx.ID_ANY, "import sound theme")
		self.Bind(wx.EVT_BUTTON, self.onImportTheme,  self.importBtn)
		self.deleteBtn = wx.Button(self, wx.ID_ANY, "delete sound theme")
		self.Bind(wx.EVT_BUTTON, self.onDeleteTheme, self.deleteBtn)

	def onSave(self):
		selSoundTheme = self.soundThemeSelector.GetStringSelection()
		config.conf["unspokenpy3"]["soundtheme"] = selSoundTheme
		log.info("sound theme: " + config.conf["unspokenpy3"]["soundtheme"])
		createSoundFiles(self.soundTheme)
		loadSoundTheme(selSoundTheme)
		self.Destroy()

	def onCustomiseSoundTheme	(self, evt):
		dlg = CustomiseSoundThemeDialog(self)
		dlg.ShowModal()


	def onImportTheme(self, evt):
		importSoundThemePath= None
		log.info("import button pressed")
		wildcard = "zip file containing sound theme(*.zip) |*.zip|"
		dlg = wx.FileDialog(self, wildcard=wildcard, style=wx.FD_CHANGE_DIR |
							wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, defaultDir=os.path.expandvars("%userprofile%"))
		if dlg.ShowModal() == wx.ID_OK:
			importSoundThemePath = dlg.GetPath()
		log.info("importing theme" + importSoundThemePath)
		dlg.Destroy()
		importTheme(importSoundThemePath)
		self.soundThemes = getAvailableSoundThemes()
		self.soundThemeSelector.SetItems(self.soundThemes)
		self.soundThemeSelector.SetSelection(self.soundThemeSelector.Count-1)

	def onDeleteTheme(self, evt):
		log.info("deleting sound theme: " +
				 self.soundThemeSelector.GetStringSelection())
		deleteSoundTheme(self.soundThemeSelector.GetStringSelection())
		self.soundThemeSelector.SetItems(getAvailableSoundThemes())
		self.soundThemeSelector.SetSelection(self.soundThemeSelector.Count - 1)
		config.conf["unspokenpy3"]["soundtheme"] = self.soundThemeSelector.GetStringSelection()


class CustomiseSoundThemeDialog (gui.SettingsDialog):
	title = _('customise sound theme  setting ')
	def __init__(self, parent) -> None:
		super(CustomiseSoundThemeDialog, self).__init__( parent)
		self.soundTheme = parent.soundThemeSelector.GetStringSelection()
		self.filesToCopy = {}



	def makeSettings(self, settingsSizer):
		self.controlLabel = wx.StaticText(
			self, wx.ID_ANY, "window control list")
		self.controlList = wx.ListBox(
			self, wx.ID_ANY, choices= CONTROL_ROLE_NAMES)
		self.selectAudioBtn = wx.Button(self, wx.ID_ANY, " select wave file ")
		self.Bind(wx.EVT_BUTTON, self.onSelectAudio,  self.selectAudioBtn)

	def onOk(self, evt):
		log.info ("files copy length: {length}".format (length = len(self.filesToCopy)))
		for key in self.filesToCopy:
			log.info("key: {key}".format(key=key))
			log.info ("   path: {source} theme: {soundTheme}".format(**self.filesToCopy[key]))
			copySoundFile(key,**self.filesToCopy[key])
		self.Destroy()
		
	def onSelectAudio(self, evt):
		log.info("sound theme: {st} selected list item: {sl}".format(st=self.soundTheme, sl=self.controlList.GetStringSelection()))
		selectedRole = self.controlList.GetStringSelection()
		wildcard = "wave file with mono channel  (.wav) |*.wav|"
		dlg = wx.FileDialog(self, wildcard=wildcard, style=wx.FD_CHANGE_DIR |
							wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, defaultDir=os.path.expandvars("%userprofile%"))
		if dlg.ShowModal() == wx.ID_OK:
			audioPath= dlg.GetPath()
		self.filesToCopy[selectedRole]={'source': audioPath, 'soundTheme': self.soundTheme}
		dlg.Destroy()
		log.info (" path: {source} theme: {soundTheme}".format(**self.filesToCopy[selectedRole]))
