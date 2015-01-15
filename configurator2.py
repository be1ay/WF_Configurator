# Copyright 2015 Belkin Alexey Igorevich
# Licensed under the Apache License, Version 2.0
import sys
from PySide import QtGui, QtCore
from MainWindow import MyMainWindow
from add_groups import Add_Groups
from del_groups import Del_Groups

from connectBD import *

f=open('sql.txt')
tmp=f.read().split('\n')
sqlServer=tmp[0]
BDname=tmp[1]

def conn(self):
    conn=Connection(sqlServer,BDname)
    return conn
class AddWindow(QtGui.QWidget,Add_Groups):
    def __init__(self,list_groups,uId,parent=None):
        QtGui.QWidget.__init__(self,parent)
        # self.l_groups=list_groups
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.uId=uId
        self.parent=parent
        self.setupUi(self)
        self.move(parent.geometry().center()-self.rect().center()-QtCore.QPoint(4,30))
        self.list_groups.addItems(list_groups)
    @QtCore.Slot()
    def Add(self):
        global conn
        cnn=conn(self)
        # print(self.list_groups.currentItem ().text())
        grId=cnn.getGroupId(self.list_groups.currentItem ().text())
        cnn.insertUserGroup(str(grId[0][0]),str(self.uId))
        # print(grId[0][0])
        # self.close()
        self.list_groups.takeItem(self.list_groups.currentRow ())
        # self.parent.listRoles.repaint()
        self.parent.showGroups()
    @QtCore.Slot()
    def Cancel(self):
        self.close()

class DeleteWindow(QtGui.QWidget,Del_Groups):
    def __init__(self,list_groups,uId,parent=None):
        QtGui.QWidget.__init__(self,parent)
        # self.l_groups=list_groups
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.uId=uId
        self.parent=parent
        self.setupUi(self)
        self.move(parent.geometry().center()-self.rect().center()-QtCore.QPoint(4,30))
        self.list_groups.addItems(list_groups)
    @QtCore.Slot()
    def Delete(self):
        global conn
        cnn=conn(self)
        # print(self.list_groups.currentItem ().text())
        grId=cnn.getGroupId(self.list_groups.currentItem ().text())
        cnn.deleteUserGroup(str(grId[0][0]),str(self.uId))
        # print(grId[0][0])
        self.list_groups.takeItem(self.list_groups.currentRow ())
        self.parent.showGroups()
        # self.close()
    @QtCore.Slot()
    def Cancel(self):
        self.close()

class MyWindow(QtGui.QWidget,MyMainWindow):
    def __init__(self, parent=None):
         QtGui.QWidget.__init__(self)
         self.setupUi(self)
         self.txt_server.setText(sqlServer)
         self.txt_db.setText(BDname)
 
    def add_groups(self):
        conn=self.conn()
        rows=conn.getGroups()
        # список групп пользователя
        grlist,uId=self.showGroups()
        # список всех групп
        list_groups=[row[1] for row in rows]
        # создаем список групп которых нет у пользователя
        lst=[item for item in list_groups if item not in grlist]
        # self.second_window = SecondWindow()
        self.second_window = AddWindow(lst,uId,self)
        self.second_window.show()

    def del_groups(self):
        conn=self.conn()
        rows=conn.getGroups()
        # список групп пользователя
        grlist,uId=self.showGroups()
        self.third_window = DeleteWindow(grlist,uId,self)
        self.third_window.show()

    def createActions(self):
        self.Add = QtGui.QAction("Add", self,
                triggered=self.add_groups)
 
        self.Delete = QtGui.QAction("Delete", self,
                triggered=self.del_groups)
        return (self.Add,self.Delete)
    

    @QtCore.Slot()
    def showGroups(self):
        self.listRoles.clear()
        conn=self.conn()
        s=self.listFIO.currentItem ().text().split(' : ')
        # rows=conn.selectFio2(s[1])

        uId=conn.GetUserId(s[0])
        # print (uId)
        rows=conn.getUserGroups(str(uId))
        grlist=[row[1] for row in rows]
        self.listRoles.addItems(grlist)


        login=conn.GetLogin(s[0])
        login=str(uId)+' : '+str(login)
        self.label_5.setText(login)
        
        return grlist,uId

    @QtCore.Slot()
    def SelDep(self):
        self.tree2Click()

    @QtCore.Slot()
    def InsertUser(self):
        conn=self.conn()
        s=self.listFIO.currentItem ().text().split(' : ')
        if conn.InsertUser(s[0],self.treeWid.currentItem().text(1)):
            QtGui.QMessageBox.information(self, 'Сообщение', 'Пользователь успешно добавлен!')
        else:
            QtGui.QMessageBox.critical(self, 'Сообщение', 'Пользователь добавлен раньше!')

    
    @QtCore.Slot()
    def MySearchFio(self):
        self.listFIO.clear()
        conn=self.conn()
        rows=conn.selectFio(self.txt_fio.text())
        for row in rows:
            self.listFIO.addItem(str(row[0])+' : '+row[1])#str(row[0])- id
    
    @QtCore.Slot()
    def BDConnect(self):
        conn=self.conn()
        if(conn.ConnectDB()):
            self.BD_Connected()
            self.treeRoot()
            self.btn_search.setEnabled(True)
         
        else:
            self.BD_NotConnected()

    


    def tree2Click(self):# DoubleClick на подразделении
        conn=self.conn()
        SelectedItem=self.treeWid.currentItem()
        list1=conn.showSelectDep(SelectedItem.text(1))
        
        for i in SelectedItem.takeChildren(): # Удаляем если до этого разворачивали элемент
            SelectedItem.removeChild(i)

        for l in sorted(list1):
            itemId=str(l[0])
            descr=str(l[1])
            parent=str(l[2])
            treeItem=QtGui.QTreeWidgetItem([descr,itemId,parent])
            SelectedItem.removeChild(treeItem)
            SelectedItem.addChild(treeItem)



    def treeRoot(self):
        conn=self.conn()
        list1=conn.showStruct()
        treeItems=[]
        self.treeWid.clear()
#-----------------------------------
        for l in sorted(list1):
            itemId=str(l[0])
            descr=str(l[1])
            parent=str(l[2])
            treeItem=QtGui.QTreeWidgetItem([descr,itemId,parent])
            treeItems.append(treeItem)

        treeItemsFin=[]# формируем дерево
        i=1
        for item in treeItems:
            for itemj in treeItems[i:]:
                if item.text(1)==itemj.text(2):
                    item.addChild(itemj)
            i+=1
            treeItemsFin.append(item)
#--------------------------------------

        self.treeWid.insertTopLevelItems(0,treeItemsFin)


    def conn(self):
        global sqlServer,BDname
        (sqlServer,BDname)=(self.txt_server.text(),self.txt_db.text())
        conn=Connection(sqlServer,BDname)
        return conn

    def BD_Connected(self):
        QtGui.QMessageBox.information(self, 'Message', 'Connection success!')

    def BD_NotConnected(self):
        QtGui.QMessageBox.information(self, 'Message', 'No connection!')

    def closeEvent(self, event):
        f=open('sql.txt','w')
        f.write(sqlServer+'\n'+BDname)
        f.close()
  
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MyWindow()
    main_window.show()
    sys.exit(app.exec_())