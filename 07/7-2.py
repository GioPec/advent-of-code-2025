### CLASSES ###
class Node:
    c = ""
    value = 1

    def __init__(self, c, value):
        self.c = str(c)
        self.value = int(value)
        
    def __str__(self):
        if self.c!="|":
            return str(self.c)
        elif self.c=="|":
            if int(self.value)<10:
                return str(self.value)
            else: return str("*")
    def __repr__(self):
        return str(self)
    
### FUNCTIONS ###

################

DEBUG = False
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
        row.append(Node(c,1))
    matrix.append(row)

for y,row in enumerate(matrix):
    for x,char in enumerate(row):
        # CHECK
        if y==0: continue # skip first line
        if matrix[y][x].c=="^": # splitters remain splitters
            if DEBUG: print(char, end="")
            continue 
        # - case ABOVE
        if matrix[y-1][x].c == "|": 
            matrix[y][x] = Node("|",matrix[y-1][x].value)
        # - case SPLIT LEFT
        if (x!=0 
        and matrix[y][x-1].c == "^" 
        and matrix[y-1][x-1].c == "|"): 
            if matrix[y][x].c == ".":
                matrix[y][x] = Node("|",matrix[y-1][x-1].value) # standard case: new "|", weight one
            elif matrix[y][x].c == "|":
                matrix[y][x] = Node("|",matrix[y-1][x-1].value + matrix[y][x].value) # if was already "|", add value
        # - case SPLIT RIGHT
        if (x!=len(row)-1 
        and matrix[y][x+1].c == "^" 
        and matrix[y-1][x+1].c == "|"): 
            if matrix[y][x].c == ".":
                matrix[y][x] = Node("|",matrix[y-1][x+1].value) # standard case: new "|", weight one
            elif matrix[y][x].c == "|":
                matrix[y][x] = Node("|",matrix[y-1][x+1].value + matrix[y][x].value) # if was already "|", add value

        if DEBUG: print(matrix[y][x], end="")

    if DEBUG: print("\n")

for n in matrix[-1]:
    if n.c =="|":
        res+=n.value

print("\n********\nres =", res,"\n********\n")