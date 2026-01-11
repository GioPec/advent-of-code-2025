### CLASSES ###

class Extreme_Coords:
    min_x: int = 0
    min_y: int = 0
    max_x: int = 0
    max_y: int = 0

    def __init__(self, min_x: int = 0, min_y: int = 0, max_x: int = 0, max_y: int = 0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

class Node:
    x: int
    y: int
    # A node has assigned a "potential" maximum score, if taken as a potential lower/upper/left/right corner
    ll_score: int
    lr_score: int
    ul_score: int
    ur_score: int

    def __init__(self, x: str, y: str, compute_scores: bool = False, extreme_coords: Extreme_Coords = None):
        self.x = int(x)
        self.y = int(y)
        if compute_scores and extreme_coords:
            self.compute_scores(extreme_coords)

    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return str(self)
    
    def compute_scores(self, extreme_coords: Extreme_Coords):
        self.ll_score = (extreme_coords.max_x - self.x) * (extreme_coords.max_y - self.y)
        self.lr_score = self.x                          * (extreme_coords.max_y - self.y)
        self.ul_score = (extreme_coords.max_x - self.x) * self.y
        self.ur_score = self.x                          * self.y

### FUNCTIONS ###

def find_extreme_coords(l: list[Node]) -> Extreme_Coords:
    l.sort(key=lambda n: n.x)
    min_x = l[0].x
    max_x = l[-1].x

    l.sort(key=lambda n: n.y)
    min_y = l[0].y
    max_y = l[-1].y

    return Extreme_Coords(min_x, min_y, max_x, max_y)

# convert to (0,0) system
def normalize_coords(nodes: list[Node], true_min_x: int, true_min_y: int, extreme_coords: Extreme_Coords) -> list[Node]:
    new_nodes: list[Node] = []
    for n in nodes:
        new_nodes.append(
            Node(n.x-true_min_x, n.y-true_min_y, compute_scores = True, extreme_coords = extreme_coords)
            )
    return new_nodes

# convert to (0,0) system
def normalize_extreme_coords(true_extreme_coords: Extreme_Coords) -> Extreme_Coords:
    return Extreme_Coords(
            true_extreme_coords.min_x - true_extreme_coords.min_x, # = 0
            true_extreme_coords.min_y - true_extreme_coords.min_y, # = 0
            true_extreme_coords.max_x - true_extreme_coords.min_x, 
            true_extreme_coords.max_y - true_extreme_coords.min_y
            )

################

DEBUG = True
res = 0

if DEBUG: print("Start...")

### MAIN ###

#with open("9/input.txt", 'r') as file:
with open("9/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

nodes: list[Node] = []
for row in rows:
    nodes.append(
        Node(row.split(",")[0], row.split(",")[1])
        )

true_extreme_coords = find_extreme_coords(nodes)
if DEBUG: print("true_min_x =", true_extreme_coords.min_x)
if DEBUG: print("true_max_x =", true_extreme_coords.max_x)
if DEBUG: print("true_min_y =", true_extreme_coords.min_y)
if DEBUG: print("true_max_y =", true_extreme_coords.max_y)
if DEBUG: print("old nodes =", nodes)

extreme_coords = normalize_extreme_coords(true_extreme_coords)
nodes = normalize_coords(nodes, true_extreme_coords.min_x, true_extreme_coords.min_y, extreme_coords)
if DEBUG: print("min_x =", extreme_coords.min_x)
if DEBUG: print("max_x =", extreme_coords.max_x)
if DEBUG: print("min_y =", extreme_coords.min_y)
if DEBUG: print("max_y =", extreme_coords.max_y)
if DEBUG: print("nodes =", nodes)

best_ll_corner = nodes.sort(key=lambda n: n.ll_score, reverse=True)[0]
best_ll_corner = nodes.sort(key=lambda n: n.ll_score, reverse=True)[0]
best_lr_corner = nodes.sort(key=lambda n: n.lr_score, reverse=True)[0]
best_ul_corner = nodes.sort(key=lambda n: n.ul_score, reverse=True)[0]
best_ur_corner = nodes.sort(key=lambda n: n.ur_score, reverse=True)[0]

best_area_ll_ur = (best_ur_corner.x - best_ll_corner.x) * (best_ur_corner.y - best_ll_corner.y)
best_area_lr_ul = (best_lr_corner.x - best_ul_corner.x) * (best_ul_corner.y - best_lr_corner.y)
res = max(best_area_ll_ur, best_area_lr_ul)

if DEBUG: print("\n********\nres =", res,"\n********\n")