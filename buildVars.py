from pathlib import Path



_ = lambda x : x

addon_info = {
	"addon_name" : "unspokenPy3",
	"addon_summary" : _("Unspoken"),
	"addon_description" : _("""Removes names label from object like,  link, button. It plays different sounds instead of labels."""),
	"addon_version" : "0.4",
	"addon_author" : u", Sean (ported python3): s.tolstoyevski@gmail.com, Camlorn (main developer): camlorn38@gmail.com, Bryan Smart: NoMail",
	"addon_url" : "https://github.com/SeanTolstoyevski/unspokenPy3/releases",
	"addon_docFileName" : "readme.html",
	"addon_minimumNVDAVersion" : 2019.3,
	"addon_lastTestedNVDAVersion" : 2022.3,
	"addon_updateChannel" : None,
}



pythonSources = list(Path.cwd().joinpath("addon", "globalPlugins").rglob("*.py"))

i18nSources = pythonSources + ["buildVars.py", "addon\\installTasks.py"]

excludedFiles = []
