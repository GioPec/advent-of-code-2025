### FUNCTIONS ###


################

DEBUG = False
res = 0

if DEBUG: print("Start...")

### MAIN ###

with open("5/input.txt", 'r') as file:
#with open("5/test.txt", 'r') as file:
    rows = [line.rstrip() for line in file]

fresh_list_ranges_string = rows[:rows.index("")]

if DEBUG: print(f"starting")
if DEBUG: print(len(fresh_list_ranges_string))

# CONVERT TO INT TUPLES
fresh_list_ranges = []
for r in fresh_list_ranges_string:
    start = int(r.split("-")[0])
    end   = int(r.split("-")[1])
    fresh_list_ranges.append((start,end))

fresh_list_ranges.sort()    # normal sort seems to work
if DEBUG: print(fresh_list_ranges)

# REMOVE DUPLICATES
for i,r in enumerate(fresh_list_ranges):
    if i != 0:
        if r == fresh_list_ranges[i-1]:
            fresh_list_ranges.remove(r)

if DEBUG: print(len(fresh_list_ranges))

# REMOVE SELF-CONTAINED
for i,r in enumerate(fresh_list_ranges):
    start = r[0]
    end   = r[1]

    for j,r2 in enumerate(fresh_list_ranges):
        start2 = r2[0]
        end2   = r2[1]

        if i!=j and start2>=start and end2<=end:
            fresh_list_ranges.remove(fresh_list_ranges[j])

if DEBUG: print(fresh_list_ranges)
if DEBUG: print(len(fresh_list_ranges))

# GIVEN RANGE, FIND MAX END OF ALL THE STARTING INSIDE IT: 
# THAT IS THE NEW END OF THE RANGE
new_fresh_list_ranges = []

for i,r in enumerate(fresh_list_ranges):
    start = r[0]
    end   = r[1]

    # I skip ranges alreaddy included in the new big range
    if len(new_fresh_list_ranges) != 0:
        if start>=(new_fresh_list_ranges[-1])[0] and start<=(new_fresh_list_ranges[-1])[1]:
            continue

    new_start = start
    new_end = end

    for j,local_r in enumerate(fresh_list_ranges):
        local_start = local_r[0]
        local_end   = local_r[1]

        if i!=j and local_start>=start and local_start<=new_end:
            if local_end>new_end:
                new_end = local_end

    new_fresh_list_ranges.append((new_start,new_end))

if DEBUG: print(new_fresh_list_ranges)
if DEBUG: print(len(new_fresh_list_ranges))

# COUNT
res = 0

for r in new_fresh_list_ranges:
    start = r[0]
    end   = r[1]
    res += (end-start+1)

print("\n********\nAccessible =", res,"\n********\n")