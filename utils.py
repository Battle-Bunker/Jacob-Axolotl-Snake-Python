def possible_moves(x,y):
    pos_moves = {}
    pos_moves["right"] = x+1, y
    pos_moves["left"] = x-1, y
    pos_moves["up"] = x, y+1
    pos_moves["down"] = x, y-1
    return pos_moves