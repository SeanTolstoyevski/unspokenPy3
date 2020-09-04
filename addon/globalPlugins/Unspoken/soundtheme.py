import os
import shutil
from zipfile import ZipFile
import controlTypes
from .camlorn_audio import Sound3D
from config import conf
from logHandler import log

UNSPOKEN_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
UNSPOKEN_SOUNDS_PATH = os.path.join(UNSPOKEN_ROOT_PATH, "sounds")

CONTROL_ROLE_IDS_NAMES = controlTypes.roleLabels
CONTROL_ROLE_IDS = list(CONTROL_ROLE_IDS_NAMES.keys())
CONTROL_ROLE_NAMES = list(CONTROL_ROLE_IDS_NAMES.values())

sound_files = {}
sounds = dict()


def loadSoundTheme(soundTheme):
	sound_files.clear()
	sounds.clear()
	soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme)

	if not os.path.exists(soundThemePath):
		conf["unspokenpy3"]["soundtheme"] = "default theme"
		soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, "default theme")
	files = os.listdir(soundThemePath)

	for f in files:
		fileName, fileExt = os.path.splitext(f)
		if fileName in CONTROL_ROLE_NAMES and fileExt == ".wav":
			sound_files[CONTROL_ROLE_IDS[CONTROL_ROLE_NAMES.index(
				fileName)]] = fileName + fileExt

	for key in sound_files:
		sounds[key] = Sound3D(os.path.join(
			UNSPOKEN_SOUNDS_PATH, soundTheme,  sound_files[key]))
		sounds[key].set_rolloff_factor(0)


def createSoundTheme(soundTheme):
	soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme)
	if not os.path.exists(soundThemePath):
		os.makedirs(soundThemePath)


def deleteSoundTheme(soundTheme):
	soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme)
	if os.path.exists(soundThemePath):
		shutil.rmtree(os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme))


def getAvailableSoundThemes():
	soundThemes = []
	dirs = os.listdir(UNSPOKEN_SOUNDS_PATH)
	for d in dirs:
		if os.path.isdir(os.path.join(UNSPOKEN_SOUNDS_PATH, d)):
			soundThemes.append(d)
	return soundThemes


def importTheme(path):
	soundTheme, fileExt = os.path.splitext(os.path.basename(path))
	soundThemeFile = ZipFile(path)
	soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme)
	if not os.path.exists(soundThemePath):
		os.makedirs(soundThemePath)
	os.chdir(soundThemePath)
	soundThemeFile.extractall()


def exportSoundTheme(path, soundTheme):
	soundThemeFileName, fileExt = os.path.splitext(os.path.basename(path))
	soundThemePath = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme)
	outputSoundThemePath = os.path.join(
	os.path.dirname(path), soundThemeFileName)
	log.info(" zip file: {outputSoundThemePath} sound theme: {soundTheme}".format(outputSoundThemePath=outputSoundThemePath, soundTheme=soundTheme))
	shutil.make_archive(base_name=outputSoundThemePath,
						format='zip', root_dir=soundThemePath)


def copySoundFile(role, source, soundTheme):
	dst = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme,
					   "{role}.wav".format(role=role))
	if os.path.exists(dst):
		os.remove(dst)
	shutil.copy(source, dst)


def deleteSoundFile(role, source, soundTheme):
	dst = os.path.join(UNSPOKEN_SOUNDS_PATH, soundTheme,
					   "{role}.wav".format(role=role))
	if os.path.exists(dst):
		os.remove(dst)
