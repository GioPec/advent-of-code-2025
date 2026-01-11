res = 0

with open("2/input.txt", 'r') as file:
#with open("2/test.txt", 'r') as file:
    content = file.read().strip()
    ranges = content.split(",")
    
    for r in ranges:
        start = int(r.split("-")[0])
        end   = int(r.split("-")[1])
        
        ids = list(range(start, end+1))
        
        for id_int in ids:
            id_str = str(id_int)

            # ignore odd lenght IDs
            if len(id_str)%2!=0:
                continue

            # gestione len=2
            if len(id_str)==2:
                if id_str in ["11","22","33","44","55","66","77","88","99"]:
                    res+=id_int
                continue

            middle_index = int(len(id_str)/2)
            
            first_half  = id_str[:middle_index]
            second_half = id_str[middle_index:]

            if first_half == second_half:
                res += id_int

print("\n********\nres =", res,"\n********\n")