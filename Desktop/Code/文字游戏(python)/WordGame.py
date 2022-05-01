from msvcrt import getch
from os import system

wall = "墙"
me = "我"
door = "门"
null = "  "
wg_firstLevel = [
    [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
    [me, null, null, null, null, null, null, null, null, null, null, door],
    [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall]
]
x, y = 1, 0
while True:
    for i in wg_firstLevel:
        for j in i:
            print(j, end="", sep="")
        print()
    c = getch()
    if (c == 'w'):
        if (wg_firstLevel[x - 1][y] != wall):
            wg_firstLevel[x][y] = null
            x -= 1
    if (c == 's'):
        if (wg_firstLevel[x + 1][y] != wall):
            wg_firstLevel[x][y] = null
            x += 1
    if (c == 'a'):
        if (wg_firstLevel[x][y - 1] != wall):
            wg_firstLevel[x][y] = null
            y -= 1
    if (c == 'd'):
        if (wg_firstLevel[x][y + 1] != wall):
            wg_firstLevel[x][y] = null
            y += 1

    wg_firstLevel[x][y] = me
    system("cls")
