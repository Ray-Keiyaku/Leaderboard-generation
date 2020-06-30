import tkinter as tk
from tkinter import END

from Leaderboard.read import get_table_content
from Leaderboard.write import change_to_table
from globalData import data


class MenuChange(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('修改数据：')
        self.geometry('420x570')

        # 数据
        self.table_now = table_now
        self.listbox = tk.Listbox(self, width=25, font=('Arial', 12))
        self.data = get_table_content(table_now)
        self.v_PicStyle = tk.StringVar()
        self.v_PicQuality = tk.StringVar()
        self.v_Music = tk.StringVar()
        self.v_Voice = tk.StringVar()
        self.v_Setting = tk.StringVar()
        self.v_Plot = tk.StringVar()
        self.v_Character = tk.StringVar()

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        lab_message = tk.Label(self, text='修改{}中数据：(评分：0-100分)'.format(self.table_now), font=('Arial', 15))
        lab_message.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        # 选择名称
        lab_hint = tk.Label(self, text='选择要修改的项：', font=('Arial', 13))
        self.data.remove(self.data[0])
        for item in self.data:
            self.listbox.insert(END, item[0])
        lab_hint.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        self.listbox.grid(row=2, column=0, columnspan=2)

        # 输入提示
        frame_lab = tk.Frame(self)
        lab_PicStyle = tk.Label(frame_lab, text='画风：', font=('Arial', 12))
        lab_PicStyle.grid(row=0, column=0, sticky=tk.W, pady=5)
        lab_PicQuality = tk.Label(frame_lab, text='画质：', font=('Arial', 12))
        lab_PicQuality.grid(row=1, column=0, sticky=tk.W, pady=5)
        lab_Music = tk.Label(frame_lab, text='音乐：', font=('Arial', 12))
        lab_Music.grid(row=2, column=0, sticky=tk.W, pady=5)
        lab_Voice = tk.Label(frame_lab, text='语音：', font=('Arial', 12))
        lab_Voice.grid(row=3, column=0, sticky=tk.W, pady=5)
        lab_Setting = tk.Label(frame_lab, text='设定：', font=('Arial', 12))
        lab_Setting.grid(row=4, column=0, sticky=tk.W, pady=5)
        lab_Plot = tk.Label(frame_lab, text='剧情：', font=('Arial', 12))
        lab_Plot.grid(row=5, column=0, sticky=tk.W, pady=5)
        lab_Character = tk.Label(frame_lab, text='角色：', font=('Arial', 12))
        lab_Character.grid(row=6, column=0, sticky=tk.W, pady=5)
        frame_lab.grid(row=3, column=0, rowspan=8, sticky=tk.E)

        # 输入框
        frame_entry = tk.Frame(self)
        entry_PicStyle = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_PicStyle)
        entry_PicStyle.grid(row=0, column=0, sticky=tk.W, pady=5)
        entry_PicQuality = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_PicQuality)
        entry_PicQuality.grid(row=1, column=0, sticky=tk.W, pady=5)
        entry_Music = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_Music)
        entry_Music.grid(row=2, column=0, sticky=tk.W, pady=5)
        entry_Voice = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_Voice)
        entry_Voice.grid(row=3, column=0, sticky=tk.W, pady=5)
        entry_Setting = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_Setting)
        entry_Setting.grid(row=4, column=0, sticky=tk.W, pady=5)
        entry_Plot = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_Plot)
        entry_Plot.grid(row=5, column=0, sticky=tk.W, pady=5)
        entry_Character = tk.Entry(frame_entry, font=('Arial', 12), textvariable=self.v_Character)
        entry_Character.grid(row=6, column=0, sticky=tk.W, pady=5)
        frame_entry.grid(row=3, column=1, rowspan=8, sticky=tk.W)

        # 按钮
        frame_button = tk.Frame(self)
        button_yes = tk.Button(frame_button, text='确定', font=('Arial', 15), width=10, height=1, command=self.confirm)
        button_yes.grid(row=0, column=0, sticky=tk.E, padx=15, pady=10)
        button_no = tk.Button(frame_button, text='取消', font=('Arial', 15), width=10, height=1, command=self.cancel)
        button_no.grid(row=0, column=1, sticky=tk.E, padx=15, pady=10)
        frame_button.grid(row=11, column=0, columnspan=2, sticky=tk.E)

    def confirm(self):
        name_select = self.listbox.curselection()  # 设置数据
        if not name_select:
            tk.messagebox.showwarning(message='请选择要修改的项目！')
            return
        list_name = [item[0] for item in self.data]
        v_NAME = list_name[name_select[0]]

        if not_number(self.v_PicStyle.get()) or int(self.v_PicStyle.get()) > 100 or int(self.v_PicStyle.get()) < 0:
            tk.messagebox.showwarning(message='画风数值非法！(范围：0-100)')
            return
        if not_number(self.v_PicQuality.get()) or int(self.v_PicQuality.get()) > 100 or int(
                self.v_PicQuality.get()) < 0:
            tk.messagebox.showwarning(message='画质数值非法！(范围：0-100)')
            return
        if not_number(self.v_Music.get()) or int(self.v_Music.get()) > 100 or int(self.v_Music.get()) < 0:
            tk.messagebox.showwarning(message='音乐数值非法！(范围：0-100)')
            return
        if not_number(self.v_Voice.get()) or int(self.v_Voice.get()) > 100 or int(self.v_Voice.get()) < 0:
            tk.messagebox.showwarning(message='语音数值非法！(范围：0-100)')
            return
        if not_number(self.v_Setting.get()) or int(self.v_Setting.get()) > 100 or int(self.v_Setting.get()) < 0:
            tk.messagebox.showwarning(message='设定数值非法！(范围：0-100)')
            return
        if not_number(self.v_Plot.get()) or int(self.v_Plot.get()) > 100 or int(self.v_Plot.get()) < 0:
            tk.messagebox.showwarning(message='剧情数值非法！(范围：0-100)')
            return
        if not_number(self.v_Character.get()) or int(self.v_Character.get()) > 100 or int(self.v_Character.get()) < 0:
            tk.messagebox.showwarning(message='角色数值非法！(范围：0-100)')
            return
        total_point, recommend_point = self.cal_point()
        a = tk.messagebox.askokcancel('提示:', '总分为：{}\n推荐分为：{}\n'.format(total_point, recommend_point))
        if not a:
            return
        change_to_table(self.table_now, v_NAME, int(self.v_PicStyle.get()), int(self.v_PicQuality.get()),
                        int(self.v_Music.get()), int(self.v_Voice.get()), int(self.v_Setting.get()),
                        int(self.v_Plot.get()), int(self.v_Character.get()), total_point, recommend_point)

        self.destroy()  # 销毁窗口

    def cancel(self):
        self.destroy()

    def cal_point(self):
        weight_total = [data.WEIGHT_TOTAL['画风'], data.WEIGHT_TOTAL['画质'], data.WEIGHT_TOTAL['音乐'],
                        data.WEIGHT_TOTAL['语音'], data.WEIGHT_TOTAL['设定'], data.WEIGHT_TOTAL['剧情'],
                        data.WEIGHT_TOTAL['角色']]
        weight_recommend = [data.WEIGHT_RECOMMEND['画风'], data.WEIGHT_RECOMMEND['画质'],
                            data.WEIGHT_RECOMMEND['音乐'], data.WEIGHT_RECOMMEND['语音'],
                            data.WEIGHT_RECOMMEND['设定'], data.WEIGHT_RECOMMEND['剧情'],
                            data.WEIGHT_RECOMMEND['角色']]
        point_list = [int(self.v_PicStyle.get()), int(self.v_PicQuality.get()),
                      int(self.v_Music.get()), int(self.v_Voice.get()),
                      int(self.v_Setting.get()), int(self.v_Plot.get()),
                      int(self.v_Character.get())]
        total_point = 0
        recommend_point = 0
        for i, point in enumerate(point_list):
            total_point += point * weight_total[i]
            recommend_point += point * weight_recommend[i]
        total_point = round(total_point, 2)
        recommend_point = round(recommend_point, 2)
        return total_point, recommend_point


def not_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True
