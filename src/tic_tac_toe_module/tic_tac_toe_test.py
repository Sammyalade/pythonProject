from tic_tac_toe import TicTacToe, positions
import pytest

from tic_tac_toe_module import tic_tac_toe


class TestTicTacToe:
    @pytest.fixture
    def game(self):
        return TicTacToe()

    def test_player_can_make_move_to_first_position(self, game):
        game.make_move(1)
        assert game.game_board[0][0] == positions.Positions.X

    def test_player_can_make_move_to_second_position(self, game):
        game.make_move(2)
        assert game.game_board[0][1] == positions.Positions.X

    def test_player_can_make_move_to_third_position(self, game):
        game.make_move(3)
        assert game.game_board[0][2] == positions.Positions.X

    def test_player_can_make_move_to_fourth_position(self, game):
        game.make_move(4)
        assert game.game_board[1][0] == positions.Positions.X

    def test_player_can_make_move_to_fifth_position(self, game):
        game.make_move(5)
        assert game.game_board[1][1] == positions.Positions.X

    def test_player_can_make_move_to_sixth_position(self, game):
        game.make_move(6)
        assert game.game_board[1][2] == positions.Positions.X

    def test_player_can_make_move_to_seventh_position(self, game):
        game.make_move(7)
        assert game.game_board[2][0] == positions.Positions.X

    def test_player_can_make_move_to_eighth_position(self, game):
        game.make_move(8)
        assert game.game_board[2][1] == positions.Positions.X

    def test_player_can_make_move_to_ninth_position(self, game):
        game.make_move(9)
        assert game.game_board[2][2] == positions.Positions.X

    def test_second_player_can_move_to_first_position(self, game):
        game.switch_player_turn()
        game.make_move(1)
        assert game.game_board[0][0] == positions.Positions.O

    def test_second_player_can_move_to_second_position(self, game):
        game.switch_player_turn()
        game.make_move(2)
        assert game.game_board[0][1] == positions.Positions.O

    def test_second_player_can_move_to_third_position(self, game):
        game.switch_player_turn()
        game.make_move(3)
        assert game.game_board[0][2] == positions.Positions.O

    def test_second_player_can_move_to_fourth_position(self, game):
        game.switch_player_turn()
        game.make_move(4)
        assert game.game_board[1][0] == positions.Positions.O

    def test_second_player_can_move_to_fifth_position(self, game):
        game.switch_player_turn()
        game.make_move(5)
        assert game.game_board[1][1] == positions.Positions.O

    def test_second_player_can_move_to_sixth_position(self, game):
        game.switch_player_turn()
        game.make_move(6)
        assert game.game_board[1][2] == positions.Positions.O

    def test_second_player_can_move_to_seventh_position(self, game):
        game.switch_player_turn()
        game.make_move(7)
        assert game.game_board[2][0] == positions.Positions.O

    def test_second_player_can_move_to_eighth_position(self, game):
        game.switch_player_turn()
        game.make_move(8)
        assert game.game_board[2][1] == positions.Positions.O

    def test_second_player_can_move_to_ninth_position(self, game):
        game.switch_player_turn()
        game.make_move(9)
        assert game.game_board[2][2] == positions.Positions.O

    def test_both_players_can_make_move(self, game):
        game.make_move(2)
        game.switch_player_turn()
        game.make_move(9)
        assert game.game_board[0][1] == positions.Positions.X
        assert game.game_board[2][2] == positions.Positions.O

    def test_players_can_win_in_column_1(self, game):
        game.make_move(1)
        game.make_move(4)
        game.make_move(7)
        assert game.check_winner() is True

    def test_players_can_win_in_column_2(self, game):
        game.make_move(2)
        game.make_move(5)
        game.make_move(8)
        assert game.check_winner() is True

    def test_players_can_win_in_column_3(self, game):
        game.make_move(3)
        game.make_move(6)
        game.make_move(9)
        assert game.check_winner() is True

    def test_players_can_win_in_row(self, game):
        game.make_move(1)
        game.make_move(2)
        game.make_move(3)
        assert game.check_winner() is True

    def test_players_can_win_in_row_2(self, game):
        game.make_move(4)
        game.make_move(5)
        game.make_move(6)
        assert game.check_winner() is True

    def test_players_can_win_in_row_3(self, game):
        game.make_move(7)
        game.make_move(8)
        game.make_move(9)
        assert game.check_winner() is True

    def test_players_can_win_diagonal_1(self, game):
        game.make_move(1)
        game.make_move(5)
        game.make_move(9)
        assert game.check_winner() is True

    def test_players_can_win_diagonal_2(self, game):
        game.make_move(3)
        game.make_move(5)
        game.make_move(7)
        assert game.check_winner() is True

    def test_players_can_draw(self, game):
        game.make_move(1)
        game.switch_player_turn()
        game.make_move(2)
        game.switch_player_turn()
        game.make_move(6)
        game.switch_player_turn()
        game.make_move(3)
        game.switch_player_turn()
        game.make_move(5)
        game.switch_player_turn()
        game.make_move(9)
        game.switch_player_turn()
        game.make_move(4)
        game.switch_player_turn()
        game.make_move(7)
        game.switch_player_turn()
        game.make_move(8)
        assert game.is_draw() is True

    def test_player_cannot_play_on_same_cell_twice(self, game):
        game.make_move(2)
        with pytest.raises(Exception):
            game.make_move(2)

    def test_exception_thrown_for_invalid_moves(self, game):
        with pytest.raises(Exception):
            game.make_move(19)
        with pytest.raises(Exception):
            game.make_move(-10)
        with pytest.raises(Exception):
            game.make_move(int("a"))
