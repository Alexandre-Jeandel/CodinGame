import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x = x0
y = y0
lu = 0
ll = 0
ld = h - 1
lr = w - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if "U" in bomb_dir:
        dir = - 1
        dist_to_limit_u = y - lu
        newy = y + dir * math.ceil((dist_to_limit_u)/2)
        ld = y
        y = newy
    if "D" in bomb_dir:
        dir = + 1
        dist_to_limit_d = - y + ld
        newy = y + dir * math.ceil((dist_to_limit_d)/2)
        lu = y
        y = newy
    if "L" in bomb_dir:
        dir = - 1
        dist_to_limit_l = + x - ll
        newx = x + dir * math.ceil((dist_to_limit_l)/2)
        lr = x
        x = newx
    if "R" in bomb_dir:
        dir = + 1
        dist_to_limit_r = - x + lr
        newx = x + dir * math.ceil((dist_to_limit_r)/2)
        ll = x
        x = newx



    print(x, y)