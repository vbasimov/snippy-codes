def check_straight_line(coordinates):
    if 2 == len(coordinates):
        return True
    x1, y1 = coordinates[0][0],coordinates[0][1]
    x2, y2 = coordinates[-1][0],coordinates[-1][1]

    for x,y in coordinates[1:-1]:
        if not (x-x1)*(y2-y1) == (y-y1)*(x2-x1):
            return False
    return True

assert True is check_straight_line([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
assert False is check_straight_line([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
assert True is check_straight_line([[0,0],[0,1],[0,-1]])
