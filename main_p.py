# The corrected code with appropriate logic and syntax

import random
import typing
import utils


def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#ABABAB",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


def start(game_state: typing.Dict):
    print("GAME START")


def end(game_state: typing.Dict):
    print("GAME OVER\n")


def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {
        "up": True,
        "down": True,
        "left": True,
        "right": True
    }

    my_head = game_state["you"]["body"][0]
    my_neck = game_state["you"]["body"][1]

    if my_neck["x"] < my_head["x"]:
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:
        is_move_safe["up"] = False

    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    if my_head['y'] == 0:
        is_move_safe["down"] = False
    if board_height - 1 == my_head['y']:
        is_move_safe["up"] = False
    if my_head['x'] == 0:
        is_move_safe["left"] = False
    if board_width - 1 == my_head['x']:
        is_move_safe["right"] = False

    my_body = game_state['you']['body']
    possible_moves = utils.possible_moves(my_body[0]['x'], my_body[0]['y'])

    for direction, coord in possible_moves.items():
        if coord in my_body:
            is_move_safe[direction] = False

    opponents = game_state['board']['snakes']
    all_enemy_pos = utils.all_enemy_pos(opponents, my_body)

    for move in utils.find_intersections(all_enemy_pos, is_move_safe):
        is_move_safe[move] = False

    safe_moves = [move for move, isSafe in is_move_safe.items() if isSafe]

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    next_move = random.choice(safe_moves)
    food = game_state['board']['food']

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


if __name__ == "__main__":
    from server import run_server

    run_server({
        "info": info,
        "start": start,
        "move": move,
        "end": end
    })