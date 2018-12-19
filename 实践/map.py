# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import io
import path_find
#import login

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(802, 496)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background:rgb(198, 255, 254)"))
        self.layout_2 = QtGui.QGridLayout(Form)
        self.layout_2.setObjectName(_fromUtf8("layout_2"))
        self.layout = QtGui.QGridLayout()
        self.layout.setMargin(10)
        self.layout.setSpacing(10)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.Textcity = QtGui.QLabel(Form)
        self.Textcity.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Textcity.setFont(font)
        self.Textcity.setObjectName(_fromUtf8("Textcity"))
        self.layout.addWidget(self.Textcity, 0, 0, 1, 1)
        self.goal = QtGui.QLineEdit(Form)
        self.goal.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.goal.setFont(font)
        self.goal.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.goal.setObjectName(_fromUtf8("goal"))
        self.layout.addWidget(self.goal, 4, 3, 1, 1)
        self.Button = QtGui.QPushButton(Form)
        self.Button.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Button.setFont(font)
        self.Button.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.Button.setObjectName(_fromUtf8("Button"))
        self.layout.addWidget(self.Button, 5, 3, 1, 1)
        self.Textfrom = QtGui.QLabel(Form)
        self.Textfrom.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Textfrom.setFont(font)
        self.Textfrom.setObjectName(_fromUtf8("Textfrom"))
        self.layout.addWidget(self.Textfrom, 1, 3, 1, 1)
        self.start = QtGui.QLineEdit(Form)
        self.start.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.start.setObjectName(_fromUtf8("start"))
        self.layout.addWidget(self.start, 2, 3, 1, 1)
        self.Textto = QtGui.QLabel(Form)
        self.Textto.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Textto.setFont(font)
        self.Textto.setObjectName(_fromUtf8("Textto"))
        self.layout.addWidget(self.Textto, 3, 3, 1, 1)
        self.Listcity = QtGui.QComboBox(Form)
        self.Listcity.setMaximumSize(QtCore.QSize(900, 600))
        self.Listcity.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Listcity.setObjectName(_fromUtf8("Listcity"))
        self.layout.addWidget(self.Listcity, 0, 1, 1, 1)
        self.tabPath = QtGui.QTabWidget(Form)
        self.tabPath.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tabPath.setObjectName(_fromUtf8("tabPath"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab_1"))
        self.tabPath.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabPath.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabPath.addTab(self.tab_3, _fromUtf8(""))
        self.layout.addWidget(self.tabPath, 7, 0, 1, 3)
        self.map = QtGui.QGraphicsView(Form)
        self.map.setEnabled(True)
        self.map.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.map.setFont(font)
        self.map.setStyleSheet(_fromUtf8("border-image: (beijing.jpg);"))
        self.map.setObjectName(_fromUtf8("map"))
        self.layout.addWidget(self.map, 1, 0, 6, 3)
        self.layout.setColumnStretch(1, 10)
        self.layout.setColumnStretch(2, 90)
        self.layout.setColumnStretch(3, 10)
        self.layout.setRowStretch(1, 10)
        self.layout.setRowStretch(6, 60)
        self.layout.setRowStretch(7, 40)
        self.layout_2.addLayout(self.layout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabPath.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Underground path finder", None))
        self.Textcity.setText(_translate("Form", "City :", None))
        self.Button.setText(_translate("Form", "Search", None))
        self.Textfrom.setText(_translate("Form", "Start:", None))
        self.Textto.setText(_translate("Form", "Goal:", None))
        self.tabPath.setTabText(self.tabPath.indexOf(self.tab), _translate("Form", "Best route", None))
        self.tabPath.setTabText(self.tabPath.indexOf(self.tab_2), _translate("Form", "Fewer transfer", None))
        self.tabPath.setTabText(self.tabPath.indexOf(self.tab_3), _translate("Form", "Less walking", None))


        self.Button.clicked.connect(self.find_path)

    def find_path(self):
        command=self.Button.text()

        cityname="london"
        start=self.start.text()
        goal=self.goal.text()
        #
        start="Westminster"
        goal="Euston"
        #
        if command=="Search":
        
            result = str(path_find.search(cityname,start,goal))
            print (result)

            layout = QFormLayout()
            layout.addRow("Name",QLineEdit())
            layout.addRow("Address",QLineEdit())
            self.setTabText(0,"Contact Details")
            self.tab1.setLayout(layout)

             
            self.setTabText(0,result)
            self.Button.setText(_translate("Form", "Clear", None))
        else:
            self.tabPath.indexOf(self.tab).setText("")
            self.Button.setText(_translate("Form", "Search", None))
        
if __name__ == '__main__':
    '''
    username,mapname = str(login())
    print (username,mapname)
    if username !="":
    '''
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


