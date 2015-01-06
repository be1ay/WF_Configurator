# 2014 September A.I.Belkin
import sys
from PySide import QtGui, QtCore

from connectBD import *

f=open('sql.txt')
tmp=f.read().split('\n')
sqlServer=tmp[0]
BDname=tmp[1]

# idGroups={} #словарь с группами
class Add_Groups(QtGui.QWidget):
    def __init__(self,list_groups):
        super(Add_Groups, self).__init__()
        self.initUI()
        self.list_groups.addItems(list_groups)
               
    def initUI(self): 
        self.setWindowTitle('Add Groups')
        self.resize(356, 265)
        self.gridLayout_2 = QtGui.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.list_groups = QtGui.QListWidget(self)
        self.list_groups.setObjectName("list_groups")
        self.gridLayout.addWidget(self.list_groups, 0, 0, 1, 2)
        self.btn_OK = QtGui.QPushButton('OK',self)
        self.btn_OK.setObjectName("btn_OK")
        self.gridLayout.addWidget(self.btn_OK, 1, 0, 1, 1)
        self.btn_cancel = QtGui.QPushButton('Cancel',self)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        # Bindings
        self.btn_cancel.clicked.connect(self.Cancel)
        self.btn_OK.clicked.connect(self.OK)

        self.show()
    
    @QtCore.Slot()
    def OK(self):
        self.close()
    @QtCore.Slot()
    def Cancel(self):
        self.close()

class MyWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
               
    def initUI(self):               
#---------------------------------------------------------------------gui    
        # self.setGeometry(667, 667, 250, 250)
        self.resize(665, 543)        
        self.setWindowTitle('My WorkFlow Configurator')

        self.treeWid = QtGui.QTreeWidget(self)
        self.treeWid.setGeometry(QtCore.QRect(310, 10, 341, 511))
        self.treeWid.setObjectName("treeWid")
        self.treeWid.setColumnCount(1)
        self.treeWid.setHeaderLabels([''])
        self.listFIO = QtGui.QListWidget(self)
        self.listFIO.setGeometry(QtCore.QRect(20, 140, 270, 91))
        self.listFIO.setObjectName("listFIO")
        self.listRoles = QtGui.QListWidget(self)
        self.listRoles.setGeometry(QtCore.QRect(20, 280, 270, 131))
        self.listRoles.setObjectName("listRoles")
        self.btn_insert = QtGui.QPushButton('INSERT',self)
        self.btn_insert.setGeometry(QtCore.QRect(100, 240, 91, 31))
        self.btn_insert.setObjectName("btn_insert")
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(30, 20, 270, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel('SQL Server',self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txt_server = QtGui.QLineEdit(sqlServer,self.widget)
        self.txt_server.setObjectName("txt_server")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_server)
        self.label_2 = QtGui.QLabel('Database',self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txt_db = QtGui.QLineEdit(BDname,self.widget)
        self.txt_db.setObjectName("txt_db")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_db)
        self.horizontalLayout.addLayout(self.formLayout)
        self.btn_connect = QtGui.QPushButton('Connect',self.widget)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        self.widget1 = QtGui.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(30, 90, 216, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txt_s = QtGui.QLineEdit(self.widget1)
        self.txt_s.setObjectName("txt_s")
        self.horizontalLayout_2.addWidget(self.txt_s)
        self.btn_search = QtGui.QPushButton('Search',self.widget1)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.btn_search)

#---------bindings
        self.btn_search.clicked.connect(self.MySearchFio)
        self.btn_connect.clicked.connect(self.BDConnect)
        self.treeWid.itemDoubleClicked.connect(self.SelDep)
        self.btn_insert.clicked.connect(self.InsertUser)
        self.listFIO.itemClicked.connect(self.showGroups)
        # 21.10.2014 начал разработку контекстного меню для групп
        # ----было несколько пунктов контекстного меню оставил 1
        # lst=self.createActions()
        # self.listRoles.addActions(lst)
        # 06.01.2015
        lst=self.createActions()
        self.listRoles.addActions(lst)
        # lst.setEnabled(False)
        # ----
        # self.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        # self.listFIO.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listRoles.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
#---------------------------------
        self.show()
    def add_groups(self):
        conn=self.conn()
        rows=conn.getGroups()
        # список групп пользователя
        grlist=self.showGroups()
        # список всех групп
        list_groups=[row[1] for row in rows]
        # создаем список групп которых нет у пользователя
        lst=[item for item in list_groups if item not in grlist]
        self.second_window = Add_Groups(lst)
 
    def del_groups(self):
        conn=self.conn()
        rows=conn.getGroups()
        # список групп пользователя
        grlist=self.showGroups()
        self.second_window = Add_Groups(grlist)
 
    # def paste(self):
    #     QtGui.QMessageBox.information(self, 'Сообщение', 'PASTE!')
    def createActions(self):
        self.Add = QtGui.QAction("Add", self,
                triggered=self.add_groups)
 
        self.Delete = QtGui.QAction("Delete", self,
                triggered=self.del_groups)
 
        # self.pasteAct = QtGui.QAction("Paste", self,
        #         triggered=self.paste)
        # return (self.cutAct,self.copyAct,self.pasteAct)
        return (self.Add,self.Delete)
    # def contextMenuEvent(self, event):
    #     menu = QtGui.QMenu(self)
    #     menu.addAction(self.cutAct)
    #     menu.addAction(self.copyAct)
    #     menu.addAction(self.pasteAct)
    #     menu.exec_(event.globalPos())
        

    @QtCore.Slot()
    def showGroups(self):
        self.listRoles.clear()
        conn=self.conn()
        s=self.listFIO.currentItem ().text().split(' : ')
        rows=conn.selectFio2(s[1])
        
        # lst.setEnabled(True)
        # Рабочий код переделал
        # rows=conn.getUserGroups(str(rows[0][0]))
        # for row in rows:
        #     self.listRoles.addItem(idGroups[row[0]])
        rows=conn.getUserGroups(str(rows[0][0]))
        grlist=[row[1] for row in rows]
        # for row in rows:
        #     glist.addItem(row[1])

            # self.listRoles.addItem(row[1])
        self.listRoles.addItems(grlist)
        return grlist

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
        rows=conn.selectFio(self.txt_s.text())
        for row in rows:
            self.listFIO.addItem(str(row[0])+' : '+row[1])#str(row[0])- id
    
    @QtCore.Slot()
    def BDConnect(self):
        conn=self.conn()
        if(conn.ConnectDB()):
            self.BD_Connected()
            self.treeRoot()
            # Рабочий код с группами
            # ----------------------
            # global idGroups
            # conn=self.conn()
            # rows=conn.getGroups() # получаем список групп которые есть в базе и сохраняем в словарь
            # for row in rows:
            #     idGroups[row[0]]=row[1]

            # ----------------------
            self.btn_search.setEnabled(True)
            

            # self.second_window = Ui_Form_Groups()
            
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
  
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()