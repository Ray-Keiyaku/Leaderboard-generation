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

    if not set(Tables) > set(data.INIT_LIST):
        for tab in data.INIT_LIST:
            if tab not in Tables:
                conn.execute('''CREATE TABLE {}
                                (
                                NAME        TEXT    PRIMARY KEY     NOT NULL,
                                PicStyle    INT     NOT NULL,
                                PicQuality  INT     NOT NULL,
                                Music       INT     NOT NULL,
                                Voice       INT     NOT NULL,
                                Setting     INT     NOT NULL,
                                Plot        INT     NOT NULL,
                                Character   INT     NOT NULL,
                                TotalPoint  REAL     NOT NULL,
                                Recommend   REAL     NOT NULL);'''.format(tab))


def insert_to_table(table_now, v_NAME, v_PicStyle, v_PicQuality, v_Music, v_Voice, v_Setting, v_Plot, v_Character,
                    total_point, recommend_point):
    conn = sqlite3.connect(data.DATA_PATH)
    cur = conn.cursor()  # 创建游标cur来执行SQL语句
    cur.execute("INSERT INTO {tab} \
        VALUES ('{vn}', {vps}, {vpq}, {vm}, {vv}, {vs}, {vp}, {vc}, {vt}, {vr})"
                .format(tab=table_now, vn=v_NAME, vps=v_PicStyle, vpq=v_PicQuality,
                        vm=v_Music, vv=v_Voice, vs=v_Setting, vp=v_Plot, vc=v_Character,
                        vt=total_point, vr=recommend_point))
    conn.commit()


def change_to_table(table_now, v_NAME, v_PicStyle, v_PicQuality, v_Music, v_Voice, v_Setting, v_Plot, v_Character,
                    total_point, recommend_point):
    conn = sqlite3.connect(data.DATA_PATH)
    cur = conn.cursor()  # 创建游标cur来执行SQL语句
    cur.execute("UPDATE {tab} \
        SET PicStyle={vps},PicQuality={vpq},Music={vm},Voice={vv},Setting={vs},\
        Plot={vp},Character={vc},TotalPoint={vt},Recommend={vr} \
        WHERE NAME ='{vn}'".format(tab=table_now, vps=v_PicStyle, vpq=v_PicQuality,
                                   vm=v_Music, vv=v_Voice, vs=v_Setting, vp=v_Plot, vc=v_Character,
                                   vt=total_point, vr=recommend_point, vn=v_NAME))
    conn.commit()


def delete_to_table(table_now, v_NAME):
    conn = sqlite3.connect(data.DATA_PATH)
    cur = conn.cursor()  # 创建游标cur来执行SQL语句
    cur.execute("DELETE FROM {tab} WHERE NAME ='{vn}'".format(tab=table_now, vn=v_NAME))
    conn.commit()
