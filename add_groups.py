# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created: Tue Jan  6 13:38:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Add_Groups(object):
    def __init__(self):
        super(Add_Groups, self).__init__()
        # self.list_groups.addItems(list_groups)

    def setupUi(self, Form_Groups):
        Form_Groups.setObjectName("Form_Groups")
        Form_Groups.resize(356, 265)
        self.gridLayout_2 = QtGui.QGridLayout(Form_Groups)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.list_groups = QtGui.QListWidget(Form_Groups)
        self.list_groups.setObjectName("list_groups")
        self.gridLayout.addWidget(self.list_groups, 0, 0, 1, 2)
        self.btn_OK = QtGui.QPushButton(Form_Groups)
        self.btn_OK.setObjectName("btn_OK")
        self.gridLayout.addWidget(self.btn_OK, 1, 0, 1, 1)
        self.btn_cancel = QtGui.QPushButton(Form_Groups)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form_Groups)
        QtCore.QMetaObject.connectSlotsByName(Form_Groups)
        # Bindings
        self.btn_cancel.clicked.connect(self.Cancel)
        self.btn_OK.clicked.connect(self.OK)

    def retranslateUi(self, Form_Groups):
        Form_Groups.setWindowTitle(QtGui.QApplication.translate("Form_Groups", "Add Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_OK.setText(QtGui.QApplication.translate("Form_Groups", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Form_Groups", "Close", None, QtGui.QApplication.UnicodeUTF8))

