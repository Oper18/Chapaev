"""

Frontend First Interface for Chapaev Project

"""


import sys
from PyQt5 import uic, QtWidgets


chapaev = QtWidgets.QApplication(sys.argv)
main_window = uic.loadUi('fe_main_window.ui')


main_window.show()
sys.exit(chapaev.exec_())
