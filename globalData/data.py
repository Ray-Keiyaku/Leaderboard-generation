import os

SOFT_INFO = "author: ray      \nversion: v0.0.1"

# PATH
TOP_PATH = os.path.expanduser('~') + "/.LeaderboardGenerator"
DATA_PATH = TOP_PATH + "/database.db"
TEMPLATE_PATH = TOP_PATH + "/template.jpg"
PICTURE_PATH = TOP_PATH + "/temp.png"

# Weight
INIT_LIST = ["动漫", "电影", "电视剧"]
WEIGHT_TOTAL = {'画风': 1 / 90, '画质': 2 / 90, '音乐': 1 / 90, '语音': 1 / 90, '设定': 1 / 90, '剧情': 1 / 90, '角色': 2 / 90}
WEIGHT_RECOMMEND = {'画风': 0, '画质': 2 / 60, '音乐': 1 / 60, '语音': 1 / 60, '设定': 1 / 60, '剧情': 1 / 60, '角色': 0}

# Print Parameter
PRINT_FONT = TOP_PATH + "/SourceHanSans-Regular.ttc"
PRINT_FONT_SIZE = 24
PRINT_LINE_SPACING = PRINT_FONT_SIZE + 12
PRINT_FONT_COLOR = "#000000"

# Display Parameter
DISPLAY_FONT = "微软雅黑"

