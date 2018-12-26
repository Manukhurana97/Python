import mysql.connector

class database:

    def __init__(self):

        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='python'
        )
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute('CREATE TABLE  IF NOT EXISTS BOOKRECORD(id INTEGER AUTO_INCREMENT,PRIMARY KEY(id),Name varchar(50),Title varchar(50),Edition varchar(50),ISBN varchar(50))')
        self.mydb.commit()


    def insert(self,name, title, edition, isbn):
        sql='INSERT INTO BOOKRECORD(Name,Title,Edition,ISBN) values(%s,%s,%s,%s)'
        val=(name, title, edition, isbn)
        self.mycursor.execute(sql, val)
        self.mydb.commit()



    def  search_all(self):
        self.mycursor.execute('SELECT * FROM BOOKRECORD')
        rows=self.mycursor.fetchall()
        return rows



    def delete(self,isbn):
        sql="delete from bookrecord where ISBN=%s"
        val=(isbn)
        print(val)
        self.mycursor.execute(sql,(val,))
        self.mydb.commit()




    def update(self,a,name, title, edition, isbn):
        sql='UPDATE BOOKRECORD SET Name=%s,Title=%s,Edition=%s,ISBN=%s where ISBN=%s'
        var = (name, title, edition, isbn,a)
        self.mycursor.execute(sql,var)
        self.mydb.commit()

    def __del__(self):
        self.mydb.close()