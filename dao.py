import sqlite3
from models import data,user,login_user
from passlib.hash import bcrypt


def create_connection():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    return cursor,connection

def create_table():
    cursor,connection=create_connection()
    cursor.execute('create table if not exists usersdata (problem_name TEXT,topic TEXT,difficulty TEXT, entry_date date,user_id INTEGER)')
    connection.commit()
    connection.close()

create_table()

def insert_entries(data:data,email:str):
    cursor,connection=create_connection()
    user_id=get_user_id(email)
    placeholdersdata=(data.problem_name,data.topic,data.difficulty,data.entry_date,user_id)
    cursor.execute('insert into usersdata values (?,?,?,?,?)',placeholdersdata)
    connection.commit()
    connection.close()

def show_values():
    cursor,connection=create_connection()
    data=cursor.execute('select * from usersdata').fetchall()
    connection.close()
    return data

def filter_by_difficulty(difficulty:str):
    cursor,connection=create_connection()
    data= cursor.execute('select problem_name,topic,entry_date from usersdata where difficulty like ?',(difficulty,)).fetchall()
    connection.close()
    return data
    
def get_difficulty_count(email:str):
    cursor,connection=create_connection()
    userid=get_user_id(email)
    res=cursor.execute('select count(*),difficulty from usersdata where userid=? group by difficulty',(userid,)).fetchall()
    connection.close()
    return res

def create_user_table():
    cursor,connection=create_connection()
    cursor.execute('create table if not exists user (id Integer Primary key Autoincrement,name TEXT,email TEXT unique, password TEXT)')
    connection.commit()
    connection.close()

create_user_table()

def insert_user(user:user):
    try:
        cursor,connection=create_connection()
        hashed_pass = bcrypt.hash(user.password)
        cursor.execute('Insert into user(name, email, password) values(?,?,?)',(user.name,user.email,hashed_pass))
        connection.commit()
        return "success"
    except Exception as e:
        return "Email aldrready exists"
    finally:
        connection.close()

def login_user_dao(user:login_user):
    cursor,connection=create_connection()
    data=cursor.execute('Select * from user where email like ?',(user.email,)).fetchall()
    if not data:
        return None
    is_valid = bcrypt.verify(user.password, data[0][3])
    connection.close()
    if is_valid:
        return data
    return None

def get_user_id(email:str):
    cursor,connection=create_connection()
    id=cursor.execute('select id from user where email like ?',(email,)).fetchone()
    connection.close()
    return id[0]

def show_single_user_value(email:str):
    cursor,connection=create_connection()
    id=get_user_id(email)
    data=cursor.execute('select * from usersdata where userid=?',(id,)).fetchall()
    connection.close()
    return data

def piechartbytopic(email:str):
    cursor,connection=create_connection()
    userid=get_user_id(email)
    data=cursor.execute('select count(*),topic from usersdata where userid= ? group by topic',(userid,)).fetchall()
    connection.close()
    return data

def dates_user_active(email:str):
    cursor,connection=create_connection()
    userid=get_user_id(email)
    data=cursor.execute('select distinct entry_date from usersdata where userid=? order by entry_date asc',(userid,)).fetchall()
    connection.close()
    return data


