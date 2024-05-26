# There's so many lights on the grid, the imaginary comic artist that draws my life says they no longer has any bulbs to give me ideas!

# 0
AOCinput = open("C:\\Users\\Jouke Rodenhuis\\Github\\adventofcode\\AOC20156.txt").readlines()

# 1
data = {"l-on":0, "do":"", "l":"", "x1":0, "y1": 0, "x2":0, "y2":0}

# 2
instruc = ["turn on", "toggle", "turn off"]

# 3
lights = {"0,0":"off", }

list = [AOCinput, data, instruc, lights]


# So I guess I want a dict that contains all light coordinates as a key, with all their respective values set to off. Big dict time. Sorry.
def lightemup(lights):
    for x in range(1, 1000):
        xl = ""
        xl = xl + str(x)
        for y in range(1, 1000):   
            yl = ""
            yl = yl + str(y)
            t = xl + "," + yl
            lights.update({t:"off"})
    return(lights)

lights = lightemup(lights)
list[3] = lights


# This function resets all temporary key:values in the data dict
def rst(list):
    list[1]["do"] = ""
    list[1]["l"] = ""
    list[1]["x1"] = 0
    list[1]["y1"] = 0
    list[1]["x2"] = 0
    list[1]["y2"] = 0
    return(list)


#This function extracts the four coordinates from the specific line the mainfunc is processing
def inputhandler(list):
    i = 0
    l = list[1]["l"]
    match l:
        case l if l.find("turn off") != -1:
            l = l.lstrip("turn off ")
            l = l.rstrip(" \n")
            list[1]["do"] = list[2][2]
        case l if l.find("turn on") != -1:
            l = l.lstrip("turn on")
            l = l.rstrip(" \n")
            list[1]["do"] = list[2][0]
        case l if l.find("toggle") != -1:
            l = l.lstrip("toggle ")
            l = l.rstrip(" \n")
            list[1]["do"] = list[2][1]
    c = l.split(" through ")
    c1 = c[0].split(",")
    c2 = c[1].split(",")
    list[1]["x1"] = c1[0]
    list[1]["y1"] = c1[1]
    list[1]["x2"] = c2[0]
    list[1]["y2"] = c2[1]
    return(list)

#This mainfunc calls for the other functions and directly handles the "l-on" keyvalue pair
def main(list):
    for l in list[0]:
        list = rst(list)
        list[1]["l"] = l
        inputhandler(list)
        x1 = int(list[1]["x1"])
        x2 = int(list[1]["x2"])
        y1 = int(list[1]["y1"])
        y2 = int(list[1]["y2"])
        match list[1]["do"]:
            case "turn off":
                for x in range(x1, x2):
                    for y in range(y1, y2):
                        key = str(x) + "," + str(y)
                        list[3][key] = "off"
                        if list[1]["l-on"] > 0:
                                    list[1]["l-on"] -= 1
            case "toggle":
                for x in range(x1, x2):
                    for y in range(y1, y2):
                        key = str(x) + "," + str(y)
                        match list[3][key]:
                            case "off":
                                list[3][key] = "on"
                                list[1]["l-on"] += 1
                            case "on":
                                list[3][key] = "off"
                                if list[1]["l-on"] > 0:
                                    list[1]["l-on"] -= 1
            case "turn on":
                for x in range(x1, x2):
                    for y in range(y1, y2):
                        key = str(x) + "," + str(y)
                        list[3][key] = "on"
                        list[1]["l-on"] += 1
            case _:
                print("Um, the do key has a value that is weird. How did you do that?")
                exit()
    return list

list = main(list)
print(list[1]["l-on"])