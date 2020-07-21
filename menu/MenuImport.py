import time
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

from Leaderboard.importAndexport import get_import, import_table_out
from Leaderboard.read import get_table_content
from Leaderboard.write import insert_to_table
from globalData import data


class MenuImport(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('数据导入')
        # self.geometry('1000x600')

        # 数据
        self.data = get_table_content(table_now)
        self.content = []
        self.content_error = []
        self.table_now = table_now
        self.path = tk.StringVar()
        self.path.set("未选择")

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        # Message
        frame_lab = tk.Frame(self)
        lab_message = tk.Label(frame_lab, text="当前选择文件：", font=(data.DISPLAY_FONT, 15))
        lab_message.grid(row=0, column=0, sticky=tk.W)
        lab_path = tk.Label(frame_lab, textvariable=self.path, font=(data.DISPLAY_FONT, 15), width=40, anchor=tk.NW)
        lab_path.grid(row=0, column=1, sticky=tk.W)
        frame_lab.grid(row=0, column=0, sticky=tk.W)

        # Content
        from menu.MenuMain import ContentAll
        content = ContentAll(self, self.content, 10)
        content.grid(row=1, column=0, columnspan=12, sticky=tk.W)

        lab_message2 = tk.Label(self, text="以下是无法导入的错误信息：", font=(data.DISPLAY_FONT, 15))
        lab_message2.grid(row=2, column=0, sticky=tk.W)

        # Error Content
        content_error = ContentAll(self, self.content_error, 10)
        content_error.grid(row=3, column=0, columnspan=12, sticky=tk.W)

        # button
        frame_button = tk.Frame(self)
        button_select = tk.Button(frame_button, text='选择导入文件', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                  command=self.select)
        button_select.grid(row=0, column=0, sticky=tk.W, padx=15, pady=10)
        button_refresh = tk.Button(frame_button, text='刷新', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                   command=self.refresh)
        button_refresh.grid(row=0, column=1, sticky=tk.W, padx=15, pady=10)
        button_import = tk.Button(frame_button, text='导入', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                  command=self.importTable)
        button_import.grid(row=0, column=2, sticky=tk.W, padx=15, pady=10)
        button_get = tk.Button(frame_button, text='获取导入模板', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                               command=self.getImportTable)
        button_get.grid(row=0, column=3, sticky=tk.W, padx=15, pady=10)
        button_back = tk.Button(frame_button, text='返回', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                command=self.back)
        button_back.grid(row=0, column=4, sticky=tk.W, padx=15, pady=10)
        frame_button.grid(row=4, column=0, columnspan=12, sticky=tk.W)

    def select(self):
        input_path = askopenfilename(parent=self, filetypes=[('Excel 表格', '*.xlsx')])
        if input_path:
            self.path.set(input_path)
            self.refresh()

    def refresh(self):
        if self.path.get() == "未选择":
            return
        self.data = get_table_content(self.table_now)
        self.content, self.content_error = get_import(self.path.get(), self.data)
        self.setup_UI()
        self.grab_set()

    def importTable(self):
        if len(self.content) != 0:
            for line in self.content:
                insert_to_table(self.table_now, line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                                line[7], line[8], line[9])
            tk.messagebox.showinfo('成功', '导入成功！')
            self.refresh()

    def getImportTable(self):
        cur_time = time.strftime("%Y-%m-%d", time.localtime())
        default_name = "排行榜生成器数据导入模板" + cur_time
        input_path = asksaveasfilename(parent=self, defaultextension="xlsx",
                                       filetypes=[('Excel 表格', '*.xlsx')], initialfile=default_name)
        if input_path:
            if not import_table_out(input_path):
                tk.messagebox.showerror('错误', '路径非法或文件未关闭，请重试！')
            else:
                tk.messagebox.showinfo('成功', '数据导入模板生成成功！')

    def back(self):
        self.destroy()  # 销毁窗口
