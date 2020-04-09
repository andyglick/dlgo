from dlgo import goboard_slow
from dlgo.utils import print_board


def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    print_board(game.board)


if __name__ == '__main__':
    main()
