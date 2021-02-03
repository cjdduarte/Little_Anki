# -*- coding: utf-8 -*-
#Copyright(C)   | Carlos Duarte
#License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
#Source in      | https://github.com/cjdduarte/Little_Anki

from aqt import mw

#-------------Configuration------------------
config = mw.addonManager.getConfig(__name__)
MaximumWidth = config['MaximumWidth']
MaximumHeight = config['MaximumHeight']
#-------------Configuration------------------

config = mw.addonManager.getConfig(__name__)

#Width
mw.setMaximumWidth(MaximumWidth)
mw.web.setMaximumWidth(MaximumWidth)

#Height
mw.setMaximumHeight(MaximumHeight)
mw.web.setMaximumHeight(MaximumHeight)