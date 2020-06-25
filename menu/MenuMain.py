import tkinter as tk
from tkinter import END, DISABLED
from Leaderboard.read import get_table_content
from menu.MenuInsert import MenuInsert


class MenuMain(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('排行榜控制中心')
        self.geometry('1000x600')

        # 数据
        self.data = get_table_content(table_now)
        self.table_now = table_now

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        # ID
        content = tk.Text(self, font=('Arial', 12), height=20, width=4)
        for item in self.data:
            content.insert(END, item[0])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=0, sticky=tk.W)

        # NAME
        content = tk.Text(self, font=('Arial', 12), height=20, width=25)
        for item in self.data:
            content.insert(END, item[1])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=1, sticky=tk.W)

        # PicStyle
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[2])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=2, sticky=tk.W)

        # PicQuality
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[3])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=3, sticky=tk.W)

        # Music
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[4])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=4, sticky=tk.W)

        # Voice
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[5])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=5, sticky=tk.W)

        # Setting
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[6])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=6, sticky=tk.W)

        # Plot
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[7])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=7, sticky=tk.W)

        # Character
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[8])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=8, sticky=tk.W)

        # TotalPoint
        content = tk.Text(self, font=('Arial', 12), height=20, width=8)
        for item in self.data:
            content.insert(END, item[9])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=9, sticky=tk.W)

        # Recommend
        content = tk.Text(self, font=('Arial', 12), height=20, width=10)
        for item in self.data:
            content.insert(END, item[10])
            content.insert(tk.INSERT, '\n')
        content.config(state=DISABLED)
        content.grid(row=0, column=10, sticky=tk.W)

        # button
        frame_button = tk.Frame(self)

        button_print = tk.Button(frame_button, text='打印排行', font=('Arial', 15), width=12, height=1, command=self.print)
        button_print.grid(row=0, column=0, sticky=tk.W, padx=15, pady=10)
        button_insert = tk.Button(frame_button, text='插入新项目', font=('Arial', 15), width=12, height=1, command=self.insert)
        button_insert.grid(row=0, column=1, sticky=tk.W, padx=15, pady=10)
        button_insert = tk.Button(frame_button, text='修改项目', font=('Arial', 15), width=12, height=1, command=self.change)
        button_insert.grid(row=0, column=2, sticky=tk.W, padx=15, pady=10)
        button_insert = tk.Button(frame_button, text='删除项目', font=('Arial', 15), width=12, height=1, command=self.delete)
        button_insert.grid(row=0, column=3, sticky=tk.W, padx=15, pady=10)
        button_back = tk.Button(frame_button, text='返回', font=('Arial', 15), width=12, height=1, command=self.back)
        button_back.grid(row=0, column=4, sticky=tk.W, padx=15, pady=10)

        frame_button.grid(row=1, column=0, columnspan=11, sticky=tk.W)

    def print(self):
        self.destroy()

    def insert(self):
        MenuInsert(self.table_now)
        # self.destroy()

    def change(self):
        self.destroy()

    def delete(self):
        self.destroy()

    def back(self):
        self.destroy()  # 销毁窗口
