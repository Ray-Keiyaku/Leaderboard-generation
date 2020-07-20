import time
import tkinter as tk
from tkinter import END, DISABLED
from tkinter.filedialog import asksaveasfilename

from Leaderboard.importAndexport import table_export
from Leaderboard.read import get_table_content
from globalData import data
from menu.MenuChange import MenuChange
from menu.MenuDelete import MenuDelete
from menu.MenuInsert import MenuInsert
from menu.MenuPrint import MenuPrint


class MenuMain(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('排行榜控制中心')
        # self.geometry('1000x600')

        # 数据
        self.data = get_table_content(table_now)
        self.table_now = table_now

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        # content
        content = ContentAll(self, self.data)
        content.grid(row=1, column=0, columnspan=12, sticky=tk.W)

        # button
        frame_button = tk.Frame(self)
        button_insert = tk.Button(frame_button, text='插入新项目', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                  command=self.insert)
        button_insert.grid(row=0, column=0, sticky=tk.W, padx=15, pady=10)
        button_change = tk.Button(frame_button, text='修改项目', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                  command=self.change)
        button_change.grid(row=0, column=1, sticky=tk.W, padx=15, pady=10)
        button_delete = tk.Button(frame_button, text='删除项目', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                  command=self.delete)
        button_delete.grid(row=0, column=2, sticky=tk.W, padx=15, pady=10)
        button_back = tk.Button(frame_button, text='返回', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                command=self.back)
        button_back.grid(row=0, column=3, sticky=tk.W, padx=15, pady=10)
        button_print = tk.Button(frame_button, text='打印排行', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                 command=self.print)
        button_print.grid(row=1, column=0, sticky=tk.W, padx=15, pady=10)
        button_importData = tk.Button(frame_button, text='导入数据', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                      command=self.importData)
        button_importData.grid(row=1, column=1, sticky=tk.W, padx=15, pady=10)
        button_exportData = tk.Button(frame_button, text='导出数据', font=(data.DISPLAY_FONT, 15), width=12, height=1,
                                      command=self.exportData)
        button_exportData.grid(row=1, column=2, sticky=tk.W, padx=15, pady=10)

        frame_button.grid(row=2, column=0, columnspan=12, sticky=tk.W)

    def print(self):
        insertDialog = MenuPrint(self.table_now)
        self.wait_window(insertDialog)
        self.update_data()

    def insert(self):
        insertDialog = MenuInsert(self.table_now)
        self.wait_window(insertDialog)
        self.update_data()

    def change(self):
        insertDialog = MenuChange(self.table_now)
        self.wait_window(insertDialog)
        self.update_data()

    def delete(self):
        insertDialog = MenuDelete(self.table_now)
        self.wait_window(insertDialog)
        self.update_data()

    def importData(self):
        pass

    def exportData(self):
        cur_time = time.strftime("%Y-%m-%d", time.localtime())
        default_name = self.table_now + cur_time
        input_path = asksaveasfilename(parent=self, defaultextension="xlsx",
                                       filetypes=[('表格', '*.xlsx')], initialfile=default_name)
        if input_path:
            if not table_export(input_path, self.table_now, self.data):
                tk.messagebox.showerror('错误', '路径非法或文件未关闭，请重试！')
            else:
                tk.messagebox.showinfo('成功', '数据导出成功！')

    def back(self):
        self.destroy()  # 销毁窗口

    def update_data(self):
        self.data = get_table_content(self.table_now)
        self.setup_UI()
        self.grab_set()


class ContentAll(tk.Frame):
    def __init__(self, master, table_data):
        tk.Frame.__init__(self, master)
        self.data = table_data

        # Title
        lab_RANK = tk.Label(self, text='排名', font=(data.DISPLAY_FONT, 12))
        lab_RANK.grid(row=0, column=0, sticky=tk.W, pady=5)
        lab_NAME = tk.Label(self, text='名称', font=(data.DISPLAY_FONT, 12))
        lab_NAME.grid(row=0, column=1, sticky=tk.W, pady=5)
        lab_PicStyle = tk.Label(self, text='画风', font=(data.DISPLAY_FONT, 12))
        lab_PicStyle.grid(row=0, column=2, sticky=tk.W, pady=5)
        lab_PicQuality = tk.Label(self, text='画质', font=(data.DISPLAY_FONT, 12))
        lab_PicQuality.grid(row=0, column=3, sticky=tk.W, pady=5)
        lab_Music = tk.Label(self, text='音乐', font=(data.DISPLAY_FONT, 12))
        lab_Music.grid(row=0, column=4, sticky=tk.W, pady=5)
        lab_Voice = tk.Label(self, text='语音', font=(data.DISPLAY_FONT, 12))
        lab_Voice.grid(row=0, column=5, sticky=tk.W, pady=5)
        lab_Setting = tk.Label(self, text='设定', font=(data.DISPLAY_FONT, 12))
        lab_Setting.grid(row=0, column=6, sticky=tk.W, pady=5)
        lab_Plot = tk.Label(self, text='剧情', font=(data.DISPLAY_FONT, 12))
        lab_Plot.grid(row=0, column=7, sticky=tk.W, pady=5)
        lab_Character = tk.Label(self, text='角色', font=(data.DISPLAY_FONT, 12))
        lab_Character.grid(row=0, column=8, sticky=tk.W, pady=5)
        lab_TotalPoint = tk.Label(self, text='总分', font=(data.DISPLAY_FONT, 12))
        lab_TotalPoint.grid(row=0, column=9, sticky=tk.W, pady=5)
        lab_Recommend = tk.Label(self, text='推荐', font=(data.DISPLAY_FONT, 12))
        lab_Recommend.grid(row=0, column=10, sticky=tk.W, pady=5)

        # RANK
        self.content_rank = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=5)
        # self.content_rank.insert(END, 'RANK')
        if len(self.data) > 0:
            for i in range(1, len(self.data) + 1):
                self.content_rank.insert(END, i)
                self.content_rank.insert(tk.INSERT, '\n')
        self.content_rank.config(state=DISABLED)
        self.content_rank.grid(row=1, column=0, sticky=tk.W)

        # NAME
        self.content_name = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=25, wrap=tk.NONE)
        for item in self.data:
            self.content_name.insert(END, item[0])
            self.content_name.insert(tk.INSERT, '\n')
        self.content_name.config(state=DISABLED)
        self.content_name.grid(row=1, column=1, sticky=tk.W)

        # PicStyle
        self.content_picStyle = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_picStyle.insert(END, item[1])
            self.content_picStyle.insert(tk.INSERT, '\n')
        self.content_picStyle.config(state=DISABLED)
        self.content_picStyle.grid(row=1, column=2, sticky=tk.W)

        # PicQuality
        self.content_picQuality = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_picQuality.insert(END, item[2])
            self.content_picQuality.insert(tk.INSERT, '\n')
        self.content_picQuality.config(state=DISABLED)
        self.content_picQuality.grid(row=1, column=3, sticky=tk.W)

        # Music
        self.content_music = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_music.insert(END, item[3])
            self.content_music.insert(tk.INSERT, '\n')
        self.content_music.config(state=DISABLED)
        self.content_music.grid(row=1, column=4, sticky=tk.W)

        # Voice
        self.content_voice = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_voice.insert(END, item[4])
            self.content_voice.insert(tk.INSERT, '\n')
        self.content_voice.config(state=DISABLED)
        self.content_voice.grid(row=1, column=5, sticky=tk.W)

        # Setting
        self.content_setting = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_setting.insert(END, item[5])
            self.content_setting.insert(tk.INSERT, '\n')
        self.content_setting.config(state=DISABLED)
        self.content_setting.grid(row=1, column=6, sticky=tk.W)

        # Plot
        self.content_plot = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_plot.insert(END, item[6])
            self.content_plot.insert(tk.INSERT, '\n')
        self.content_plot.config(state=DISABLED)
        self.content_plot.grid(row=1, column=7, sticky=tk.W)

        # Character
        self.content_character = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_character.insert(END, item[7])
            self.content_character.insert(tk.INSERT, '\n')
        self.content_character.config(state=DISABLED)
        self.content_character.grid(row=1, column=8, sticky=tk.W)

        # TotalPoint
        self.content_totalPoint = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=8)
        for item in self.data:
            self.content_totalPoint.insert(END, item[8])
            self.content_totalPoint.insert(tk.INSERT, '\n')
        self.content_totalPoint.config(state=DISABLED)
        self.content_totalPoint.grid(row=1, column=9, sticky=tk.W)

        # Recommend
        self.content_recommend = tk.Text(self, font=(data.DISPLAY_FONT, 12), height=20, width=10)
        for item in self.data:
            self.content_recommend.insert(END, item[9])
            self.content_recommend.insert(tk.INSERT, '\n')
        self.content_recommend.config(state=DISABLED)
        self.content_recommend.grid(row=1, column=10, sticky=tk.W)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=1, column=11, sticky=tk.E + tk.N + tk.S)

        # Changing the settings to make the scrolling work
        self.scrollbar['command'] = self.on_scrollbar
        self.content_rank['yscrollcommand'] = self.on_text_scroll
        self.content_name['yscrollcommand'] = self.on_text_scroll
        self.content_picStyle['yscrollcommand'] = self.on_text_scroll
        self.content_picQuality['yscrollcommand'] = self.on_text_scroll
        self.content_music['yscrollcommand'] = self.on_text_scroll
        self.content_voice['yscrollcommand'] = self.on_text_scroll
        self.content_setting['yscrollcommand'] = self.on_text_scroll
        self.content_plot['yscrollcommand'] = self.on_text_scroll
        self.content_character['yscrollcommand'] = self.on_text_scroll
        self.content_totalPoint['yscrollcommand'] = self.on_text_scroll
        self.content_recommend['yscrollcommand'] = self.on_text_scroll

    def on_scrollbar(self, *args):
        """Scrolls both text widgets when the scrollbar is moved"""
        self.content_rank.yview(*args)
        self.content_name.yview(*args)
        self.content_picStyle.yview(*args)
        self.content_picQuality.yview(*args)
        self.content_music.yview(*args)
        self.content_voice.yview(*args)
        self.content_setting.yview(*args)
        self.content_plot.yview(*args)
        self.content_character.yview(*args)
        self.content_totalPoint.yview(*args)
        self.content_recommend.yview(*args)

    def on_text_scroll(self, *args):
        """Moves the scrollbar and scrolls text widgets when the mousewheel
        is moved on a text widget"""
        self.scrollbar.set(*args)
        self.on_scrollbar('moveto', args[0])
