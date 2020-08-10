import os

SOFT_INFO = "author: Ray      \nversion: v0.1.1"

# Resource
res = {"template": "template.jpg", "print_font": "SourceHanSans-Regular.ttc"}

# PATH
TOP_PATH = os.path.expanduser('~') + "/.LeaderboardGenerator"
DATA_PATH = TOP_PATH + "/database.db"
PICTURE_PATH = TOP_PATH + "/temp.png"
BACKUP_PATH = TOP_PATH + "/database.bak"
TEMPLATE_PATH = os.path.join(TOP_PATH, res["template"])
PRINT_FONT_PATH = os.path.join(TOP_PATH, res["print_font"])

# Weight
INIT_LIST = ["动漫", "电影", "电视剧"]
WEIGHT_TOTAL = {'画风': 1 / 90, '画质': 2 / 90, '音乐': 1 / 90, '语音': 1 / 90, '设定': 1 / 90, '剧情': 1 / 90, '角色': 2 / 90}
WEIGHT_RECOMMEND = {'画风': 0, '画质': 2 / 50, '音乐': 1 / 50, '语音': 1 / 50, '设定': 1 / 50, '剧情': 0, '角色': 0}

# Print Parameter
PRINT_FONT_SIZE = 24
PRINT_LINE_SPACING = PRINT_FONT_SIZE + 12
PRINT_FONT_COLOR = "#000000"

# Display Parameter
DISPLAY_FONT = "微软雅黑"
