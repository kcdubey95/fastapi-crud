from fastapi import FastAPI
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="college")
mycursor = mydb.cursor()
app = FastAPI()


@app.get("/")
def home():
    return "home"


@app.post("/insert_user")
def insert_user(user: dict):
    sql = "INSERT INTO users (fullname, mobileno, email_id, class) VALUES(%s, %s, %s, %s)"
    val = (user['fullname'], user['mobileno'], user['email_id'], user['class'])
    mycursor.execute(sql, val)
    mydb.commit()
    return "insert"


@app.get("/get-all")
def get_user():
    sql = "select * from users"
    mycursor.execute(sql)
    all_user = mycursor.fetchall()
    return all_user


@app.post("/update_user")
def update_user(userid: int, user: dict):
    sql = "update users set fullname= %s , mobileno=%s, email_id= %s,class=%s where id=%s"
    val = (user['fullname'], user['mobileno'], user['email_id'], user['class'], userid)
    mycursor.execute(sql, val)
    mydb.commit()
    return "Update Done"


@app.get("/delete-user")
def delete_user(userid: int):
    sql = "delete from users where id=%s"
    # val = (userid)
    mycursor.execute(sql, (userid,))
    mydb.commit()
    return "user delete"
