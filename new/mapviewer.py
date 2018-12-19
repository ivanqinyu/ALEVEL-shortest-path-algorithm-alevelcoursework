# -*- coding: utf-8 -*-
import os
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import path_find

class GRview(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(GRview, self).__init__(parent)

    def wheelEvent(self,x):
        factor = x.delta()
        if x.delta()  > 0:
            factor=2
        else:
            factor=0.5

        self.map.scale(factor,factor)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 622)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background:rgb(255, 255, 255)")
        self.layout_2 = QtWidgets.QGridLayout(Form)
        self.layout_2.setObjectName("layout_2")
        self.layout = QtWidgets.QGridLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)
        self.layout.setObjectName("layout")
        self.Textcity = QtWidgets.QLabel(Form)
        self.Textcity.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Textcity.setFont(font)
        self.Textcity.setObjectName("Textcity")
        self.layout.addWidget(self.Textcity, 0, 0, 1, 1)
        self.goal = QtWidgets.QLineEdit(Form)
        self.goal.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.goal.setFont(font)
        self.goal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.goal.setObjectName("goal")
        self.layout.addWidget(self.goal, 4, 3, 1, 1)
        self.Textfrom = QtWidgets.QLabel(Form)
        self.Textfrom.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Textfrom.setFont(font)
        self.Textfrom.setObjectName("Textfrom")
        self.layout.addWidget(self.Textfrom, 1, 3, 1, 1)
        self.start = QtWidgets.QLineEdit(Form)
        self.start.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start.setObjectName("start")
        self.layout.addWidget(self.start, 2, 3, 1, 1)
        self.Textto = QtWidgets.QLabel(Form)
        self.Textto.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Textto.setFont(font)
        self.Textto.setObjectName("Textto")
        self.layout.addWidget(self.Textto, 3, 3, 1, 1)

        self.Listcity = QtWidgets.QComboBox(Form)
        self.Listcity.setMaximumSize(QtCore.QSize(900, 600))
        self.Listcity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Listcity.setObjectName("Listcity")
        self.layout.addWidget(self.Listcity, 0, 1, 1, 1)
        with sqlite3.connect("userinfo.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Current")
            currentuser = cursor.fetchall()
            
            db.commit()

        s=currentuser[0][1]+","
        start=0
        end=s.find(",")
        while len(s)>1:
            self.Listcity.addItem(s[0:end])
            start=end+2
            s=s[start-1:]
            end=s.find(",")
        self.Listcity.addItem("ADD MAP")

        self.Listcity.currentIndexChanged.connect(self.selectionchange)
        
        self.tabPath = QtWidgets.QTabWidget(Form)
        self.tabPath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabPath.setObjectName("tabPath")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabPath.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabPath.addTab(self.tab2, "")
 
        self.layout.addWidget(self.tabPath, 7, 0, 1, 3)
     
        self.map = QtWidgets.QGraphicsView(Form)
        self.map.setEnabled(True)

        self.viewscene=GRview(self.map)
        Qpix=QtGui.QPixmap(self.Listcity.currentText()+".png")
        self.viewscene.addPixmap(Qpix)
        self.map.setScene(self.viewscene)
        self.map.scale(0.4,0.4)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.map.setFont(font)
        self.map.setMouseTracking(True)

        self.map.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.map.setObjectName("map")
        self.layout.addWidget(self.map, 1, 0, 6, 3)
        self.exit = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(170,0, 0);")
        self.exit.setObjectName("exit")
        self.layout.addWidget(self.exit, 7, 3, 1, 1)
        self.Button = QtWidgets.QPushButton(Form)
        self.Button.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Button.setFont(font)
        self.Button.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Button.setObjectName("Button")
        self.layout.addWidget(self.Button, 5, 3, 1, 1)
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
        Form.setTabOrder(self.Listcity, self.start)
        Form.setTabOrder(self.start, self.goal)
        Form.setTabOrder(self.goal, self.Button)
        Form.setTabOrder(self.Button, self.tabPath)
        Form.setTabOrder(self.tabPath, self.exit)
        Form.setTabOrder(self.exit, self.map)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        with sqlite3.connect("userinfo.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Current")
            currentuser = cursor.fetchall()
            db.commit()
        Form.setWindowTitle(_translate("Form", "Underground path finder. Welcome "+currentuser[0][0]))
        self.Textcity.setText(_translate("Form", "City :"))
        self.Textfrom.setText(_translate("Form", "Start:"))
        self.Textto.setText(_translate("Form", "Goal:"))
        self.tabPath.setTabText(self.tabPath.indexOf(self.tab1), _translate("Form", "Best route"))
        self.tabPath.setTabText(self.tabPath.indexOf(self.tab2), _translate("Form", "Fewer transfer"))

        self.exit.setText(_translate("Form", "Log off"))
        self.Button.setText(_translate("Form", "Search"))


        self.Button.clicked.connect(self.find_path)
        self.exit.clicked.connect(self.logoff)

    def selectionchange(self,i):
        self.viewscene=GRview(self.map)
        Qpix=QtGui.QPixmap(self.Listcity.currentText()+".png")
        self.viewscene.addPixmap(Qpix)
        self.map.setScene(self.viewscene)
        self.map.scale(0.4,0.4)

  
    def find_path(self):
        command=self.Button.text()

        cityname=self.Listcity.currentText()
        start=self.start.text()
        goal=self.goal.text()
    
        
        if command=="Search":

            
            result = path_find.search(cityname,start,goal,0)
            layout = QtWidgets.QFormLayout()
            while len(result) >4:
                layout.addRow("",QtWidgets.QLabel(str(result[0:4])))
                result=result[4:]
            layout.addRow("",QtWidgets.QLabel(str(result)))
            self.tab1.setLayout(layout)

            result = path_find.search(cityname,start,goal,1)
            layout = QtWidgets.QFormLayout()
            while len(result) >4:
                layout.addRow("",QtWidgets.QLabel(str(result[0:4])))
                result=result[4:]
            layout.addRow("",QtWidgets.QLabel(str(result)))
            self.tab2.setLayout(layout)

            self.tab1.setLayout(layout)
            
            self.Button.setText("Clear")
        else:
            layout = QtWidgets.QFormLayout()
            layout.addRow("",QtWidgets.QLabel(""))
            self.Button.setText("Search")
            
    def logoff(self):
        try:            
            with sqlite3.connect("Userinfo.db") as db:
                cursor = db.cursor()
                sql = "DROP TABLE Current;"
                cursor.execute(sql)
        except:
            pass
        
        os.popen("python login.py")
        QCoreApplication.quit()
def main():
    app = QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    main=Ui_Form()
    main.setupUi(w)
    
    w.show()
    sys.exit(app.exec_())

