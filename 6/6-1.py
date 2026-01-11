### FUNCTIONS ###

################

DEBUG = True
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("6/input.txt", 'r') as file:
#with open("6/test2.txt", 'r') as file:
    raw_rows = [line.rstrip() for line in file]

# READ
rows = []
for i,r in enumerate(raw_rows):
    elem = r.split(" ")
    if elem != "": 
        if i==len(raw_rows)-1:
            rows.append([e for e in elem if e != ""])
        else:
            rows.append([int(e) for e in elem if e != ""])

# CHECK
for row in rows:
    assert(len(row)==len(rows[0]))

res = 0

for i in range(len(rows[-1])):
    sign = (rows[-1])[i] # exclude sign
    temp = 0 if sign=="+" else 1 # init temp
    for j,r in enumerate(rows[:-1]):
        if sign == "+":
            temp += r[i]
        elif sign == "*":
            temp *= r[i]
    res += temp

print("\n********\nAccessible =", res,"\n********\n")