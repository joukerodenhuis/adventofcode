# Day 8! Some definitions on counting stuff, really.
# As of 28/5/2024 15:29 PM, answer is 1945 which is too low
# As of 28/5/2024 20:29 PM, answer is 1645 which is too low

AOCfile = open("C:\\Users\\Jouke Rodenhuis\\Github\\adventofcode\\AOC20158.txt")
AOCinput = AOCfile.readlines()
AOCfile.close()


dict = {"strl":0, "ml":0, "enc":0}
list = [AOCinput, dict]


# day 1 and day 2
def strlit(list):
    for line in list[0]:
        line = line.strip()
        list[1]["strl"] += len(line)
    return list


# day 1
def strmem(list):
    for line in list[0]:
        line = line.strip()
        ml = len(line) - 2
        skip = 0
        for i,letter in enumerate(line):
            match letter:
                case "\\":
                    if line[i-1] == "\\" and skip == 0:
                        skip = 1
                        continue
                    ml -= 1
                    if line[i+1] == "x":
                        ml -= 2
                    skip = 0
                    continue
                case _:
                    skip = 0
                    continue
        list[1]["ml"] += ml
    return list


# day 2
def strenc(list):
    enclist = ["\\", "\""]
    for line in list[0]:
        line.strip(" \n")
        newline = ""
        for i,letter in enumerate(line):
            match letter:
                case letter if letter in enclist:
                    newline = newline + "\\" + letter
                case _:
                    newline = newline + letter
        newline = '"' + newline + '"'
        list[1]["enc"] += len(newline) - 1
    return list



day = int(input("what day? 1 or 2 "))

list = strlit(list)

if day == 1:
    list = strmem(list)
    t = list[1]["strl"] - list[1]["ml"]
    print(t)



if day == 2:
    list = strenc(list)
    print(list[1]["enc"])
    print(list[1]["strl"])
    t = list[1]["enc"] - list[1]["strl"]
    print(t)