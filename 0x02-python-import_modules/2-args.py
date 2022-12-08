#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    arg_len_string = "argument" if arg_len == 1 else "arguments"
    arg_len_punc = "." if arg_len == 0 else ":"

    print(f"{arg_len} {arg_len_string}{arg_len_punc}")

    for i in range(1, arg_len + 1):
        print(f"{i}: {argv[i]}")
