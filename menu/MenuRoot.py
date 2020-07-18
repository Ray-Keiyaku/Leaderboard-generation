# -*- coding: utf-8 -*-
# author: Ray

import tkinter as tk
from globalData import data
from menu.MenuAskTable import MenuAskTable
from menu.MenuMain import MenuMain


class MenuRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('可视化排行榜生成器')
        self.geometry('500x600')
        # 程序界面
        self.setupUI()

    def setupUI(self):
        lab_message = tk.Label(self, text=data.SOFT_INFO, font=(data.DISPLAY_FONT, 15))
        # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
        lab_message.grid(row=0, column=0, sticky=tk.W)  # Label内容content区域放置位置，自动调节尺寸

        button_entry = tk.Button(self, text='选择排行榜', font=(data.DISPLAY_FONT, 15), width=15, height=1, command=self.set_Table)
        button_entry.grid(row=1, column=2, sticky=tk.W, padx=30, pady=50)
        button_exit = tk.Button(self, text='退出', font=(data.DISPLAY_FONT, 15), width=15, height=1, command=self.exit_window)
        button_exit.grid(row=3, column=2, sticky=tk.W, padx=30, pady=50)

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

    def exit_window(self):
        self.destroy()

