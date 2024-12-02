area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def draw_area():
    for i in area:
        print(*i)
    print()

area[0][0] = 'X'
draw_area()

area[0][1] = 'X'
draw_area()

area[0][2] = 'X'
draw_area()