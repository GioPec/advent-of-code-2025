### FUNCTIONS ###

def find_highest_fresh(fresh_list):
    highest = 0
    for couple in fresh_list:
        local_high = int(couple[couple.index("-")+1:])
        if local_high > highest:
            highest = local_high
    return highest

def fill_dict(fresh_dict, fresh_list):
    for couple in fresh_list:
        low  = int(couple[:couple.index("-")])
        high = int(couple[couple.index("-")+1:])
        for n in range(low, high+1):
            fresh_dict[n] = True


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

highest_fresh = find_highest_fresh(fresh_list)
fresh_dict = {n: False for n in range(highest_fresh+1)}
fill_dict(fresh_dict, fresh_list)

for id in id_list:
    id = int(id)
    if id in fresh_dict and fresh_dict[id]:
        res+=1

if DEBUG: print(fresh_dict)

print("\n********\nAccessible =", res,"\n********\n")