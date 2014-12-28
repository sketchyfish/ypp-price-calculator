#!/usr/bin/python

b = []
a = open('C:/Python27/Myscripts/project/commodities_list.txt', 'r')

def main():
    for each_item in a:
        b.append(each_item)
        print(each_item)
    print(b)

main()
