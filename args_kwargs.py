#! usr/bin/env python3
"""demo to explain args kwargs"""

__author__ = "Fenna Feenstra"

import sys

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def print_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(k, v)


def main():
    # first with *args
    args = ("hi", 1,6)
    test_args_kwargs(*args)

    # now with **kwargs:
    kwargs = {"arg3":1,
              "arg2":"hi",
              "arg1":6}
    test_args_kwargs(**kwargs)

    # use keywords
    print_kwargs(arg3=1, arg2="hi", arg1=6)

    return 0

if __name__ == "__main__":
    exitcode = main()
    sys.exit(exitcode)
