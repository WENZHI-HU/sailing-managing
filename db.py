

import pymysql
import hashlib
import Config as C

global conn
conn = None


# 01获取数据库连接
def conn_mysql():
    conn = None
    try:
        conn = pymysql.connect(host=C.DB_HOST, port=3306, user=C.DB_USER, password=C.DB_PASSWORD, db=C.DB_NAME,
                               charset='utf8')
    except Exception as e:
        print(e)
    return conn


# 02根据SQL语句操作数据库
def sql_execute(sql):
    global conn
    if conn is None:
        conn = conn_mysql()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    return result


# 03获取MD5加密结果
def md5(text):
    text = bytes(text, encoding='utf-8')
    return hashlib.md5(text).hexdigest()


if __name__ == "__main__":
    str_md5 = md5("123456")
    print('MD5加密后为 ：' + str_md5)
