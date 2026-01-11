### CLASSES ###

class Node:
    id: str = ""
    out_ids: set[str] = []
    neighbors: set[Node] = []

    def __init__(self, row: str):
        self.id = row.split(":")[0].strip()
        self.out_ids = [id.strip() for id in row.split(":")[1][1:].split(" ")]

    def fill_neighbors(self, nodes: list[Node])->None:
        self.neighbors = []
        if self.id == "out": return
        for out_id in self.out_ids:
            out_node = next(filter(lambda n: n.id == out_id, nodes))
            self.neighbors.append(out_node)

    def __str__(self):
        return f"{self.id}"
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id==other.id
        else:
            return False

### FUNCTIONS ###

# Core Concept: Depth-First Search (DFS)

# Start at 'you': Begin the traversal from your source node.
# Explore Neighbors: Move to an unvisited neighbor.
# Mark & Recurse: Add the new node to your current path and mark it as visited (to prevent cycles). Then, recursively call the function from this new node.
# Destination Reached: If the current node is 'out', print or store the current path.
# Backtrack: After exploring all paths from a neighbor, remove it from the path and unmark it as visited, allowing other routes to use it. 

def find_paths_between_nodes(you: Node, out: Node)->int:
    find_paths_between_nodes_recursive(you, out, [], [])

def find_paths_between_nodes_recursive(you: Node, out: Node, path: list[Node], visited: set[Node])->None:
    path.append(you)
    visited.append(you)
    if DEBUG: print(f"{path}")
    
    # Found it! I print the path and increment res
    if you.id == out.id:
        if DEBUG: print(f"FOUND!")
        path.remove(you)
        visited.remove(you)
        global RES
        RES += 1
    else:
        for neighbor in you.neighbors:
            if neighbor in visited:
                continue
            find_paths_between_nodes_recursive(neighbor, out, path, visited)
        path.remove(you)
        visited.remove(you)

################

DEBUG = True
RES = 0

if DEBUG: print("Start...")

### MAIN ###

with open("11/input.txt", 'r') as file:
#with open("11/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

nodes: list[Node] = []
for row in rows:
    nodes.append(Node(row))

# I append the "out" node manually (has no outside nodes)
nodes.append(Node("out:"))

# Fill nodes neighbors arrays
for n in nodes:
    n.fill_neighbors(nodes)

svr: Node = next(filter(lambda n: n.id == "svr", nodes))
out: Node = next(filter(lambda n: n.id == "out", nodes))

find_paths_between_nodes(svr, out)

print("\n********\nres =", RES,"\n********\n")