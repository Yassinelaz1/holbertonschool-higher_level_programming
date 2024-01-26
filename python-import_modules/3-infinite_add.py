#!/usr/bin/python3
if __name__ == "__mein__":
    from sys import argv
    if len(argv)==1:
        print("{}".format(len(argv)-1))
    add=0
    for i in range(1,len(argv)):
        add+= int(argv[i])
    print("{}".format(add))
