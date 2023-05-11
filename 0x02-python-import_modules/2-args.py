#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    args_num = len(argv) - 1

    if args_num == 1:
        print("{} argument".format(args_num), end="")
    else:
        print("{} arguments".format(args_num), end="")

    if args_num == 0:
        print(".")
    else:
        print(":")

    for index in range(1, len(argv)):
        arg = argv[index]
        print("{}: {}".format(index, arg))
