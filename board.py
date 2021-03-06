from kivy.app import App
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class Pit(ButtonBehavior, Image):
    def __init__(self, row, column, board, source='images\\pit.png'):
        """
        Instantiate a pit.
        :param row: line of the pit
        :type row: int
        :param column: column of the pit
        :type column: int
        :param board: the board which the pit is in
        :type board: Board
        """
        super(Pit, self).__init__()
        self.row = row
        self.column = column
        self.source = source
        self.board = board
        self.amount = 4

    def on_press(self):
        raise NotImplementedError


class Board(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        self.rows = 2
        self.cols = 7
        super(Board, self).__init__()

        self._insert_pits()

    def _insert_pits(self):
        """Insert the stores and pits in the board."""
        self.up_store = Pit(0, 0, self, 'images\\store.png')
        self.add_widget(self.up_store)

        self.up_pits = []
        self.down_pits = []
        for column in xrange(1, self.cols):
            self.up_pits.append(Pit(0, column, self))
        for column in xrange(self.cols - 1):
            self.down_pits.append(Pit(1, column, self))

        for pit in self.up_pits + self.down_pits:
            self.add_widget(pit)

        self.down_store = Pit(1, self.cols, self, 'images\\store.png')
        self.add_widget(self.down_store)

    def _has_game_ended(self):
        """
        Return whether the game has ended. The game ends when all pits of one player are empty.
        :return: whether the game has ended
        :rtype: bool
        """
        for pit in self.up_pits:
            if pit.amount != 0:
                break
        else:
            return True
        for pit in self.down_pits:
            if pit.amount != 0:
                return False
        return True


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        return Board()


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
