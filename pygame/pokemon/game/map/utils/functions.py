def euclidian_distance(*values):
    (a,b,c,d), (x,y,z,w) = values
    return ((a-x)**2 + (b-y)**2 + (c-z)**2 + (d-w)**2) ** (1/2)