import math

def e_dist(a, b): # euclidian distance
    dist = 0
    for a_i, b_i in zip(a, b):
        dist += (a_i - b_i) ** 2
    return math.floor(math.sqrt(dist))

def walk_distance(curr_pos, rsp_pos, wr):
    x, y = curr_pos
    rx, ry = rsp_pos
    if x >= (rx - wr) and x <= (rx + wr) and y >= (ry - wr) and y <= (ry + wr):
        return True
    else:
        return False