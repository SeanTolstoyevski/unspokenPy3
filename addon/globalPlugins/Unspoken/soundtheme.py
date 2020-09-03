import os
import shutil
from zipfile import ZipFile
import controlTypes
from .camlorn_audio import Sound3D

UNSPOKEN_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
UNSPOKEN_SOUNDS_PATH = os.path.join(UNSPOKEN_ROOT_PATH, "sounds")

CONTROL_ROLE_IDS_NAMES = controlTypes.roleLabels
CONTROL_ROLE_IDS = list(CONTROL_ROLE_IDS_NAMES.keys())
CONTROL_ROLE_NAMES = list (CONTROL_ROLE_IDS_NAMES.values())

sound_files = {}
sounds = dict()


def createSoundFiles(soundTheme):
	sound_files.clear()
	files = os.listdir(os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme))
	for f in files:
		fileName, fileExt = os.path.splitext(f)
		if fileName in CONTROL_ROLE_NAMES and fileExt == ".wav":
			sound_files[CONTROL_ROLE_IDS[CONTROL_ROLE_NAMES.index(fileName)]] = fileName+fileExt
def loadSoundTheme(soundTheme):
	sounds.clear ()
	for key in sound_files:
		sounds[key] = Sound3D(os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme,  sound_files[key]))
		sounds[key].set_rolloff_factor(0)

def deleteSoundTheme (soundTheme):
	import shutil 
	shutil.rmtree(os.path.join (UNSPOKEN_SOUNDS_PATH, soundTheme))


def getAvailableSoundThemes():
	soundThemes = []
	dirs = os.listdir(UNSPOKEN_SOUNDS_PATH)
	for d in dirs:
		if os.path.isdir(os.path.join(UNSPOKEN_SOUNDS_PATH, d)):
			soundThemes.append(d)
	return soundThemes


def importTheme(path):
	soundThemeFile = ZipFile(path)
	os.chdir(UNSPOKEN_SOUNDS_PATH)
	soundThemeFile.extractall()

def copySoundFile (role, source, soundTheme):
	dst = os.path.join (UNSPOKEN_SOUNDS_PATH, soundTheme, "{role}.wav".format (role= role))	
	if os.path.exists(dst):
		os.remove(dst)
	shutil.copy(source,dst)	