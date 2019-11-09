import mysql.connector

class DatabaseManip():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        #
        # print(self.username)
        # print(self.password)

        self.dbaseInitializer()

    def dbaseInitializer(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin123",
            database="testdb"
        )

        self.myCursor = mydb.cursor()
        query_user_exists = "SELECT EXISTS(SELECT * FROM users WHERE username = %s)"
        self.myCursor.execute(query_user_exists,(self.username,))
        tuple_user_exists = self.myCursor.fetchone()
        total_user_exists = int(tuple_user_exists[0])

        if total_user_exists != 0:
            query_pass_validation = "SELECT password FROM users WHERE username = %s"
            self.myCursor.execute(query_pass_validation,(self.username,))
            __tuple_valid_pass = self.myCursor.fetchone()
            __password_validation = __tuple_valid_pass[0]

            if __password_validation == self.password:

                self.verdict = "correct"
            else:
                self.verdict = "incorrect"

        else:
            self.verdict = "notexist"

    def __str__(self):
        return self.verdict


    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password = password