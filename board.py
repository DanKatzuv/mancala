from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class Board(FloatLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(Board, self).__init__(size=(1600, 200))
        self.up_store = Image(source='images\\store.png', pos=(0, 0), size_hint=(0.125, 1))
        self.up_store.allow_stretch = True
        self.add_widget(self.up_store)