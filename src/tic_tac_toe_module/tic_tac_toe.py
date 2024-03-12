from tic_tac_toe_module.position import Position


class TicTacToe:

    def __init__(self):
        self.board = [[Position.EMPTY, Position.EMPTY, Position.EMPTY],
                      [Position.EMPTY.value, Position.EMPTY, Position.EMPTY],
                      [Position.EMPTY.value, Position.EMPTY.value, Position.EMPTY.value]]

    def makeMove(self, row: int, column: int):
        self.checkMove(row, column)

    def checkMove(self, row, column):
        pass
