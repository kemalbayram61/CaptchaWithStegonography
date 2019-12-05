import sqlite3

class dbOperations:
    database=''
    databaseName=''
    im=''
    def __init__(self,databaseName):
        self.databaseName=databaseName
        self.initializeConnection()
        
    def initializeConnection(self):
        self.database=sqlite3.connect(self.databaseName)

    def executeQuery(self,query):
        self.im=self.database.cursor()
        self.im.execute(query)
        self.database.commit()
        return self.im

class UserOperations:
    databaseName=''
    database=''
    query=''
    def __init__(self,databaseName):
        self.databaseName=databaseName
        self.database=dbOperations(self.databaseName)

    def addUser(self,tcNumber,firstName,lastName,birthday,password,address):
        self.query="insert into users (tcNumber,firstName,lastName,password,birthday,address) values (\""+tcNumber+"\",\""+firstName+"\",\""+lastName+"\",\""+password+"\",\""+birthday+"\",\""+address+"\")"
        self.database.executeQuery(self.query)
        return True

    def updateUser(self,tcNumber,firstName,lastName,birthday,password,address):
        self.query="update users set firstName=\""+firstName+"\",lastName=\""+lastName+"\",tcNumber=\""+tcNumber+"\",birthday=\""+birthday+"\",password=\""+password+"\",address=\""+address+"\" where tcNumber=\""+tcNumber+"\""
        self.database.executeQuery(self.query)
        return True

    def dropUser(self,tcNumber):
        self.query="delete from users where tcNumber=\""+tcNumber+"\""
        self.database.executeQuery(self.query)
        return True

    def getUser(self,tcNumber):
        self.query="select * from users where tcNumber=\""+tcNumber+"\""
        return self.database.executeQuery(self.query).fetchall()

    def getUsers(self):
        self.query="select * from users"
        return self.database.executeQuery(self.query).fetchall()

class imageOperations:
    databaseName=''
    database=''
    query=''
    def __init__(self,databaseName):
        self.databaseName=databaseName
        self.database=dbOperations(self.databaseName)

    def addImage(self,imageID,filePath,imageName,objectFrames):
        self.query="insert into images values("+(str)(imageID)+",\""+filePath+"\",\""+imageName+"\",\""+objectFrames+"\")"
        self.database.executeQuery(self.query)
        return True

    def dropImage(self,imageID):
        self.query="delete from images where imageID="+(str)(imageID)+""
        self.database.executeQuery(self.query)
        return True

    def updateImage(self,lastImageId,filePath):
        self.query="update images set imageID="+(str)(lastImageId)+",filePath=\""+filePath+"\" where imageID="+(str)(lastImageId)+""
        self.database.executeQuery(self.query)
        return True

    def getImage(self,imageID):
        self.query="select * from images where imageID="+(str)(imageID)+""
        return self.database.executeQuery(self.query).fetchall()

    def getImages(self):
        self.query="select * from images"
        return self.database.executeQuery(self.query).fetchall()

class QuestionOperations:
    databaseName=''
    database=''
    query=''
    def __init__(self,databaseName):
        self.databaseName=databaseName
        self.database=dbOperations(self.databaseName)

    def addQuestion(self,questionID,question):
        self.query="insert into questions values ("+(str)(questionID)+",\""+question+"\")"
        self.database.executeQuery(self.query)
        return True

    def dropQuestion(self,questionID):
        self.query="delete from questions where questionID="+(str)(questionID)+""
        self.database.executeQuery(self.query)
        return True

    def getQuestion(self,questionID):
        self.query="select * from questions where questionID="+(str)(questionID)+""
        return self.database.executeQuery(self.query).fetchall()

    def updateQuestions(self,questionID,question):
        self.query="update questions set questionID="+(str)(questionID)+",question=\""+question+"\" where questionID="+(question)(questionID)+""
        self.database.executeQuery(self.query)
        return True

    def getQuestions(self):
        self.query="select * from questions"
        return self.database.executeQuery(self.query).fetchall()

    def getQuestionID(self,question):
        self.query="select * from questions where question=\""+(str)(question)+"\""
        return self.database.executeQuery(self.query).fetchall()[0][0]

class AnswerOperations:
    databaseName=''
    database=''
    query=''
    def __init__(self,databaseName):
        self.databaseName=databaseName
        self.database=dbOperations(self.databaseName)

    def addAnswer(self,questionID,userTc,answer):
        self.query="insert into answewrs values("+(str)(questionID)+",\""+userTc+"\",\""+answer+"\")"
        self.database.executeQuery(self.query)
        return True

    def dropAnswer(self,answerID,userTc):
        self.query="delete from answewrs where userTc=\""+userTc+"\" and answerID="+(str)(answerID)+""
        self.database.executeQuery(self.query)
        return True

    def updateAnswer(self,userTc,answerID,answer):
        self.query="update answewrs set answer=\""+answer+"\"  where userTc=\""+userTc+"\" and answerID="+(str)(answerID)+""
        self.database.executeQuery(self.query)
        return True

    def getAnswers(self,userTc):
        self.query="select * from answewrs where userTc="+(str)(userTc)+""
        return self.database.executeQuery(self.query).fetchall()
    



