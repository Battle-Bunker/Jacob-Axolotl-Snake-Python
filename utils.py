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
        for peice in enemy["body"]:
            all_pos.append(peice)
    for peice in me:
        all_pos.remove(peice)
        



def find_intersections(enemy_positions, possible_moves):
    intersections = []

    for move_name, move_coords in possible_moves.items():
        for enemy in enemy_positions:
            if move_coords['x'] == enemy['x'] and move_coords['y'] == enemy['y']:
                intersections.append(move_name)
                break

    return intersections