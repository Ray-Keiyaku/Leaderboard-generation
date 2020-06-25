import sqlite3

from globalData import data


def init_database():
    conn = sqlite3.connect(data.DATA_PATH)
    cur = conn.cursor()  # 创建游标cur来执行SQL语句
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    temp = cur.fetchall()
    Tables = [item[0] for item in temp]
    for tab in Tables:
        if tab not in data.INIT_LIST:
            conn.execute('''DROP TABLE \"{}\"'''.format(tab))

    if not set(data.INIT_LIST) > set(Tables):
        for tab in data.INIT_LIST:
            if tab not in Tables:
                conn.execute('''CREATE TABLE {}
                                (ID         INT     PRIMARY KEY     NOT NULL,
                                NAME        TEXT    NOT NULL    UNIQUE,
                                PicStyle    INT     NOT NULL,
                                PicQuality  INT     NOT NULL,
                                Music       INT     NOT NULL,
                                Voice       INT     NOT NULL,
                                Setting     INT     NOT NULL,
                                Plot        INT     NOT NULL,
                                Character   INT     NOT NULL,
                                TotalPoint  REAL     NOT NULL,
                                Recommend   REAL     NOT NULL);'''.format(tab))


def insert_to_table(table_now, v_NAME, v_PicStyle, v_PicQuality, v_Music, v_Voice, v_Setting, v_Plot, v_Character):
    pass
