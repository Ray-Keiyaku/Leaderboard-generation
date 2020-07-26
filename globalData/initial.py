import os
import shutil
import sys

from Leaderboard.write import init_database
from globalData import data


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def init_all():
    folder = os.path.exists(data.TOP_PATH)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(data.TOP_PATH)
    init_database()
    files_tmp = os.listdir(data.TOP_PATH)  # 得到文件夹下的所有文件名称
    files = []
    for file in files_tmp:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            files.append(file)
    for file in data.res.values():
        if file not in files:
            filename = resource_path(os.path.join("Resource", file))
            shutil.copyfile(filename, os.path.join(data.TOP_PATH, file))


