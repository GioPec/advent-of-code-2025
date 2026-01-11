### FUNCTIONS ###

################

DEBUG = True
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("7/input.txt", 'r') as file:
#with open("7/test.txt", 'r') as file:
    raw_rows = [line.rstrip() for line in file]

# READ
matrix = []
for raw_row in raw_rows:
    row = []
    for c in raw_row:
        if (c=="S"): c="|"
        row.append(c)
    matrix.append(row)

for y,row in enumerate(matrix):
    for x,c in enumerate(row):
        # CHECK
        if y==0: continue # skip first line
        if c=="^": # splitters remain splitters
            if DEBUG: print(c, end="")
            if matrix[y-1][x] == "|":
                res+=1
            continue 
        # - case ABOVE
        if matrix[y-1][x] == "|": 
            matrix[y][x] = "|"
        # - case SPLIT LEFT
        if (x!=0 
        and matrix[y][x-1] == "^" 
        and matrix[y-1][x-1] == "|"): 
            matrix[y][x] = "|"
        # - case SPLIT RIGHT
        if (x!=len(row)-1 
        and matrix[y][x+1] == "^" 
        and matrix[y-1][x+1] == "|"): 
            matrix[y][x] = "|"

        if DEBUG: print(matrix[y][x], end="")

    if DEBUG: print("\n")

print("\n********\nres =", res,"\n********\n")