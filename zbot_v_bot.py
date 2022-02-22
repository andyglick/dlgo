from dlgo import agent
from dlgo.agent.naive import RandomBot
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time


def main():
    start = time.process_time()
    start_perf = time.perf_counter_ns()
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.3)
        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
    end = time.process_time()
    end_perf = time.perf_counter_ns()
    print("zbot: elapsed time is " + str(end - start))
    print("zbot_perf: elapsed time is " + str(end_perf - start_perf))

if __name__ == '__main__':
    main()
