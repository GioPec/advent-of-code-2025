### CLASSES ###


class Node:
    x: int = 0
    y: int = 0
    z: int = 0
    circuit: Circuit = None

    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.circuit = Circuit([self])
        
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return self.z < other.z
            else: return self.y < other.y
        else: return self.x < other.x

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x==other.x and self.y==other.y and self.z==other.z
        else:
            return False
        
    def __hash__(self):
        return int(f"{str(self.x)}{str(self.y)}{str(self.z)}")
        

class Distance:
    length: int = 0
    n1: Node = None
    n2: Node = None

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.length = self.calculate_distance(self.n1, self.n2)
        
    def __str__(self):
        return f"n1={self.n1},n2={self.n2},length={self.length}"
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.length < other.length
    
    def calculate_distance(self, n1: Node, n2: Node) -> float: 
        return float((n1.x - n2.x)**2 + (n1.y - n2.y)**2 + (n1.z - n2.z)**2)**(1/3) # straight-line euclidean distance
        

class Circuit:
    nodes: list[Node] = []
    length: int = 0

    def __init__(self, n: list[Node], circuit_length=0):
        self.nodes = n
        self.nodes.sort()
        self.length = circuit_length

    def append_node(self, n):
        self.nodes.append(n)
        self.nodes.sort()
        
    def __str__(self):
        res = ""
        for n in self.nodes:
            res += f"{n}\n"
        return res
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.nodes==other.nodes
        else:
            return False
    
### FUNCTIONS ###

def connect_nodes(n1: Node, n2: Node, d: Distance):
    if are_nodes_connected(n1, n2): return
    c1 = n1.circuit
    c2 = n2.circuit
    new_nodes_list = c1.nodes + c2.nodes
    new_nodes_list = list(dict.fromkeys(new_nodes_list))
    new_circuit_length = c1.length + c2.length + d
    new_c = Circuit(new_nodes_list, new_circuit_length)
    for node_to_update in new_c.nodes:
        node_to_update.circuit = new_c

def are_nodes_connected(n1: Node, n2: Node) -> bool:
    if n1 in n2.circuit.nodes:
        assert n2 in n1.circuit.nodes
        return True
    return False

################

DEBUG = False
top_three_longest_circuits: list[Circuit] = []
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("8/input.txt", 'r') as file:
#with open("8/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

nodes: list[Node] = []
for i,r in enumerate(rows):
    nodes.append(Node(r.split(",")[0], r.split(",")[1], r.split(",")[2]))

if DEBUG: print(nodes)

distances: list[Distance] = []
for i in range(0,(len(nodes))):
    for j in range(i+1,(len(nodes))):
        distances.append(Distance(nodes[i], nodes[j]))
        #print(f"{i},{j}")

if DEBUG: print("\n\n\n")
distances.sort()
if DEBUG: print("distances[:10]:", distances[:10])
if DEBUG: print("distances length:", len(distances))

connections_made = 0
last_connection_made = None
for i,distance in enumerate(distances):
    n1 = distance.n1
    n2 = distance.n2
    d = distance.length

    if not are_nodes_connected(n1, n2):
        connect_nodes(n1, n2, d)
        connections_made += 1
        last_connection_made = distance

res = last_connection_made.n1.x * last_connection_made.n2.x
print("\n********\nres =", res,"\n********\n")

# NOTE: correct but slow!! (40s)