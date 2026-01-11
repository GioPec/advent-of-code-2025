### CLASSES ###

class Machine:
    wiring_schematics: list[list[int]] = []
    joltage: list[int] = []
    min_button_presses: int = 0

    def __init__(self, row: str):
        self.wiring_schematics = []
        self.joltage = []

        raw_schematics = row.split('] ')[1].split(' {')[0]
        for raw_schematic in raw_schematics.strip().split(' '):
            raw_schematic = raw_schematic.replace('(','').replace(')','')
            buttons = [int(x) for x in raw_schematic.split(',')]
            self.wiring_schematics.append(buttons)

        raw_joltage = row.split(' {')[-1].replace('}','').strip()
        self.joltage = [int(x) for x in raw_joltage.split(',')]

        self.compute_min_button_presses()

    def __str__(self):
        return f"({self.light_diagram}, {self.wiring_schematics})"
    def __repr__(self):
        return str(self)
    
    def compute_min_button_presses(self):
        array_of_maximum_attempts = compute_array_of_maximum_attempts(self)
        all_schematics_presses_combinations = build_all_schematics_presses_combinations(array_of_maximum_attempts)
        min_button_presses = float('inf')
        total_combinations = len(all_schematics_presses_combinations)
        for idx, combination in enumerate(all_schematics_presses_combinations):
            if idx % max(1, total_combinations // 100) == 0:
                if DEBUG: print(f"  Testing combination {idx+1}/{total_combinations} ({(idx+1)/total_combinations*100:.1f}%)")
            
            result = [0] * len(self.joltage)
            for (presses, schematic) in zip(combination, self.wiring_schematics):   # zip was made by AI
                for button in schematic:
                    result[button] += presses

            if result != self.joltage: continue

            local_button_presses = sum(combination)
            if local_button_presses < min_button_presses:
                min_button_presses = local_button_presses

        self.min_button_presses = min_button_presses

    
# Build an array of "how many times max can I use every schematic".
# Do this by checking which button of the schematic maximizes first 
def compute_array_of_maximum_attempts(m: Machine) -> list[int]:
    res = [0 for _ in range(len(m.wiring_schematics))]
    for i, wiring_schematic in enumerate(m.wiring_schematics):
        max_presses = min([m.joltage[button] for button in wiring_schematic])
        res[i] = max_presses
    return res

# Given a list of int, it returns a list of all the possible combinations of numbers from all zeroes to that list
# NOTE: this function was AI generated. I was tired and didn't want to do this by hand
def build_all_schematics_presses_combinations(max_presses: list[int]) -> list[list[int]]:
    res = []
    
    def generate_combinations(index: int, current: list[int]):
        if index == len(max_presses):
            res.append(current[:])
            return
        
        for i in range(max_presses[index] + 1):
            current.append(i)
            generate_combinations(index + 1, current)
            current.pop()
    
    generate_combinations(0, [])
    print(f"Generated {len(res)} combinations for max_presses={max_presses}: {res[:10]}...")
    return res


### FUNCTIONS ###

################

DEBUG = True
res = 0

if DEBUG: print("Start...")

### MAIN ###

#with open("10/input.txt", 'r') as file:
with open("10/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

machines: list[Machine] = []
for i, row in enumerate(rows):
    if DEBUG: print(f"Processing row {i+1}/{len(rows)} ({(i+1)/len(rows)*100:.1f}%)")
    machines.append(Machine(row))

res = sum([m.min_button_presses for m in machines])

print("\n********\nres =", res,"\n********\n")

# NOTE TO SELF:
# NOT BRUTE-FORCE-ABLE