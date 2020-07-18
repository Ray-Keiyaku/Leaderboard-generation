import os
import time
from PIL import Image, ImageDraw, ImageFont

from globalData import data


def print_table(table_now, table_content):

    table_content.remove(table_content[0])

    image = Image.open(data.TEMPLATE_PATH)  # 图片模板
    image = image.resize((700, 1000), Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    # width, height = image.size
    font = ImageFont.truetype(data.PRINT_FONT, data.PRINT_FONT_SIZE)
    color = data.PRINT_FONT_COLOR
    start_x = 50
    start_y = 300
    line_spacing = data.PRINT_LINE_SPACING

    # 标题
    cur_time = time.strftime("%Y.%m.%d", time.localtime())
    title = "{}排行榜：（更新于{}）".format(table_now, cur_time)
    draw.text((start_x, start_y), u'%s' % title, color, font)

    # 内容
    draw.text((start_x, start_y + line_spacing), "排名", color, font)
    for num, summary in enumerate(table_content):
        y = start_y + (num + 2) * line_spacing
        draw.text((start_x, y), u'%s' % str(num + 1), color, font)
        if num > 14:
            break

    draw.text((start_x + 100, start_y + line_spacing), "名称", color, font)
    for num, summary in enumerate(table_content):
        y = start_y + (num + 2) * line_spacing
        draw.text((start_x + 100, y), u'%s' % summary[0], color, font)
        if num > 14:
            break

    draw.text((start_x + 450, start_y + line_spacing), "总分", color, font)
    for num, summary in enumerate(table_content):
        y = start_y + (num + 2) * line_spacing
        draw.text((start_x + 450, y), u'%s' % summary[8], color, font)
        if num > 14:
            break

    draw.text((start_x + 550, start_y + line_spacing), "推荐", color, font)
    for num, summary in enumerate(table_content):
        y = start_y + (num + 2) * line_spacing
        draw.text((start_x + 550, y), u'%s' % summary[9], color, font)
        if num > 14:
            break

    # 保存图片
    image.save(data.PICTURE_PATH, 'png')
