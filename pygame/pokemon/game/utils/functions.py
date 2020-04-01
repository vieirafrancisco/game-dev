import math

def euclidian_distance(x0, y0, x1, y1):
    x = (x0-x1) ** 2
    y = (y0-y1) ** 2
    return math.floor(math.sqrt(x + y))

def walk_distance(curr_pos, rsp_pos, wr):
    x, y = curr_pos
    rx, ry = rsp_pos
    if x >= (rx - wr) and x <= (rx + wr) and y >= (ry - wr) and y <= (ry + wr):
        return True
    else:
        return False