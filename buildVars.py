from pathlib import Path



_ = lambda x : x

addon_info = {
	"addon_name" : "unspokenPy3",
	"addon_summary" : _("Unspoken"),
	"addon_description" : _("""Removes names like unspoken, link, button. It plays different sounds instead of informations."""),
	"addon_version" : "0.3",
	"addon_author" : u"Camlorn (main developer): camlorn38@gmail.com, Bryan Smart: NoMail, Sean (ported python3): s.tolstoyevski@gmail.com",
	"addon_url" : None,
	"addon_docFileName" : "readme.html",
	"addon_minimumNVDAVersion" : 2019.3,
	"addon_lastTestedNVDAVersion" : 2020.1,
	"addon_updateChannel" : None,
}



pythonSources = list(Path.cwd().joinpath("addon", "globalPlugins").rglob("*.py"))

i18nSources = pythonSources + ["buildVars.py", "addon\\installTasks.py"]

excludedFiles = []
