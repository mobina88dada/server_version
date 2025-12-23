import mysql.connector
from config import db_config


database_name=db_config['database']

def insert_student_data(mathp, chemistryp, physicsp, rate, cid):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    SQL_QUERY="INSERT IGNORE INTO STUDENT (MATHP, CHEMISTRYP, PHYSICSP, RATE, CID )VALUES (%s, %s, %s, %s, %s);"
    cur.execute(SQL_QUERY, (mathp, chemistryp, physicsp, rate, cid))
    conn.commit()
    return True



def insert_uni_data(code, major, university, cid_pass, capacity=None, last_rate=None):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    SQL_QUERY="INSERT INTO UNI (CODE, MAJOR, CITY, CID_PASS, CAPACITY, LAST_RATE) VALUES (%s, %s, %s, %s, %s, %s);"
    cur.execute (SQL_QUERY, (code, major, university, cid_pass, capacity, last_rate))
    conn.commit()
    return True


