# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
                                         "    wight: 150 px;\n"
                                         "    height: 70 px; \n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 60, 241, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WoodWork_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.WoodWork_Button.setEnabled(True)
        self.WoodWork_Button.setStyleSheet("")
        self.WoodWork_Button.setIconSize(QtCore.QSize(20, 20))
        self.WoodWork_Button.setCheckable(False)
        self.WoodWork_Button.setObjectName("WoodWork_Button")
        self.verticalLayout.addWidget(self.WoodWork_Button)
        self.Cloth_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Cloth_Button.setObjectName("Cloth_Button")
        self.verticalLayout.addWidget(self.Cloth_Button)
        self.Blacksmith_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Blacksmith_Button.setObjectName("Blacksmith_Button")
        self.verticalLayout.addWidget(self.Blacksmith_Button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WoodWork_Button.setText(_translate("MainWindow", "WoodWork"))
        self.Cloth_Button.setText(_translate("MainWindow", "Cloth"))
        self.Blacksmith_Button.setText(_translate("MainWindow", "Blaksmith"))
