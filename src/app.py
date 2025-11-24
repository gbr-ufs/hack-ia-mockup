import sys
from hack_ia_mockup import HackIaMockup
from PySide6 import QtWidgets


def run() -> None:
    app = QtWidgets.QApplication([])
    hack_ia = HackIaMockup()
    hack_ia.show()

    sys.exit(app.exec())
