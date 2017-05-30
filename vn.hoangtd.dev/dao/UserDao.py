class UserDao:

    #contructor
    def __init__(self, db):
        self.db = db;

    # create table 'userdto'....
    def createTableUser(self, user):
        self.db.execute("CREATE TABLE")

    # insert user to db
    def createUser(self, user):
        print "create"
        make_tab_user = self.db.prepare("INSERT INTO userdto VALUES ($1, $2)")

        with self.db.xact():
            make_tab_user(1,"sdadsa")
            make_tab_user(2, "sdadsa")
            make_tab_user(3, "sdadsa")

    def updateUser(self, user):
        print "update"
        update_tb_user = self.db.prepare("UPDATE tb_user SET name = $2 WHERE id = $1")

        with self.db.xact():
            update_tb_user(1, "whatever do you want put here, you can!")
            self.select()

    def getUser(self, user):
        print "get"
        select_tb_user = self.db.prepare("SELECT *FROM userdto")

        with self.db.xact():
            for row in select_tb_user():
                print row

    def deleteUser(self, user):
        print "delete"
        self.db.execute("DELETE FROM userdto WHERE id =$1")
