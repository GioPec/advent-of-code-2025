# Note
# This code is the generalized version of the problem 3.
# As such, it also solves the 3.1 by just changing BATTERIES_TO_CHOOSE to 2
#
### FUNCTIONS ###

def two_nums_to_int(n1, n2):
    return int(str(n1)+str(n2))

def array_of_strings_to_int(l):
    res = ""
    for n in l:
        res += str(n)
    return int(res)

def better_array_of_strings_to_int(l):
    return int(''.join(map(str, l)))

################

DEBUG = False
BATTERIES_TO_CHOOSE = 12
highest_total_joltage = 0

if DEBUG: print("Start...")

### MAIN ###

with open("3/input.txt", 'r') as file:
#with open("3/test.txt", 'r') as file:
    banks = [line.rstrip() for line in file]

for bank in banks:
    assert len(bank) > BATTERIES_TO_CHOOSE

    highest = [1] * BATTERIES_TO_CHOOSE
    highest_previous_index = -1

    for b in range(BATTERIES_TO_CHOOSE):
        for i in range(len(bank)-BATTERIES_TO_CHOOSE+b,highest_previous_index,-1):
            if int(bank[i]) >= highest[b]:
                highest[b] = int(bank[i])
                highest_previous_index = i
                if DEBUG: print("New highest number",highest[b],"!")

    highest_bank_joltage = better_array_of_strings_to_int(highest)
    if DEBUG: print(bank, highest_bank_joltage)
    highest_total_joltage += highest_bank_joltage

print("\n********\nHighest total joltage =", highest_total_joltage,"\n********\n")