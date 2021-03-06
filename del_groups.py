# Copyright 2015 Belkin Alexey Igorevich
# Licensed under the Apache License, Version 2.0

from PySide import QtCore, QtGui

class Del_Groups(object):
    def __init__(self):
        super(Del_Groups, self).__init__()
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
        self.btn_OK.clicked.connect(self.Delete)

    def retranslateUi(self, Form_Groups):
        Form_Groups.setWindowTitle(QtGui.QApplication.translate("Form_Groups", "Delete Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_OK.setText(QtGui.QApplication.translate("Form_Groups", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Form_Groups", "Close", None, QtGui.QApplication.UnicodeUTF8))

