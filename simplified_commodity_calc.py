#!/usr/bin/python

def main():
    x = raw_input("Type buy price and hit enter: ")
    if len(x) <= 2:
        x = int(x)
        x = x + 1
        x = str(x)
        print("Set your buy price to %s.") % (x)
        x = int(x)
        y = x + 15
        y = str(y)
        z = x * 5
        z = str(z)
        print("Set your selling price to %s.") % (z)
        print("Set your use cost to %s.") % (y)
        print(" \n")
        main()
    elif len(x) == 3:
        x = int(x)
        x = x + 1
        x = str(x)
        print("Set your buy price to %s.") % (x)
        x = int(x)
        y = x + 70
        y = str(y)
        z = x * 5
        z = str(z)
        print("Set your selling price to %s.") % (z)
        print("Set your use cost to %s.") % (y)
        print(" \n")
        main()
    else:
        x = int(x)
        x = x + 1
        x = str(x)
        print("Set your buy price to %s.") % (x)
        x = int(x)
        y = x + 200
        y = str(y)
        z = x * 5
        z = str(z)
        print("Set your selling price to %s.") % (z)
        print("Set your use cost to %s.") % (y)
        print(" \n")
        main()

main()
