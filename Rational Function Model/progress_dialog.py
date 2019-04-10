
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PBarWindow(object):

    def __init__(self):
        print("")

    def setupUi(self, MainWindow_PB):

        MainWindow_PB.setObjectName("MainWindow_PB")
        MainWindow_PB.resize(529, 157)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow_PB.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow_PB)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 70, 471, 23))
        self.progressBar.setObjectName("progressBar")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap("loading_icon.png")
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(35, 25, 31, 31)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(75, 30, 301, 21))
        self.label_2.setObjectName("label_2")

        MainWindow_PB.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow_PB)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 29))
        self.menubar.setObjectName("menubar")
        MainWindow_PB.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow_PB)
        self.statusbar.setObjectName("statusbar")
        MainWindow_PB.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_PB)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_PB)

    def retranslateUi(self, MainWindow_PB):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_PB.setWindowTitle(_translate("MainWindow_PB", "Progress Dialog"))
        self.label_2.setText(_translate("MainWindow_PB", "Generating RPC file. Please Wait . . ."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_PB = QtWidgets.QMainWindow()
    ui = Ui_PBarWindow()
    ui.setupUi(MainWindow_PB)
    MainWindow_PB.show()
    sys.exit(app.exec_())

