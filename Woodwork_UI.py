# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WoodWork.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Woodwork(object):
    def setupUi(self, Woodwork):
        Woodwork.setObjectName("Woodwork")
        Woodwork.resize(437, 274)
        self.centralwidget = QtWidgets.QWidget(Woodwork)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 171, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 40, 141, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setTabletTracking(False)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 10, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 170, 121, 41))
        self.pushButton.setObjectName("pushButton")
        Woodwork.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Woodwork)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 26))
        self.menubar.setObjectName("menubar")
        Woodwork.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Woodwork)
        self.statusbar.setObjectName("statusbar")
        Woodwork.setStatusBar(self.statusbar)

        self.retranslateUi(Woodwork)
        QtCore.QMetaObject.connectSlotsByName(Woodwork)

    def retranslateUi(self, Woodwork):
        _translate = QtCore.QCoreApplication.translate
        Woodwork.setWindowTitle(_translate("Woodwork", "MainWindow"))
        self.checkBox.setText(_translate("Woodwork", "Bow"))
        self.checkBox_2.setText(_translate("Woodwork", "Inferno Staff"))
        self.checkBox_3.setText(_translate("Woodwork", "Ice Staff"))
        self.checkBox_4.setText(_translate("Woodwork", "Light Staff"))
        self.checkBox_5.setText(_translate("Woodwork", "Restoretaion Staff"))
        self.lineEdit.setText(_translate("Woodwork", "Title"))
        self.checkBox_6.setText(_translate("Woodwork", "Epic"))
        self.checkBox_7.setText(_translate("Woodwork", "Legendary"))
        self.lineEdit_2.setText(_translate("Woodwork", "Quality"))
        self.pushButton.setText(_translate("Woodwork", "Make a gold!"))


