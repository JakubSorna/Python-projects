from random import randrange
def uniqueness_of_digits(string):
    for char in string:
        if string.count(char) > 1:
            return True
    return False
def insert_number():
    number = input("Enter your number:")
    if len(number) != 4 or uniqueness_of_digits(number):
        print("Enter number with 4 unique digits!")
        insert_number()
    else:
        return number
def random_number():
    number = set()
    while len(number) < 4:
        number.add(str(randrange(0, 10)))
    return list(number)

def cows(tip, list):
    cow = 0
    for i in tip:
        if i in list:
            cow += 1
    return cow

def bulls(tip, list):
    bulls = []
    for i in range(4):
        if tip[i] == list[i]:
            continue
        else:
            bulls.append(list[i])
    return bulls

def guessed_number():
    riddle = random_number()
    if riddle[0] == "0":
        guessed_number()
    else:
        return riddle

def game(tip, riddle):
    Bulls = 4 - len(bulls(tip, riddle))
    Cows = cows(tip, bulls(tip, riddle))
    result = dict(bulls = Bulls, cows = Cows)
    return result

def main():
    print("Hello there!", "_"*46, sep="\n")
    bc = [0,0]
    tip = "1111"
    riddle = guessed_number()
    result = game(tip, riddle)
    while result["bulls"] < 4:
        tip = insert_number()
        result = game(tip, riddle)
        print("_"*46,f">>> {tip}", sep = "\n")
        if result["bulls"] <= 1:
            bc[0] = "Bull"
        else:
            bc[0] = "Bulls"
        if result["cows"] <= 1:
            bc[1] = "Cow"
        else:
            bc[1] = "Cows"
        print(f'{bc[0]} = {result["bulls"]} {bc[1]} = {result["cows"]}', "_"*46, sep = "\n")
    else:
        print("_" * 46, f">>> {tip}", sep="\n")
        print(f'{bc[0]} = {result["bulls"]} {bc[1]} = {result["cows"]}', "_" * 46, sep="\n")
        print("YOU WIN!!!")

main()
