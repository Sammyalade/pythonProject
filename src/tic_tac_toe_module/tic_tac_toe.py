from tic_tac_toe_module.position import Position


class TicTacToe:
    def __init__(self):
        self.game_board = [
            [Position.EMPTY, Position.EMPTY, Position.EMPTY],
            [Position.EMPTY, Position.EMPTY, Position.EMPTY],
            [Position.EMPTY, Position.EMPTY, Position.EMPTY]
        ]
        self.is_player_turn = True

    def make_move(self, row, column):
        self.check_move(row, column)
        if self.game_board[row][column] == Position.EMPTY:
            self.game_board[row][column] = Position.X if self.is_player_turn else Position.O
            if self.check_winner():
                return f"Player {'X' if self.is_player_turn else 'O'} wins!"
            if self.is_draw():
                return "It's a draw!"
            self.is_player_turn = not self.is_player_turn
            self.display_game()
        return None

    def check_move(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise RuntimeError("Invalid move. Rows or columns must not be less than 0 or greater than 2")

        if self.game_board[row][column] != Position.EMPTY:
            raise RuntimeError("Invalid move")

    def check_winner(self):
        return (self.check_winner_diagonal_left() or
                self.check_winner_in_row() or
                self.check_winner_in_column() or
                self.check_winner_diagonal_right())

    def check_winner_in_row(self):
        for index in range(3):
            if (self.game_board[index][0] != Position.EMPTY and
                    self.game_board[index][0] == self.game_board[index][1] ==
                    self.game_board[index][2]):
                return True
        return False

    def check_winner_in_column(self):
        for index in range(3):
            if (self.game_board[0][index] != Position.EMPTY and
                    self.game_board[0][index] == self.game_board[1][index] ==
                    self.game_board[2][index]):
                return True
        return False

    def check_winner_diagonal_left(self):
        return (self.game_board[0][0] != Position.EMPTY and
                self.game_board[0][0] == self.game_board[1][1] ==
                self.game_board[2][2])

    def check_winner_diagonal_right(self):
        return (self.game_board[0][2] != Position.EMPTY and
                self.game_board[0][2] == self.game_board[1][1] ==
                self.game_board[2][0])

    def is_draw(self):
        empty_count = sum(1 for row in self.game_board for position in row if position == Position.EMPTY)
        return empty_count == 0

    def display_game(self):
        print("________________")
        for row in self.game_board:
            for position in row:
                print(" " if position == Position.EMPTY else position, end="      ")
            print()
            print("________________")


