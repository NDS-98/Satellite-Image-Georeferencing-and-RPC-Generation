import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QProgressDialog
from progress_dialog import Ui_PBarWindow
from model import RPC

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 290)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_rmse = QtWidgets.QLabel(self.centralwidget)
        self.label_rmse.setGeometry(QtCore.QRect(40,180,600,20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_rmse.setFont(font)
        self.label_rmse.setObjectName("label_rmse")
        self.label_rmse.hide()

        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(220, 87, 381, 24))
        self.inputText.setObjectName("inputText")
        self.inputText.setStyleSheet("QLineEdit{ border: 2px solid gray;"
                                                "border-radius: 5px;}")

        self.outputText = QtWidgets.QLineEdit(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(220, 136, 381, 24))
        self.outputText.setObjectName("outputText")
        self.outputText.setStyleSheet("QLineEdit{ border: 2px solid gray;"
                                                 "border-radius: 5px;}")

        self.browseInput = QtWidgets.QPushButton(self.centralwidget)
        self.browseInput.setGeometry(QtCore.QRect(650, 85, 93, 28))
        self.browseInput.setObjectName("browseInput")

        self.browseOutput = QtWidgets.QPushButton(self.centralwidget)
        self.browseOutput.setGeometry(QtCore.QRect(650, 135, 93, 28))
        self.browseOutput.setObjectName("browseOutput")

        self.buttonOk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOk.setGeometry(QtCore.QRect(340, 230, 93, 28))
        self.buttonOk.setObjectName("buttonOk")
        # self.buttonOk.setStyleSheet("QPushButton{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 grey);"
        #                             "border-style: solid;"
        #                             "border-color: black;"
        #                             "border-width: 2px;"
        #                             "border-radius: 5px;}")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonOk.clicked.connect(self.button_ok)
        self.browseInput.clicked.connect(self.openFileNameDialog)
        self.browseOutput.clicked.connect(self.openFolderNameDialog)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPCGen"))
        self.label.setText(_translate("MainWindow", "Input GCP file location"))
        self.label_2.setText(_translate("MainWindow", "Output location"))
        self.label_rmse.setText(_translate("MainWindow", "Root Mean Squared Error (RMSE) : "))
        self.browseInput.setText(_translate("MainWindow", "Browse"))
        self.browseOutput.setText(_translate("MainWindow", "Browse"))
        self.buttonOk.setText(_translate("MainWindow", "OK"))

########################################################################

    # Display message
    def message(self,title_text,label_text,icon_type):
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setText(label_text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle(title_text)
        msg.resize(300, 150)

        msg.show()
        msg.exec_()

########################################################################

    # OK button functionality
    def button_ok(self):
        if self.inputText.text() == "" or self.outputText.text() == "":
            self.message("Error", "Fields must be non-empty!",QMessageBox.Critical)
        else:
            # Connecting other window to this one
            self.progress_window = QtWidgets.QMainWindow()
            self.ui = Ui_PBarWindow()
            self.ui.setupUi(self.progress_window)
            self.progress_window.show()
            self.ui.progressBar.setValue(0)
            QtWidgets.QApplication.processEvents()
            self.rpc = RPC()
            self.rpc.pgbar=self.ui.progressBar
            self.rpc.inputfileLoc = self.inputText.text()
            self.rpc.outputfileLoc = self.outputText.text()
            self.rpc.writeToFile()
            self.ui.progressBar.setValue(100)

            time.sleep(1)

            self.label_rmse.setText("Root Mean Squared Error (RMSE) : "+str(self.rpc.rmse)+" pixels")
            self.label_rmse.show()

            self.progress_window.hide()
            self.message("Done", "The RPC file is generated at the desired location with RMSE : "+str(self.rpc.rmse)+" pixels",QMessageBox.Information)

########################################################################

    # Browse buttons
    def openFileNameDialog(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(), 'Browse File', 'C:\\', "Text file(*.txt)")
        self.inputText.setText(filename[0])

    def openFolderNameDialog(self):
        foldername = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QWidget(), 'Select Directory', 'C:\\')
        self.outputText.setText(foldername)

########################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

