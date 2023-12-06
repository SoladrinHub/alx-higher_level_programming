#!/usr/bin/bash
if __name__ = "__main__":
    from hidden_4 import *
    myfunc = dir()
    for i in range(0, len(myfunc)):
        if myfunc[i][:2] != "__":
            print("{}".format(myfunc[i]))
