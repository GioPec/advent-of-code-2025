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
    #update_top_three_longest_circuits(new_c)

def are_nodes_connected(n1: Node, n2: Node) -> bool:
    if n1 in n2.circuit.nodes:
        assert n2 in n1.circuit.nodes
        return True
    return False

def update_top_three_longest_circuits(c: Circuit) -> bool:
    if len(top_three_longest_circuits) < 3: 
        top_three_longest_circuits.append(c)
        top_three_longest_circuits.sort(reverse=True)
        if DEBUG: print(f"new top_three_longest_circuits: {c.length}")
        return True
    if c.length > top_three_longest_circuits[-1].length:
        top_three_longest_circuits.pop(-1)
        top_three_longest_circuits.append(c)
        top_three_longest_circuits.sort(reverse=True)
        if DEBUG: print(f"new top_three_longest_circuits: {c.length}")
        return True


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
#distances = distances[:1000]
if DEBUG: print("distances[:10]:", distances[:10])
if DEBUG: print("distances length:", len(distances))

connections_made = 0
distance_i = 0
#while connections_made < 1000:
for i in range(1000):
    n1 = distances[distance_i].n1
    n2 = distances[distance_i].n2
    d = distances[distance_i].length

    if not are_nodes_connected(n1, n2):
        connect_nodes(n1, n2, d)
        connections_made += 1
    distance_i += 1

circuits: list[Circuit] = []
for n in nodes:
    if n.circuit not in circuits:
        circuits.append(n.circuit)
        
if DEBUG: print("len(circuits):",len(circuits))
circuits.sort(key=lambda x: len(x.nodes), reverse=True)
for i,c in enumerate(circuits):
    if DEBUG: 
        print(f"circuit {i} length: {len(c.nodes)}")
        print(c)

res = len(circuits[0].nodes) * len(circuits[1].nodes) * len(circuits[2].nodes)
print("\n********\nres =", res,"\n********\n")