### CLASSES ###
class Group:
    sign = ""
    numbers = []

    def __init__(self, sign, numbers):
        self.sign = sign
        self.numbers = numbers
        
    def __str__(self):
        return f"GROUP:sign='{self.sign}',numbers={self.numbers},calculate={self.calculate()}"
    def __repr__(self):
        return f"GROUP:sign='{self.sign}',numbers={self.numbers},calculate={self.calculate()}"

    def calculate(self):
        res = 0 if self.sign=="+" else 1 # init res
        for n in self.numbers:
            if self.sign == "+":
                res += n
            elif self.sign == "*":
                res *= n
        return res
    
### FUNCTIONS ###

################

DEBUG = True
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("6/input.txt", 'r') as file:
#with open("6/test.txt", 'r') as file:
    rows = [line.rstrip("\n") for line in file]
print(rows)

# TRANSPOSE
new_rows = []
for i in range(len(rows[0])-1,-1,-1):
    new_row = ""
    for r in rows:
        new_row += r[i]
    new_rows.append(new_row)

# CHECK
for row in new_rows:
    assert(len(row)==len(new_rows[0]))

rows = new_rows
rows.append(" ") # to compute last group

groups = []
temp_sign = ""
temp_numbers = []

for i,r in enumerate(rows):
    r = str(r)
    if "+" in r:
        temp_sign = "+"
    elif "*" in r:
        temp_sign = "*"

    if r.replace(" ","") != "":
        temp_numbers.append(int(r.replace("+","").replace("*","").strip()))
    elif r.replace(" ","") == "":
        groups.append(Group(temp_sign, temp_numbers))
        temp_sign = ""
        temp_numbers = []

print("\n********\nrows =", rows,"\n********\n")
print("\n********\ngroups =", groups,"\n********\n")

res = 0
for g in groups:
    res += g.calculate()

print("\n********\nres =", res,"\n********\n")
