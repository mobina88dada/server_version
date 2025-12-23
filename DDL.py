import mysql.connector
from config import db_config
database_name=db_config['database']
def create_database(database_name):
    conn=mysql.connector.MySQLConnection(user=db_config['user'], password=db_config['password'], host=db_config['host'])
    cur=conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
    conn.commit()
    cur.close()
    print(f'database {database_name} created successfully')
def create_table_student():
    conn=mysql.connector.MySQLConnection(**db_config)
    cur=conn.cursor()
    cur.execute("""
                create table if not exists student (
                mathp         int not null,
                chemistryp    int not null,
                physicsp      int not null,
                rate          bigint unsigned not null,
                CID           bigint unsigned not null primary key
                );""")
    conn.commit()
    cur.close()
    conn.close()
    print(f' table student created successfully')
def create_table_uni():
    conn=mysql.connector.MySQLConnection(**db_config)
    cur=conn.cursor()
    cur.execute("""
                create table if not exists uni (
                code          int unsigned not null primary key,
                major         varchar(150) not null,
                city          varchar(150) not null,
                capacity      tinyint unsigned,
                last_rate     bigint unsigned not null,
                CID_pass      bigint unsigned not null,
                foreign key(CID_pass) references student(CID)
                );""")
    conn.commit()
    cur.close()
    conn.close()
    print(f' table uni created successfully')


if  __name__ == "__main__":
    create_database(database_name)
    create_table_student()
    create_table_uni()


