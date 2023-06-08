#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print(f"{length} arguments:")
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
