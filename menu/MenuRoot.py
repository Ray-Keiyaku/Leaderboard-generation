# -*- coding: utf-8 -*-
# author: Ray

import tkinter as tk

from Leaderboard.backupAndrestore import backUp, restore
from globalData import data
from menu.MenuAskTable import MenuAskTable
from menu.MenuMain import MenuMain


class MenuRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('可视化排行榜生成器')
        # self.geometry('500x600')
        # 程序界面
        self.setupUI()

    def setupUI(self):
        lab_message = tk.Label(self, text=data.SOFT_INFO, font=(data.DISPLAY_FONT, 15))
        # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
        lab_message.grid(row=0, column=0, sticky=tk.W)  # Label内容content区域放置位置，自动调节尺寸

        button_entry = tk.Button(self, text='选择排行榜', font=(data.DISPLAY_FONT, 15), width=15, height=1,
                                 command=self.set_Table)
        button_entry.grid(row=1, column=0, sticky=tk.W, padx=80, pady=20)
        button_backUp = tk.Button(self, text='数据备份', font=(data.DISPLAY_FONT, 15), width=15, height=1,
                                  command=self.data_backUp)
        button_backUp.grid(row=2, column=0, sticky=tk.W, padx=80, pady=20)
        button_restore = tk.Button(self, text='数据恢复', font=(data.DISPLAY_FONT, 15), width=15, height=1,
                                   command=self.data_restore)
        button_restore.grid(row=3, column=0, sticky=tk.W, padx=80, pady=20)
        button_exit = tk.Button(self, text='退出', font=(data.DISPLAY_FONT, 15), width=15, height=1,
                                command=self.exit_window)
        button_exit.grid(row=4, column=0, sticky=tk.W, padx=80, pady=20)

    def set_Table(self):
        # 接收弹窗的数据
        res = self.ask_table_name()
        # print(res)
        if res is None:
            return
        # print(res)
        mainDialog = MenuMain(res)
        self.wait_window(mainDialog)

    def ask_table_name(self):
        inputDialog = MenuAskTable()

        self.wait_window(inputDialog)  # 这一句很重要！！！

        return inputDialog.table_name

    def data_backUp(self):
        a = tk.messagebox.askokcancel('警告:', '建立备份将覆盖原备份！\n确定要新建备份吗？')
        if a:
            backUp()
            tk.messagebox.showinfo('成功', '备份成功！')

    def data_restore(self):
        a = tk.messagebox.askokcancel('警告:', '恢复数据将覆盖现有数据！\n确定要恢复数据吗？')
        if a:
            restore()
            tk.messagebox.showinfo('成功', '恢复成功！')

    def exit_window(self):
        self.destroy()
