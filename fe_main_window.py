import sys
from PyQt5 import uic, QtWidgets




def single_player_push():
    print('Button 1 pressed')
    main_window.textBrowser.setText('Not working yet')


def multi_player_push():
    print('Button 2 pressed')
    main_window.textBrowser.setText('Not working yet')


def options_push():
    print('Button 3 pressed')
    main_window.textBrowser.setText('Not working yet')


def records_push():
    print('Button 4 pressed')
    main_window.textBrowser.setText('Not working yet')


def quit_push():
    print('Button 5 pressed')
    chapaev.quit()


chapaev = QtWidgets.QApplication(sys.argv)
main_window = uic.loadUi('fe_main_window.ui')
main_window.show()

main_window.pushButton_1.clicked.connect(single_player_push)
main_window.pushButton_2.clicked.connect(multi_player_push)
main_window.pushButton_3.clicked.connect(options_push)
main_window.pushButton_4.clicked.connect(records_push)
main_window.pushButton_5.clicked.connect(quit_push)

sys.exit(chapaev.exec_())


