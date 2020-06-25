from Leaderboard.write import init_database
from menu.MenuRoot import MenuRoot

init_database()
app = MenuRoot()
app.mainloop()
