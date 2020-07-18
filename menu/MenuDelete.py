import tkinter as tk
from tkinter import END

from Leaderboard.read import get_table_content
from Leaderboard.write import delete_to_table
from globalData import data


class MenuDelete(tk.Toplevel):
    def __init__(self, table_now):
        super().__init__()
        self.title('删除数据：')
        # self.geometry('420x320')

        # 数据
        self.table_now = table_now
        self.listbox = tk.Listbox(self, width=25, font=(data.DISPLAY_FONT, 12))
        self.data = get_table_content(table_now)

        # 弹窗界面
        self.setup_UI()
        self.grab_set()

    def setup_UI(self):
        lab_message = tk.Label(self, text='删除{}中数据：(操作不可逆，请谨慎操作)'.format(self.table_now), font=(data.DISPLAY_FONT, 15))
        lab_message.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        # 选择名称
        lab_hint = tk.Label(self, text='选择要删除的项：', font=(data.DISPLAY_FONT, 13))
        self.data.remove(self.data[0])
        for item in self.data:
            self.listbox.insert(END, item[0])
        lab_hint.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        self.listbox.grid(row=2, column=0, columnspan=2)

        # 按钮
        frame_button = tk.Frame(self)
        button_yes = tk.Button(frame_button, text='确定', font=(data.DISPLAY_FONT, 15), width=10, height=1, command=self.confirm)
        button_yes.grid(row=0, column=0, sticky=tk.E, padx=15, pady=10)
        button_no = tk.Button(frame_button, text='取消', font=(data.DISPLAY_FONT, 15), width=10, height=1, command=self.cancel)
        button_no.grid(row=0, column=1, sticky=tk.E, padx=15, pady=10)
        frame_button.grid(row=3, column=0, columnspan=2)

    def confirm(self):
        name_select = self.listbox.curselection()  # 设置数据
        if not name_select:
            tk.messagebox.showwarning(message='请选择要修改的项目！')
            return
        list_name = [item[0] for item in self.data]
        v_NAME = list_name[name_select[0]]
        message = "NAME={na}\nPicStyle={vps}\nPicQuality={vpq}\nMusic={vm}\nVoice={vv}\n" \
                  "Setting={vs}\nPlot={vp}\nCharacter={vc}\nTotalPoint={vt}\nRecommend={vr}"\
            .format(na=v_NAME, vps=self.data[name_select[0]][1], vpq=self.data[name_select[0]][2],
                    vm=self.data[name_select[0]][3], vv=self.data[name_select[0]][4],
                    vs=self.data[name_select[0]][5], vp=self.data[name_select[0]][6],
                    vc=self.data[name_select[0]][7], vt=self.data[name_select[0]][8],
                    vr=self.data[name_select[0]][9])
        a = tk.messagebox.askokcancel('警告:', '删除的项目为:\n{}\n删除操作不可逆，请仔细核对后谨慎操作！'.format(message))
        if not a:
            return
        delete_to_table(self.table_now, v_NAME)

        self.destroy()  # 销毁窗口

    def cancel(self):
        self.destroy()
