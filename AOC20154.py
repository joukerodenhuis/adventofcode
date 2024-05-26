HashDict = {
"A":0, 
"Amount":0, 
"AOCinput":"bgvyzdsv", 
"AOCanswer":"", 
"Choice":"", 
"Hash":"", 
"Number":1, 
"Testinput1":"abcdef", 
"Testanswer1":"abcdef609043", 
"Testinput2":"pqrstuv", 
"Testanswer2":"pqrstuv1048970", 
"ToHash":""
}

print("")
print("Choose AOC, T1, T2 to either test or provide an answer to the puzzle")
print("")
HashDict["Choice"] = input()
print("")

import hashlib

def Main(HashDict):
    while HashDict["A"] == 0:
        HashDict = Hasher(HashDict)
        TryHash = HashDict.get("Hash")
        for element in HashDict.get("Hash"):
            match element:
                case "0":
                    HashDict["Amount"] += 1
                case _:
                    if HashDict["Amount"] >= 6:
                        HashDict["A"] = 1
                        break
                    if HashDict["Amount"] < 6:
                        HashDict["Amount"] = 0
                        HashDict = NumberGenerator(HashDict)
                        break
    return HashDict

def Hasher(HashDict):
    match HashDict["Choice"]:
        case "T1":
            HashDict["ToHash"] = HashDict["Testinput1"] + str(HashDict["Number"])
            HashDict["Hash"] = hashlib.md5((HashDict["ToHash"]).encode('utf-8')).hexdigest()
        case "T2":
            HashDict["ToHash"] = HashDict["Testinput2"] + str(HashDict["Number"])
            HashDict["Hash"] = hashlib.md5((HashDict["ToHash"]).encode('utf-8')).hexdigest()
        case "AOC":
            HashDict["ToHash"] = HashDict["AOCinput"] + str(HashDict["Number"])
            HashDict["Hash"] = hashlib.md5((HashDict["ToHash"]).encode('utf-8')).hexdigest()
        case _:
            print("You didn't pick AOC, T1, or T2. Please try again")
    return HashDict

def NumberGenerator(HashDict):
    HashDict["Number"] += 1
    return HashDict

HashDict = Main(HashDict)
print(HashDict)