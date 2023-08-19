# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/Little_Anki

from aqt import mw
from aqt.qt import Qt

# Disable the maximization button
mw.setWindowFlags(mw.windowFlags() & ~Qt.WindowMaximizeButtonHint)
mw.show()  # Necessary for the flag changes to take effect

#-------------Configuration------------------
config = mw.addonManager.getConfig(__name__)
MaximumWidth = config.get('MaximumWidth', 400)  # Default to 400 if not specified
MaximumHeight = config.get('MaximumHeight', 400)  # Default to 400 if not specified
#-------------Configuration------------------

# Applying the configurations:
mw.setMaximumWidth(MaximumWidth)
mw.setMaximumHeight(MaximumHeight)

# Apply zoom. For example, 0.6 is 60% of the original size (zoom out):
mw.web.setZoomFactor(0.6)
