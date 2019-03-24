# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Pictures/ai logos/human_portal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.img_predict = QtWidgets.QPushButton(self.centralwidget)
        self.img_predict.setObjectName("img_predict")
        self.gridLayout.addWidget(self.img_predict, 0, 2, 1, 1)
        self.img_predict_out = QtWidgets.QLabel(self.centralwidget)
        self.img_predict_out.setObjectName("img_predict_out")
        self.gridLayout.addWidget(self.img_predict_out, 1, 2, 1, 1)
        self.img_in = QtWidgets.QLabel(self.centralwidget)
        self.img_in.setObjectName("img_in")
        self.gridLayout.addWidget(self.img_in, 1, 0, 1, 1)
        self.img_open = QtWidgets.QPushButton(self.centralwidget)
        self.img_open.setCheckable(False)
        self.img_open.setChecked(False)
        self.img_open.setObjectName("img_open")
        self.gridLayout.addWidget(self.img_open, 0, 0, 1, 1)
        self.img_grey = QtWidgets.QLabel(self.centralwidget)
        self.img_grey.setObjectName("img_grey")
        self.gridLayout.addWidget(self.img_grey, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Clasiffier"))
        self.img_predict.setText(_translate("MainWindow", "Make prediction"))
        self.img_predict_out.setText(_translate("MainWindow", "Prediction"))
        self.img_in.setText(_translate("MainWindow", "image"))
        self.img_open.setText(_translate("MainWindow", "Open img"))
        self.img_grey.setText(_translate("MainWindow", "grey image"))

