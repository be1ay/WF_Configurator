# 2014 September A.I.Belkin
import pypyodbc

class Connection(object):
    """docstring for Connection"""
    def __init__(self, sqlServer,BDname):
        super(Connection, self).__init__()
        self.cnxn = None
        self.cursor=None
        self.sqlServer=sqlServer
        self.BDname=BDname

    def get_cursor(self):
        return self.cursor
    def set_cursor(self,cursor):
        self.cursor=cursor
    def get_cnxn(self):
        return self.cnxn
    def set_cnxn(self,cnxn):
        self.cnxn=cnxn  

    def showSelectDep(self,idDep):
        self.ConnectDB()
        cursor=self.get_cursor()
        cursor.execute("select * from wfRoles where inIdDepartment = "+idDep)
        rows=cursor.fetchall()
        l=[]
        for row in rows:
            l.append([row[0],row[2],row[1]])
        return l

    def showStruct(self):
        self.ConnectDB()
        cursor=self.get_cursor()
        cursor.execute("select * from wfDepartments")
        rows=cursor.fetchall()
        l=[]
        for row in rows:
            l.append([row[0],row[1],row[2]])
        return l

    def ConnectDB(self):
        try:
            cnxn = pypyodbc.connect('DRIVER={SQL Server};SERVER='+self.sqlServer+';DATABASE='+self.BDname+';UID=Admin;PWD=P@ssword1')
            self.set_cursor(cnxn.cursor())
            self.set_cnxn(cnxn)
            return True
        except:
            return False
    def selectFio(self,name): # Поиск в БД
        self.ConnectDB()
        cursor=self.get_cursor()
        select=str("select * from wfActors where stDescription like '"+name+'%'+"' order by stDescription")
        cursor.execute(select)
        rows=cursor.fetchall()
        return rows

    def InsertUser(self,uId,roleId):
        self.ConnectDB()
        cnxn=self.get_cnxn()
        cursor=self.get_cursor()
        
        try:
            cursor.execute("insert into wfUserRoles values ("+uId+","+roleId+",null,null)")
            cnxn.commit()
            return True
        except:
            return False

