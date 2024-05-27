#The elf had too much eggnog apparently. I want whatever he's having.

# Getting the directions and changing it to a normal string
AOCfile = open("C:\\Users\\Jouke Rodenhuis\\Github\\adventofcode\\AOC20153.txt")
AOCinput = AOCfile.readlines()
AOCfile.close()
AOCstr = ""
for element in AOCinput:
    AOCstr = AOCstr + element

# The dictionary below is used for keeping track of the data. I am not happy with how its implemented in the PresentAmount function.
# I don't yet know how to make that better
TheDict = {"visitedhouses":[[0,0]],"amount":int(1),"xSanta":int(0),"xRobo":int(0),"ySanta":int(0),"yRobo":int(0),"SR":int(0)}

# Main function. It loops through the directions of the AOCinput file and determines what needs to happen. 
# Calls for another function below

def CoordinateHandler(TheDict):
    iteration = 1
    for direction in AOCstr:
        if TheDict["SR"] == 0:
            TheDict["SR"] = 1
            match direction:
                case ">":
                    TheDict["xSanta"] += 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "<":
                    TheDict["xSanta"] -= 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "^":
                    TheDict["ySanta"] += 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "v":
                    TheDict["ySanta"] -= 1
                    TheDict = PresentAmount(TheDict)
                    continue
        if TheDict["SR"] == 1:
            TheDict["SR"] = 0
            match direction:
                case ">":
                    TheDict["xRobo"] += 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "<":
                    TheDict["xRobo"] -= 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "^":
                    TheDict["yRobo"] += 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case "v":
                    TheDict["yRobo"] -= 1
                    TheDict = PresentAmount(TheDict)
                    continue
                case _:
                    continue
        iteration += 1
    return TheDict

# The function below keeps track of how many houses received at least one present given a coordinate

def PresentAmount(TheDict):
    if TheDict["visitedhouses"].count([TheDict["xSanta"],TheDict["ySanta"]]) == 0 and TheDict["SR"] == 0:
        TheDict["visitedhouses"].append([TheDict["xSanta"],TheDict["ySanta"]])
        TheDict["amount"] += 1
    if TheDict["visitedhouses"].count([TheDict["xRobo"],TheDict["yRobo"]]) == 0 and TheDict["SR"] == 1:
        TheDict["visitedhouses"].append([TheDict["xRobo"],TheDict["yRobo"]])
        TheDict["amount"] += 1
    return TheDict

TheDict = CoordinateHandler(TheDict)
print("")
print(TheDict["visitedhouses"])
print(TheDict["amount"])
print("")

