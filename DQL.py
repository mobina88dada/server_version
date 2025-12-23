import mysql.connector
from config import db_config

database_name=db_config['database']

def get_uni_data(cid_pass):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    SQL_QUERY="select * from uni where cid_pass = %s;"
    cur.execute(SQL_QUERY, (cid_pass,))
    info = cur.fetchall()[0]
    cur.close()
    conn.close()
    return info
