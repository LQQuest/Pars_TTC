import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Woodwork_UI import Ui_Woodwork
from Parser import main
from Main_UI import Ui_MainWindow
from Clother_UI import Ui_Clother
from Blacksmith_UI import Ui_Blaksmith

WoodWork_URL = 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=12749&ItemNamePattern=Sealed+Woodworking+Writ&page='
Clothier_URL = 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=&ItemNamePattern=Sealed+Clothier+Writ&page='
Blacksmith_URL = 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=13082&ItemNamePattern=Sealed+Blacksmithing+Writ&page='


class top_gui(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.WoodWork_Button.clicked.connect(self.wood_click)
        self.ui.Blacksmith_Button.clicked.connect(self.blacksmith_click)
        self.ui.Cloth_Button.clicked.connect(self.cloth_click)

    def wood_click(self):
        WoodWindow.show()

    def blacksmith_click(self):
        BlacksmithWindow.show()

    def cloth_click(self):
        ClothWindow.show()


class WoodGUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Woodwork()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        project_title = []
        if self.ui.checkBox.isChecked():
            project_title.append("Ruby Ash Bow")
        if self.ui.checkBox_2.isChecked():
            project_title.append("Ruby Ash Inferno Staff")
        if self.ui.checkBox_3.isChecked():
            project_title.append("Ruby Ash Ice Staff")
        if self.ui.checkBox_4.isChecked():
            project_title.append("Ruby Ash Lightning Staff")
        if self.ui.checkBox_5.isChecked():
            project_title.append("Ruby Ash Restoration Staff")

        project_quality = []
        if self.ui.checkBox_6.isChecked():
            project_quality.append("Epic")
        if self.ui.checkBox_7.isChecked():
            project_quality.append("Legendary")

        WoodWindow.close()

        main(project_title, project_quality, WoodWork_URL, 30, 5)


class BlacksmithGUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Blaksmith()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        project_title = []
        if self.ui.checkBox.isChecked():
            project_title.append("Rubedite Helm")
        if self.ui.checkBox_2.isChecked():
            project_title.append("Rubedite Pauldron")
        if self.ui.checkBox_3.isChecked():
            project_title.append("Rubedite Cuirass")
        if self.ui.checkBox_4.isChecked():
            project_title.append("Rubedite Gauntlets")
        if self.ui.checkBox_5.isChecked():
            project_title.append("Rubedite Girdle")
        if self.ui.checkBox_6.isChecked():
            project_title.append("Rubedite Greaves")
        if self.ui.checkBox_7.isChecked():
            project_title.append("Rubedite Sabatons")

        if self.ui.checkBox_8.isChecked():
            project_title.append("Rubedite Dagger")
        if self.ui.checkBox_9.isChecked():
            project_title.append("Rubedite Sword")
        if self.ui.checkBox_10.isChecked():
            project_title.append("Rubedite Axe")
        if self.ui.checkBox_11.isChecked():
            project_title.append("Rubedite Mace")
        if self.ui.checkBox_12.isChecked():
            project_title.append("Rubedite Greatsword")
        if self.ui.checkBox_13.isChecked():
            project_title.append("Rubedite Battle Axe")
        if self.ui.checkBox_14.isChecked():
            project_title.append("Rubedite Maul")

        project_quality = []
        if self.ui.checkBox_15.isChecked():
            project_quality.append("Epic")
        if self.ui.checkBox_16.isChecked():
            project_quality.append("Legendary")

        BlacksmithWindow.close()

        main(project_title, project_quality, Blacksmith_URL, 30, 5)


class ClothGUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Clother()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        project_title = []
        if self.ui.checkBox.isChecked():
            project_title.append("Ancestor Silk Hat")
        if self.ui.checkBox_2.isChecked():
            project_title.append("Ancestor Silk Epaulets")
        if self.ui.checkBox_3.isChecked():
            project_title.append("Ancestor Silk Robe")
        if self.ui.checkBox_4.isChecked():
            project_title.append("Ancestor Silk Gloves")
        if self.ui.checkBox_5.isChecked():
            project_title.append("Ancestor Silk Sash")
        if self.ui.checkBox_6.isChecked():
            project_title.append("Ancestor Silk Breech")
        if self.ui.checkBox_7.isChecked():
            project_title.append("Ancestor Silk Shoes")

        if self.ui.checkBox_8.isChecked():
            project_title.append("Rubedo Leather Helmet")
        if self.ui.checkBox_9.isChecked():
            project_title.append("Rubedo Leather Arm Cops")
        if self.ui.checkBox_10.isChecked():
            project_title.append("Rubedo Leather Jacks")
        if self.ui.checkBox_11.isChecked():
            project_title.append("Rubedo Leather Bracers")
        if self.ui.checkBox_12.isChecked():
            project_title.append("Rubedo Leather Belt")
        if self.ui.checkBox_13.isChecked():
            project_title.append("Rubedo Leather Guards")
        if self.ui.checkBox_14.isChecked():
            project_title.append("Rubedo Leather Boots")

        project_quality = []
        if self.ui.checkBox_15.isChecked():
            project_quality.append("Epic")
        if self.ui.checkBox_16.isChecked():
            project_quality.append("Legendary")

        ClothWindow.close()

        main(project_title, project_quality, Clothier_URL, 30, 5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = top_gui()
    WoodWindow = WoodGUI()
    ClothWindow = ClothGUI()
    BlacksmithWindow = BlacksmithGUI()
    myapp.show()

    sys.exit(app.exec_())
