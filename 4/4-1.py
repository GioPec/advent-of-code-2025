### FUNCTIONS ###

def get_neighbours(x, y):
    res = []
    if x > 0:
        res.append([x-1, y])
        if (y>0): 
            res.append([x-1, y-1])
        if (y<ROWS-1): 
            res.append([x-1, y+1])
    if x < COLS-1:
        res.append([x+1, y])
        if (y>0): 
            res.append([x+1, y-1])
        if (y<ROWS-1): 
            res.append([x+1, y+1])
    if y > 0:
        res.append([x, y-1])
    if y < ROWS-1:
        res.append([x, y+1])

    if DEBUG: print("Neighbours of", x, ",", y, "=", res)
    return res

def get_neighbour_paper_number(neighbours):
    res = 0
    for n in neighbours:
        if FLOOR[n[0]][n[1]] == "@":
            res += 1
    if DEBUG: print("Papers close:", res)
    return res


################

DEBUG = False
accessible = 0

if DEBUG: print("Start...")

### MAIN ###

with open("4/input.txt", 'r') as file:
#with open("4/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

FLOOR = list(map(lambda _: list(_), rows))
ROWS = len(FLOOR)
COLS = len(FLOOR[0])
if DEBUG: print(FLOOR)

for r in range(ROWS):
    for c in range(COLS):
        if (FLOOR[r][c] == "@" and
            get_neighbour_paper_number(get_neighbours(r,c)) < 4):
            accessible += 1

print("\n********\nAccessible =", accessible,"\n********\n")