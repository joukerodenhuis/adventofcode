# This is for day 2 of the puzzles for the adventofcode2015 event

l = 1
w = 1
h = 10
area = 0
Numbers = "1234567890"

AOCfile = open("C:\\Users\\Jouke Rodenhuis\\Github\\adventofcode\\AOC20152.txt")
AOCinput = AOCfile.readlines()
AOCfile.close()

def FileHandler(area):
        a = 0
        area = 0
        dimensionlist = []
        for line in AOCinput:
            l = 0
            w = 0
            h = 0
            for index, dimension in enumerate(line.strip().split("x")):
                dimension == int(dimension)
                if l == 0:
                    l = int(dimension)
                    continue
                if w == 0:
                    w = int(dimension)
                    continue
                if h == 0:
                    h = int(dimension)
                    continue
            area = area + Calc(l,w,h)
            a += 1
        print(a)
        return area
            



def Calc(l,w,h):
    arealist = [ l, w, h ]
    arealist.sort()
    area = 2 * arealist[0] + 2 * arealist[1] + l * w * h
    return area

area = FileHandler(area)
print(area)
AOCinput.close