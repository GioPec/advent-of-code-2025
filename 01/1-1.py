DEBUG = False

with open("1/input.txt", 'r') as file:
#with open("1/test.txt", 'r') as file:
    lines = [line.rstrip() for line in file]

if DEBUG: print("start...")

password = 0
dial = 50

for line in lines:
    direction = line[0]
    amount = line[1:]
    if DEBUG: print(direction, amount)
    amount = int(amount)
    assert direction in ["L", "R"]
    assert isinstance(amount, int)

    if DEBUG: print("Moving",direction,"by",amount)

    # R +
    if direction == "R":
        dial += amount

    # L -
    elif direction == "L":
        dial -= amount
        
    dial = dial % 100
    if dial == 0:
        password+=1

    if DEBUG: print("Dial is now in",dial)
    if DEBUG: print("")
        

print("The password is", password)