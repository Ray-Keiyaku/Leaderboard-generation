# -*- coding: utf-8 -*-
# author: Ray

import tkinter as tk
from tkinter.simpledialog import Listbox, END, DISABLED

from Leaderboard.read import get_table_name, get_table_content
from globalData import data


def exit_window():
    exit()


class MenuRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('可视化排行榜生成器')
        self.geometry('500x600')
        # 程序界面
        self.setupUI()

    def setupUI(self):
        lab_message = tk.Label(self, text=data.soft_info, font=('Arial', 15))
        # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
        lab_message.grid(row=0, column=0, sticky=tk.W)  # Label内容content区域放置位置，自动调节尺寸

        button_entry = tk.Button(self, text='选择排行榜', font=('Arial', 15), width=15, height=1, command=self.set_Table)
        button_entry.grid(row=1, column=2, sticky=tk.W, padx=30, pady=50)
        button_exit = tk.Button(self, text='退出', font=('Arial', 15), width=15, height=1, command=exit_window)
        button_exit.grid(row=3, column=2, sticky=tk.W, padx=30, pady=50)

    def set_Table(self):
        # 接收弹窗的数据
        res = self.ask_table_name()
        # print(res)
        if res is None:
            return
        # print(res)
        MenuMain(res)

    def ask_table_name(self):
        inputDialog = MenuAskTable()

        self.wait_window(inputDialog)  # 这一句很重要！！！

        return inputDialog.table_name


class MenuAskTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('选择排行榜：')
        self.geometry('350x300')

        # 数据
        self.listbox = Listbox(self, width=30, font=('Arial', 12))
        self.list_table = get_table_name()
        # self.list_table = [1,2,3,4]
        self.table_name = None

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        lab_hint = tk.Label(self, text='选择要进入的排行榜', font=('Arial', 15))
        for item in self.list_table:
            self.listbox.insert(END, item[0])
        lab_hint.grid(row=0, column=0, sticky=tk.W)
        self.listbox.grid(row=1, column=0, columnspan=3)
        button_yes = tk.Button(self, text='确定', font=('Arial', 15), width=10, height=1, command=self.confirm)
        button_yes.grid(row=3, column=0, sticky=tk.W, padx=15, pady=10)
        button_no = tk.Button(self, text='取消', font=('Arial', 15), width=10, height=1, command=self.cancel)
        button_no.grid(row=3, column=2, sticky=tk.W, padx=15, pady=10)

    def confirm(self):
        # print(self.listbox.curselection())
        table_select = self.listbox.curselection()  # 设置数据
        if table_select:
            # print(table_select)
            self.table_name = self.list_table[table_select[0]][0]
        self.destroy()  # 销毁窗口

    def cancel(self):
        self.destroy()


class MenuMain(tk.Toplevel):
    def __init__(self, Tablename):
        super().__init__()
        self.title('排行榜控制中心')
        self.geometry('800x600')

        # 数据
        self.data = get_table_content(Tablename)

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        # NAME
        content = tk.Text(self, font=('Arial', 15), height=20, width=25)
        print(self.data)
        for item in self.data:
            content.insert(END, item[0])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=0, sticky=tk.W)
        # TOTALPOINT
        content = tk.Text(self, font=('Arial', 15), height=20, width=15)
        print(self.data)
        for item in self.data:
            content.insert(END, item[1])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=1, sticky=tk.W)

        button_print = tk.Button(self, text='打印排行', font=('Arial', 15), width=10, height=1, command=self.confirm)
        button_print.grid(row=1, column=0, sticky=tk.W, padx=15, pady=10)
        button_insert = tk.Button(self, text='插入新项目', font=('Arial', 15), width=10, height=1, command=self.back)
        button_insert.grid(row=1, column=1, sticky=tk.W, padx=15, pady=10)
        button_back = tk.Button(self, text='返回', font=('Arial', 15), width=10, height=1, command=self.back)
        button_back.grid(row=1, column=2, sticky=tk.W, padx=15, pady=10)

    def confirm(self):
        self.destroy()  # 销毁窗口

    def back(self):
        self.destroy()


app = MenuRoot()
app.mainloop()
