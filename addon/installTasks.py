import addonHandler, gui, wx

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "Unspoken Py3":
			askToRemove(addon)
			break

def askToRemove(addon):
	if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("You have installed an old and incompatible version of this addon. Do you want to uninstall the old version?"),
		# Translators: the title of a message box dialog.
		_("Uninstall incompatible add-on"),
		wx.YES|wx.NO|wx.ICON_WARNING) == wx.YES:
			addon.requestRemove()
