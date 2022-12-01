#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i+1, 10):
        print(f"{i}{n}", end="")
        print("{}".format(", " if i != 8 or n != 9 else "\n"), end="")
