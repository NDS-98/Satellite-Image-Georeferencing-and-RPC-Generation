# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import extract
import warp
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.srcPoints=None
        self.dstPoints=None
        self.dstLoc=None
        self.srcLoc=None
        self.triangleCount=None
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 310)
        self.dialog=Dialog
        self.label_5=QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90,60,55,16))
        self.label_5.setText("Enter Points for Image:")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 60, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 401, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 140, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 190, 121, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 81, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 190, 121, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 190, 91, 20))
        self.label_4.setObjectName("label_4")
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.doGeoreferencing)
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton_3.clicked.connect(self.openPointsFileDialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.adjustSize()
        self.label_2.setText(_translate("Dialog", "Points File"))
        self.pushButton.setText(_translate("Dialog", "Proceed"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Browse"))
        self.label_3.setText(_translate("Dialog", "Polynomial"))
        self.label_4.setText(_translate("Dialog", "Resampling"))
        self.comboBox.setItemText(0, _translate("MainWindow", "First Order"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Second Order"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Third Order"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Nearest Neighbour"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Cubic"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Cubic spline"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Bilinear"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Lanczos"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Average"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Mode"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Maximum"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Minimum"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Median"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "First Quartile"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Third Quartile"))
    def openPointsFileDialog(self):
        pointsFile=QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(),'Browse Points File','','GCP file (*.points)')
        self.lineEdit.setText(pointsFile[0])
    def doGeoreferencing(self):
        self.dialog.close
        warp.georeference(self.srcPoints,self.dstPoints,self.triangleCount,self.srcLoc,self.dstLoc,str(self.comboBox.currentText()),str(self.comboBox_2.currentText()),self.lineEdit.text())
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(112, 210, 511, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(112, 280, 511, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 510, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 510, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 210, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(436, 380, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(26, 380, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(112, 130, 511, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(6, 130, 91, 20))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 111, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 340, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 130, 89, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.openFolderNameDialog)
        self.pushButton_2.clicked.connect(self.openPointsFileDialog)
        self.pushButton_5.clicked.connect(self.openFileNameDialog)
        self.pushButton_3.clicked.connect(self.startWarping)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Piecewise Georeferenccer"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_3.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "Output Dir"))
        self.label_2.setText(_translate("MainWindow", "Points file"))
        self.label_5.setText(_translate("MainWindow", "Source Image"))
        self.pushButton_5.setText(_translate("MainWindow", "Browse"))
        self.label_8.setText(_translate("MainWindow", "Error Threshold"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.005"))

    def startWarping(self):
        if(self.lineEdit.text()=='' or self.lineEdit_2.text()=='' or self.lineEdit_3.text()==''):
            #TODO: enter a warning dialog box
            print("fill all boxes")
        else:
            #TODO: call warping functions
            self.progress=QtWidgets.QProgressBar(self.centralwidget)
            self.progress.setGeometry(QtCore.QRect(300, 330, 118, 23))
            self.progress.setValue(0)
            self.progress.show()
            (self.srcPoints,self.dstPoints)=extract.takeInput(self.lineEdit_2.text())
            warp.divideInTriangles(self,self.progress,self.srcPoints,self.dstPoints,self.lineEdit_3.text(),self.lineEdit.text(),threshold=float(self.lineEdit_4.text()))
    def openFileNameDialog(self):

        fileName = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(), 'Browse file', '',
                                                   "all files(*);;corona image file (*.tif)")

        self.lineEdit_3.setText(fileName[0])

    def openFolderNameDialog(self):

        folderName = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select Directory")

        self.lineEdit.setText(folderName)
    def openPointsFileDialog(self):
        pointsFile=QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(),'Browse Points File','','GCP file (*.points)')
        self.lineEdit_2.setText(pointsFile[0])
    def showDial(self,triangleCount,srcPoints,dstPoints,dstLoc,srcLoc):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(dstLoc+'/'+str(triangleCount)+'.png')
        ui.srcPoints=srcPoints
        ui.dstPoints=dstPoints
        ui.dstLoc=dstLoc
        ui.srcLoc=srcLoc
        ui.triangleCount=triangleCount
        ui.label.adjustSize()
        Dialog.exec_()
if __name__ =="__main__": 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

