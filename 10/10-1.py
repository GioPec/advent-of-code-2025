### CLASSES ###

class Machine:
    light_diagram: list[int] = []
    wiring_schematics: list[list[int]] = []
    min_button_presses: int = 0

    def __init__(self, row: str):
        self.light_diagram = []
        self.wiring_schematics = []

        raw_light_diagram = row.split('] ')[0][1:]
        self.light_diagram = [0 if x == '.' else 1 for x in raw_light_diagram]

        raw_schematics = row.split('] ')[1].split(' {')[0]
        for raw_schematic in raw_schematics.strip().split(' '):
            raw_schematic = raw_schematic.replace('(','').replace(')','')
            buttons = [int(x) for x in raw_schematic.split(',')]
            self.wiring_schematics.append(buttons)

        self.compute_min_button_presses()

    def __str__(self):
        return f"({self.light_diagram}, {self.wiring_schematics})"
    def __repr__(self):
        return str(self)
    
    def compute_min_button_presses(self):
        combinations = 2 ** len(self.wiring_schematics) - 1
        min_res = float('inf')
        for i in range(0, combinations):
            # I use binary to represent which buttons are pressed
            on_off_combination = str(bin(i)[2:].zfill(len(self.wiring_schematics)))
            #if DEBUG: print("on_off_combination =", on_off_combination)
            diagram = [0] * len(self.light_diagram)
            for on_off_index, on_off in enumerate(on_off_combination):
                if on_off == '1':
                    for index_to_change in self.wiring_schematics[on_off_index]:
                        diagram[index_to_change] = change(diagram[index_to_change])

            if diagram == self.light_diagram:
                if DEBUG: print("MATCH:", on_off_combination)
                local_res = on_off_combination.count('1')
                if local_res < min_res:
                    min_res = local_res

        self.min_button_presses = min_res
    
def change(x: int) -> int:
    return 1 if x == 0 else 0


### FUNCTIONS ###

################

DEBUG = False
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("10/input.txt", 'r') as file:
#with open("10/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

machines: list[Machine] = []
for row in rows:
    machines.append(Machine(row))

res = sum([m.min_button_presses for m in machines])

print("\n********\nres =", res,"\n********\n")