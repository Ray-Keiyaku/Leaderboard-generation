import tkinter as tk
from tkinter.simpledialog import Listbox, END
from Leaderboard.read import get_table_name
from globalData import data


class MenuAskTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('选择排行榜：')
        # self.geometry('350x300')

        # 数据
        self.listbox = Listbox(self, width=30, font=(data.DISPLAY_FONT, 12))
        self.list_table = get_table_name()
        # self.list_table = [1,2,3,4]
        self.table_name = None

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        lab_hint = tk.Label(self, text='选择要进入的排行榜', font=(data.DISPLAY_FONT, 15))
        for item in self.list_table:
            self.listbox.insert(END, item[0])
        lab_hint.grid(row=0, column=0, sticky=tk.W)
        self.listbox.grid(row=1, column=0, columnspan=3)
        button_yes = tk.Button(self, text='确定', font=(data.DISPLAY_FONT, 15), width=10, height=1, command=self.confirm)
        button_yes.grid(row=3, column=0, sticky=tk.W, padx=15, pady=10)
        button_no = tk.Button(self, text='取消', font=(data.DISPLAY_FONT, 15), width=10, height=1, command=self.cancel)
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
