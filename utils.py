def possible_moves(x,y):
    pos_moves = {}
    pos_moves["right"] = {x+1, y}
    pos_moves["left"] = {x-1, y}
    pos_moves["up"] = {x, y+1}
    pos_moves["down"] = {x, y-1}
    return pos_moves

def all_enemy_pos(enemys, me):
    all_pos = []
    for enemy in enemys:
        for piece in enemy["body"]:
            all_pos.append(piece)
    print(me)
    for piece in me:
        all_pos.remove(piece)

    return all_pos
        



def find_intersections(enemy_positions, possible_moves: dict):
    intersections = []
    for move_name, move_coords in possible_moves.items():
        for enemy in enemy_positions:
            if move_coords["x"] == enemy["x"] and move_coords["y"] == enemy["y"]:
                intersections.append(move_name)
                break

    return intersections
    # intersections = [move_name for move_name, move_coorods in possible_moves.items() for enemy_coords in enemy_positions if move_coords == enemy_coords]
    # this looks like the code equivelant of pasta ^^^^^^^^^^^^^^
    # move_coords = {"x": 5, "y": 6}
    # enemy       = {"x": 5, "y": 6}