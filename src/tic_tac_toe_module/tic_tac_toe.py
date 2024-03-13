from tic_tac_toe_module import positions


class TicTacToe:
    def __init__(self):
        self.game_board = [[positions.Positions.EMPTY, positions.Positions.EMPTY, positions.Positions.EMPTY],
                           [positions.Positions.EMPTY, positions.Positions.EMPTY, positions.Positions.EMPTY],
                           [positions.Positions.EMPTY, positions.Positions.EMPTY, positions.Positions.EMPTY]]
        self.is_player_turn = True

    def make_move(self, cell: int):
        row, column = self.check_position(cell)
        if self.game_board[row][column] == positions.Positions.EMPTY:
            self.game_board[row][column] = positions.Positions.X if self.is_player_turn else positions.Positions.O
            return True
        else:
            raise Exception("Invalid position, please try again")

    def switch_player_turn(self):
        self.is_player_turn = not self.is_player_turn

    def check_position(self, cell: int):
        if 1 <= cell <= 3:
            return 0, cell - 1
        elif 4 <= cell <= 6:
            return 1, cell - 4
        elif 7 <= cell <= 9:
            return 2, cell - 7
        else:
            raise ValueError("Incorrect position")

    def check_winner(self):
        return self.check_winner_diagonal_left() or self.check_winner_in_row() \
            or self.check_winner_in_column() or self.check_winner_diagonal_right()

    def check_winner_in_row(self):
        for index in range(3):
            if self.game_board[index][0] != positions.Positions.EMPTY and \
                    self.game_board[index][0] == self.game_board[index][1] == self.game_board[index][2]:
                return True
        return False

    def check_winner_in_column(self):
        for index in range(3):
            if self.game_board[0][index] != positions.Positions.EMPTY and \
                    self.game_board[0][index] == self.game_board[1][index] == self.game_board[2][index]:
                return True
        return False

    def check_winner_diagonal_left(self):
        return self.game_board[0][0] != positions.Positions.EMPTY and \
            self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]

    def check_winner_diagonal_right(self):
        return self.game_board[0][2] != positions.Positions.EMPTY and \
            self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]

    def is_draw(self):
        empty_count = 0
        for row in self.game_board:
            for cell in row:
                if cell == positions.Positions.EMPTY:
                    empty_count += 1
        return empty_count == 0

    def display_game(self):
        print("________________")
        for row in self.game_board:
            for cell in row:
                print(" " if cell == positions.Positions.EMPTY else cell.value, end="      ")
            print()
            print("________________")


if __name__ == "__main__":
    game = TicTacToe()
    game.display_game()

    while True:
        player = "X" if game.is_player_turn else "O"
        try:
            position = int(input(f"Player {player}'s turn. Enter position (1-9): "))
            if not 1 <= position <= 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            if not game.make_move(position):
                print("Position already filled. Please play in another position.")
                continue
            game.switch_player_turn()
            game.display_game()

            if game.check_winner():
                print(f"Player {player} wins!")
                break
            elif game.is_draw():
                print("It's a draw!")
                break

        except ValueError as e:
            print("Stop trying to break the code")
        except Exception as e:
            print(e)
