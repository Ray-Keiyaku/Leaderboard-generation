import sqlite3

from globalData import data


def get_table_name():
    conn = sqlite3.connect(data.DATA_PATH)  # 链接数据库
    cur = conn.cursor()  # 创建游标cur来执行SQL语句

    # 获取表名
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    Tables = cur.fetchall()
    # print(Tables)
    return Tables


def get_table_content(table_name):
    content_list = []
    conn = sqlite3.connect(data.DATA_PATH)  # 链接数据库
    cur = conn.cursor()  # 创建游标cur来执行SQL语句
    cur.execute("SELECT * FROM {}".format(table_name))
    content_list.append([item[0] for item in cur.description])
    cur.execute("SELECT NAME, TOTALPOINT from {} ORDER BY TOTALPOINT DESC".format(table_name))
    for row in cur:
        content_list.append([row[0], row[1]])
    # print(content_list)
    return content_list

# get_table_content("动漫")
