from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class Board(FloatLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(Board, self).__init__(size=(1600, 200))
        self.up_store = Image(source='images\\store.png', pos=(0, 0), size_hint=(0.125, 1))
        self.up_store.allow_stretch = True
        self.add_widget(self.up_store)


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        return Board()


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
