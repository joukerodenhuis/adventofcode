# AOC20155! Yee boi

# 0
AOCinput = open("C:\\Users\\Jouke Rodenhuis\\Github\\adventofcode\\AOC20155.txt").readlines()

# 1
data = {"nice":0, "aofvow":0, "dble":0, "bad":0, "odo":0}

# 2
req = {"vow":"aeiou", 1:"ab", 2:"cd", 3:"pq", 4:"xy"}

# 3
temp = {"l":"","x":"","i":""}

# 4
test = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]

# revolver ocelot
list = [AOCinput, data, req, temp, test]


# Resets all key values of dicts in the list that are temporary for every iteration back to their starting values.
def rst(list):
    list[1]["aofvow"] = 0
    list[1]["dble"] = 0
    list[1]["bad"] = 0
    list[1]["odo"] = 0
    list[3]["l"] = ""
    list[3]["x"] = ""
    list[3]["i"] = ""
    return list


# Main for loops that sends the list to the different functions
# For part one, call func isdble, isbad, isvow.
# For part two, call func isdble, isodo.
def main(list):
    for l in list[0]:
        list[3]["l"] = str(l)
        for i,x in enumerate(l):
            list[3]["i"] = int(i)
            list[3]["x"] = str(x)
            if list[1]["dble"] == 0:
                list = is2p(list)
            if list[1]["odo"] == 0:
                list = isodo(list)
            if list[1]["odo"] > 0 and list[1]["dble"] > 0:
                break
        list = creq(list)
        list = rst(list)
    return(list)


# This funcion checks if all requirements for a nice line have been met
# For part one, check the aofvow, dble, and bad keyvalues. Change dble check value to 1
# For part two, check the dble and odo keyvalues. Change dble check value to 2
def creq(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if list[1]["dble"] >= 1 and list[1]["odo"] >= 1:
        list[1]["nice"] += 1
    return list


# This function checks if any bad combination of two letters exists within the line of the current iteration of the mainfunc
# Function only relevant for part one
def isbad(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if i + 1 >= len(l):
        return(list)
    t = x + l[ i + 1 ]
    match t:
        case t if t == list[2][1]:
            list[1]["bad"] += 1
        case t if t == list[2][2]:
            list[1]["bad"] += 1
        case t if t == list[2][3]:
            list[1]["bad"] += 1
        case t if t == list[2][4]:
            list[1]["bad"] += 1
    return list   


# This function checks if any double characters seperated by one character exist. aaa counts, aba counts, and so on. 
# Function only relevant for part two
def isodo(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if i + 2 >= len(l):
        return(list)
    if l[i + 2] == x:
        list[1]["odo"] += 1
    return list

# This function checks if any double characters exist within the line of the mainfunc
# Function only relevant for part one
def isdble(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if i + 1 == x:
        if i + 1 >= len(l):
            return(list)
        if l[i + 1] != x:
            list[1]["dble"] += 1
    return list

# This function checks if any pair of letters next to eachother in a line is present twice within the line without overlap with itself
# xxyxx would be an "odo" and an "is2p" because xx is present twice, and there is xyx. aaa is an "odo", but not an "is2p".
# Function only relevant for part two
def is2p(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if i + 1 >= len(l):
        return(list)
    t = x + l[i+1]
    for d,c in enumerate(l):
        if d < i + 2:
            continue
        if c == t[0]:
            if d + 1 >= len(l):
                return list
            if l[d + 1] == t[1]:
                if d + 2 >= len(l):
                    list[1]["dble"] += 1
                    return(list)
                if t[0] == t[1] and l[d+2] == t[0]:
                    return(list)
                list[1]["dble"] += 1
                return(list)
    return(list)

# This function counts how many vowels exist within the line of the mainfunc
# Function only relevant for part one
def isvow(list):
    l = list[3]["l"]
    x = list[3]["x"]
    i = list[3]["i"]
    if x in list[2]["vow"]:
        list[1]["aofvow"] += 1
    return list

list = main(list)
print(list[1]["nice"])