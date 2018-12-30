from kivy.app import App
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class Pit(ButtonBehavior, Image):
    def __init__(self, row, column, source='images\\pit.png'):
        """
        Instantiate a pit.
        :param row: line of the pit
        :type row: int
        :param column: column of the pit
        :type column: int
        """
        super(Pit, self).__init__()
        self.row = row
        self.column = column
        self.source = source

    def on_press(self):
        raise NotImplementedError


class Board(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        self.rows = 2
        self.cols = 7
        super(Board, self).__init__()

        self.add_widget(self.up_store)


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        return Board()


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
