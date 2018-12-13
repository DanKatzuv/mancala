from abc import ABCMeta, abstractmethod


class PlayerBase:
    """An abstract class representing a player."""
    __metaclass__ = ABCMeta

    def __init__(self, side):
        """
        Instantiate a player.
        :param side: player's row side ("up" or "down")
        :type side: str
        """
        self.side = side

    @abstractmethod
    def turn(self, board):
        """
        Return player's choice. The choice is the number of the pit the player wants to pick marbles from.
        :param board: current board of the game
        :type board: BoardRepresentation
        :return: player's choice
        :rtype: int
        """
        pass
