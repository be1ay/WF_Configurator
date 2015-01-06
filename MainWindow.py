# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form2.ui'
#
# Created: Tue Jan  6 16:50:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class MyMainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 436)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 100, 268, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.txt_fio = QtGui.QLineEdit(self.layoutWidget)
        self.txt_fio.setObjectName("txt_fio")
        self.horizontalLayout_2.addWidget(self.txt_fio)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.btn_search = QtGui.QPushButton(self.layoutWidget)
        self.btn_search.setEnabled(False)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_3.addWidget(self.btn_search)
        self.btn_insert = QtGui.QPushButton(Form)
        self.btn_insert.setGeometry(QtCore.QRect(120, 240, 91, 31))
        self.btn_insert.setObjectName("btn_insert")
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 308, 50))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txt_server = QtGui.QLineEdit(self.layoutWidget_2)
        self.txt_server.setObjectName("txt_server")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_server)
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txt_db = QtGui.QLineEdit(self.layoutWidget_2)
        self.txt_db.setObjectName("txt_db")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_db)
        self.horizontalLayout.addLayout(self.formLayout)
        self.btn_connect = QtGui.QPushButton(self.layoutWidget_2)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        self.listFIO = QtGui.QListWidget(Form)
        self.listFIO.setGeometry(QtCore.QRect(20, 140, 311, 91))
        self.listFIO.setObjectName("listFIO")
        self.treeWid = QtGui.QTreeWidget(Form)
        self.treeWid.setGeometry(QtCore.QRect(350, 10, 351, 401))
        self.treeWid.setObjectName("treeWid")
        self.treeWid.setColumnCount(1)
        self.treeWid.setHeaderLabels([''])
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(620, 410, 81, 20))
        self.label_4.setObjectName("label_4")
        self.listRoles = QtGui.QListWidget(Form)
        self.listRoles.setGeometry(QtCore.QRect(20, 280, 311, 131))
        self.listRoles.setObjectName("listRoles")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
#---------bindings
        self.btn_search.clicked.connect(self.MySearchFio)
        self.btn_connect.clicked.connect(self.BDConnect)
        self.treeWid.itemDoubleClicked.connect(self.SelDep)
        self.btn_insert.clicked.connect(self.InsertUser)
        self.listFIO.itemClicked.connect(self.showGroups)

        lst=self.createActions()
        self.listRoles.addActions(lst)

        self.listRoles.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "My Center for Loodsman", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(QtGui.QApplication.translate("Form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_insert.setText(QtGui.QApplication.translate("Form", "INSERT", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "SQL Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_connect.setText(QtGui.QApplication.translate("Form", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "2015 A.I.Belkin", None, QtGui.QApplication.UnicodeUTF8))
