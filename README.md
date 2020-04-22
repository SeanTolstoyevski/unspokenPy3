	# unspokenPy3

## A few very important note!

	**I am not the main developer of the addon.**

	***

	This add-on was running before the 2019.3 releases of NVDA.  
	Developer was not developing the addon.

	Afterwards, a Sudanese friend named Musharraf Omer built a new add-on by building the Audiothemes addon on Unspoken.
	Audiothemes have familiar problems.
	For example, some sounds crack.

	Most of Unspoken is written in C.
	So it works faster and more stable against pure Python code.
	Audiothemes react relatively slowly.

	**All sources mentioned here**:

	* Unspoken
		- Main Repo: https://github.com/camlorn/Unspoken
		- Developer's GitHub profile: https://github.com/camlorn
		- Non-license
	* Audiothemes
		- Main Repo: https://github.com/mush42/Audio-Themes-NVDA-Add-on
		- Developer's GitHub profile: https://github.com/mush42/
		- Non-license

	***

	I don't want to do  hurt the author of the add-on.
	Unspoken is a very important add-on for me.
	NVDA without it is bad 😢 .
	I wanted to open the source code to everyone.
	Please respect the great effort of the Unspoken main developer.

	## Addon Status
	* Beta

	**Note**:

	If you are not a developer, I wouldn't recommend running the plugin in beta.

	## Steps for Use or test or developing

	1. Clone this repo to test or use the plugin:  
	`git clone https://github.com/SeanTolstoyevski/unspokenPy3`
	or download it from the GitHub page.
	2. Copy the addon folder in the repo folder to the appdata/roaming/nvda / addon folder.  
**NVDA's steps for your own configuration are not here.**
	3. and change the folder name to "unspoken".
	4. Restart NVDA.

	## Issues that need help

	I searched and couldn't find it.
	Feel free to create a PR for the problem.
	A very simple problem for experienced NVDA developers 🤗.

	```
	WARNING - eventHandler._EventExecuter.next (21:56:30.419) - MainThread (2404):
	Could not execute function event_becomeNavigatorObject defined in globalPlugins.Unspoken module; kwargs: {'isFocus': True}
	Traceback (most recent call last):
	  File "eventHandler.pyc", line 100, in next
	TypeError: event_becomeNavigatorObject() got an unexpected keyword argument 'isFocus'
	```

	## License

	This repo is licensed under the MIT License.
	Components created by other developers may have a other license.
	- [MIT Lıcense](https://github.com/SeanTolstoyevski/unspokenPy3/blob/master/LICENSE)
