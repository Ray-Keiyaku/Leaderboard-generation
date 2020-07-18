import sqlite3

from globalData import data


def backUp():
    conn = sqlite3.connect(data.DATA_PATH)
    with open(data.BACKUP_PATH, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()


def restore():
    conn = sqlite3.connect(data.DATA_PATH)
    cur = conn.cursor()
    # 清空数据库
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    temp = cur.fetchall()
    Tables = [item[0] for item in temp]
    for tab in Tables:
        conn.execute('''DROP TABLE \"{}\"'''.format(tab))
    # 从备份恢复数据
    with open(data.BACKUP_PATH, 'r') as f:
        content = f.read()
    content = content.split(';\n')
    for line in content:
        cur.execute(line+";")
    conn.close()
