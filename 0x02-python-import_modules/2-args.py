#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print(f"0 arguments.")
    elif len_arg == 1:
        print(f"{len_arg} argument:")
        print(f"{len_arg}: {sys.argv[len_arg]}")
    else:
        print(f"{len_arg} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
