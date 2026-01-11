### FUNCTIONS ###

################

DEBUG = False
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("5/input.txt", 'r') as file:
#with open("5/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

fresh_list = rows[:rows.index("")]
id_list = rows[rows.index("")+1:]

for id in id_list:
    id = int(id)
    for couple in fresh_list:
        low  = int(couple[:couple.index("-")])
        high = int(couple[couple.index("-")+1:])
        if low<=id and id<=high:
            print(f"({low},{high}) {id}")
            res+=1
            break

print("\n********\nAccessible =", res,"\n********\n")