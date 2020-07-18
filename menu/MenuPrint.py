import shutil
import tkinter as tk
import time
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
from Leaderboard.read import get_table_content
from Generator.print import print_table
from globalData import data


class MenuPrint(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('排行打印中心')
        # self.geometry('350x600')

        # 数据
        self.data = get_table_content(table_now)
        self.table_now = table_now
        print_table(table_now, self.data)
        image = Image.open(data.PICTURE_PATH)
        image = image.resize((350, 500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image)

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        preview = tk.Label(self, image=self.img, width=350, height=500)
        preview.grid(row=0, column=0)
        # button
        frame_button = tk.Frame(self)

        button_print = tk.Button(frame_button, text='打印排行', font=(data.DISPLAY_FONT, 15), width=12, height=1, command=self.print)
        button_print.grid(row=0, column=0, sticky=tk.W, padx=15, pady=10)
        button_back = tk.Button(frame_button, text='返回', font=(data.DISPLAY_FONT, 15), width=12, height=1, command=self.back)
        button_back.grid(row=0, column=1, sticky=tk.W, padx=15, pady=10)

        frame_button.grid(row=1, column=0)

    def print(self):
        cur_time = time.strftime("%Y-%m-%d", time.localtime())
        default_name = self.table_now + cur_time
        input_path = asksaveasfilename(parent=self, defaultextension="png",
                                       filetypes=[('图片', '*.png')], initialfile=default_name)
        # print(input_path)
        if input_path:
            shutil.copyfile(data.PICTURE_PATH, input_path)
        self.destroy()  # 销毁窗口

    def back(self):
        self.destroy()  # 销毁窗口
