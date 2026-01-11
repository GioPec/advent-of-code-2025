# Note
# This is the first working solution.
# The general solution for this problem can be found in 3-2.
# 
### FUNCTIONS ###

def two_nums_to_int(n1, n2):
    return int(str(n1)+str(n2))

################

DEBUG = False
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("3/input.txt", 'r') as file:
#with open("3/test.txt", 'r') as file:
    banks = [line.rstrip() for line in file]

for bank in banks:
    assert len(bank) > 2

    highest = two_nums_to_int(bank[-2],bank[-1])
    highest_decine_index = -2
    highest_unita_index  = -1
    highest_decine = int(bank[highest_decine_index])
    highest_unita  = int(bank[highest_unita_index])

    for i in range(len(bank)-2,-1,-1):
        if int(bank[i]) >= highest_decine:
            highest_decine = int(bank[i])
            highest_decine_index = i
            if DEBUG: print("New highest decina!", highest_decine)

    for j in range(len(bank)-1,highest_decine_index,-1):
        if int(bank[j]) >= highest_unita:
            highest_unita = int(bank[j])
            highest_unita_index = j
            if DEBUG: print("New highest unita!", highest_unita)

    highest = two_nums_to_int(highest_decine,highest_unita)
    if DEBUG: print(bank, highest)
    res+=highest

print("\n********\nres =", res,"\n********\n")