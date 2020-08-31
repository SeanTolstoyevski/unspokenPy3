# -*- coding: utf-8 -*-
# Copyright (C) 2020 - Sean: mailto:s.tostoyevski@gmail.com
# GitHub: https://github.com/SeanTolstoyevski
# This project is licensed under the MIT license. You are free to do whatever you want as long as you accept your liability.

import os
# : NVDA's modules
import addonHandler
import config
import controlTypes
import globalPluginHandler
import NVDAObjects
import speech
import ui
# : 3rd party module
from .camlorn_audio import *
from .setting import UnspokenSettingsPanel
import gui
from .soundtheme import *

AUDIO_WIDTH = 10.0  # Width of the audio display.
AUDIO_DEPTH = 5.0  # Distance of listener from display.

confspec = {
    "active": "boolean(default=true)",
    "soundtheme": "default theme"
}

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = _("Unspoken")

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(UnspokenSettingsPanel)

        config.conf.spec["unspokenpy3"] = confspec

        init_camlorn_audio()
        loadSoundTheme(config.conf.spec["unspokenpy3"]["soundtheme"])
        self._room_reverb = Reverb()
        self._room_reverb.set_reverb_density(0)
        self._room_reverb.set_Decay_time(0.4)
        self._room_reverb.set_gain(1)
        self._room_reverb.set_reflections_gain(0.4)
        self._room_reverb.set_late_reverb_gain(0)

        self._NVDA_getSpeechTextForProperties = speech.getPropertiesSpeech
        speech.getPropertiesSpeech = self._hook_getSpeechTextForProperties

        self._previous_mouse_object = None

    def _hook_getSpeechTextForProperties(self, reason=NVDAObjects.controlTypes.REASON_QUERY, *args, **kwargs):
        role = kwargs.get('role', None)
        if role:
            if config.conf["unspokenpy3"]["active"] and \
                    'role' in kwargs and role in sounds:
                del kwargs['role']
        return self._NVDA_getSpeechTextForProperties(reason, *args, **kwargs)

    def controlPlayer(self):
        if self.activeVar == True:
            self.play_object(self)

    def play_object(self, obj):
        global AUDIO_WIDTH, AUDIO_DEPTH
        role = obj.role
        if role in sounds:
            desktop = NVDAObjects.api.getDesktopObject()
            desktop_max_x = desktop.location[2]
            desktop_max_y = desktop.location[3]
            desktop_aspect = float(desktop_max_y) / float(desktop_max_x)
            if obj.location != None:
                obj_x = obj.location[0] + (obj.location[2] / 2.0)
                obj_y = obj.location[1] + (obj.location[3] / 2.0)
            else:
                obj_x = desktop_max_x / 2.0
                obj_y = desktop_max_y / 2.0
            position_x = (obj_x / desktop_max_x) * (AUDIO_WIDTH * 2) - AUDIO_WIDTH
            position_y = (obj_y / desktop_max_y) * (desktop_aspect * AUDIO_WIDTH * 2) - (desktop_aspect * AUDIO_WIDTH)
            position_y *= -1
            sounds[role].set_position(position_x, position_y, AUDIO_DEPTH * -1)
            sounds[role].play()

    def event_becomeNavigatorObject(self, obj, nextHandler, isFocus=False):
        if config.conf["unspokenpy3"]["active"]:
            self.play_object(obj)
        else:
            pass
        nextHandler()

    def event_mouseMove(self, obj, nextHandler, x, y):
        if obj != self._previous_mouse_object:
            self._previous_mouse_object = obj
            if config.conf["unspokenpy3"]["active"]:
                self.play_object(obj)
        nextHandler()

    def script_changeActivate(self, gesture):
        if config.conf["unspokenpy3"]["active"]:
            speech.cancelSpeech()
            ui.message(_("Disable Unspoken"))
            config.conf["unspokenpy3"]["active"] = False
        elif config.conf["unspokenpy3"]["active"] == False:
            speech.cancelSpeech()
            ui.message(_("Enable Unspoken"))
            config.conf["unspokenpy3"]["active"] = True
        else:
            pass

    script_changeActivate.__doc__ = _("Changes the active  / deactive  mode of Unspoken.")
    __gestures = {
        "kb:control+shift+u": "changeActivate",
    }
