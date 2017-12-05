from pokerapp import PokerApp
from textpoker import TextInterface
from graphical_interface import GraphicsInterface

# inter = TextInterface()
inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
