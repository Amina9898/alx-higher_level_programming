#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4
    import sys

    names = dir(hidden_4)

    for name in sorted(names):
        if not name.startswith("__"):
            print("{}".format(name))