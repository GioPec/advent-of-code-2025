res = 0

with open("2/input.txt", 'r') as file:
#with open("2/test.txt", 'r') as file:
    content = file.read().strip()
    ranges = content.split(",")
    
    for r in ranges:
        start = int(r.split("-")[0])
        end   = int(r.split("-")[1])

        # to not add the same number twice (think 22222222)
        already_added_in_this_range = []
        
        ids = list(range(start, end+1))
        
        for id_int in ids:
            id_str = str(id_int)

            middle_index = int(len(id_str)/2)

            # cycle all possible substrings lenght: from 1 to len(id_str)/2
            for substr_len in range(1,middle_index+1):

                # skip impossible lengths (that do not perfectly divide)
                if len(id_str) % substr_len != 0:
                    continue

                indexes = list(range(0,len(id_str),substr_len))

                substrings = []

                for i in range(len(indexes)-1):
                    substrings.append(id_str[indexes[i]:indexes[i+1]])
                substrings.append(id_str[indexes[i+1]:])

                # print(id_str, indexes)
                # print(substrings)
                # print()
                
                substrings.sort()
                if substrings[0] == substrings[-1]:
                    if id_int not in already_added_in_this_range:
                        print(id_int)
                        res+=id_int
                        already_added_in_this_range.append(id_int)

print("\n********\nres =", res,"\n********\n")