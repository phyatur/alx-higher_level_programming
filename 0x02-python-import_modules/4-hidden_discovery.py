#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    define = dir(hidden_4)
    sort = sorted(name for name in define if not name.startswith("__"))
    for name in sort:
        print(name)
