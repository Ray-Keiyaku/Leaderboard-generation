import openpyxl


def table_export(file_path, table_now, table_content):
    index = len(table_content)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = table_now
    table_title = ["排名", "名称", "画风", "画质", "音乐", "语音", "设定", "剧情", "角色", "总分", "推荐"]
    for i in range(0, len(table_title)):
        sheet.cell(row=1, column=i + 1, value=table_title[i])
    for i in range(0, index):
        sheet.cell(row=i + 2, column=1, value=str(i + 1))
        for j in range(0, len(table_content[i])):
            sheet.cell(row=i + 2, column=j + 2, value=str(table_content[i][j]))
    try:
        workbook.save(file_path)
        # print("xlsx格式表格写入数据成功！")
        return True
    except PermissionError:
        return False
