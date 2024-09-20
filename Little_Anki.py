# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/Little_Anki

from aqt import mw

# Tentando importar do PyQt5 ou PyQt6
try:
    from PyQt6.QtCore import Qt  # PyQt6 usa este caminho e estrutura
    from PyQt6.QtWidgets import QApplication
except ImportError:
    from PyQt5.QtCore import Qt  # Caso PyQt6 não esteja disponível, fallback para PyQt5
    from PyQt5.QtWidgets import QApplication

# Compatibilidade entre PyQt5 e PyQt6 para o flag de maximização
try:
    # PyQt6 coloca as flags de janela dentro de WindowType
    WindowMaximizeButtonHint = Qt.WindowType.WindowMaximizeButtonHint
except AttributeError:
    # PyQt5 usa diretamente dentro de Qt
    WindowMaximizeButtonHint = Qt.WindowMaximizeButtonHint

# Disable the maximization button
mw.setWindowFlags(mw.windowFlags() & ~WindowMaximizeButtonHint)
mw.show()  # Necessary for the flag changes to take effect

# -------------Configuration------------------
config = mw.addonManager.getConfig(__name__)
MaximumWidth = config.get('MaximumWidth', 400)  # Default to 400 if not specified
MaximumHeight = config.get('MaximumHeight', 400)  # Default to 400 if not specified
# -------------Configuration------------------

# Applying the configurations:
mw.setMaximumWidth(MaximumWidth)
mw.setMaximumHeight(MaximumHeight)

# Alterar o tamanho da fonte global da interface para reduzir a escala geral
QApplication.instance().setStyleSheet("QWidget { font-size: 8pt; }")  # Reduzir o tamanho da fonte
# Apply zoom. For example, 0.6 is 60% of the original size (zoom out):
mw.web.setZoomFactor(0.6)
