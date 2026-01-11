DEBUG = False

with open("1/input.txt", 'r') as file:
#with open("1/test.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

if DEBUG: print("Start...\n")
if DEBUG: print("Dial is now in 50")

password = 0
dial = 50

for line in lines:
    direction = line[0]
    amount = line[1:]
    #if DEBUG: print(direction, amount)
    amount = int(amount)
    if DEBUG: assert direction in ["L", "R"]
    if DEBUG: assert isinstance(amount, int)

    if DEBUG: print("Moving",direction,"by",amount)

    olddial = dial
    if DEBUG: assert olddial in range(0,100)

    # R +
    if direction=="R":
        dial+=amount

    # L -
    elif direction=="L":
        dial-=amount

    if olddial>0:
        if dial<0:
            if DEBUG: assert direction=="L"
            password+=abs(dial//100)
            # serve questa cosa nel caso finale negativo (perché -100//100=1 ma io voglio 2)
            if dial%100==0:
                password+=1
        elif dial==0:
            if DEBUG: assert direction=="L"
            password+=1
        elif dial>0:
            password+=abs(dial//100)

    elif olddial==0:
        if dial<0:
            password+=(abs(dial//100)-1)
            # serve questa cosa nel caso finale negativo (perché -100//100=1 ma io voglio 2)
            if dial%100==0:
                password+=1
        elif dial==0:
            password+=0
        elif dial>0:
            password+=abs(dial//100)

    dial = dial % 100

    if DEBUG: print("Dial is now in",dial)
    if DEBUG: print("PASSWORD IS",password)
    if DEBUG: print("")
        

print("The password is", password)