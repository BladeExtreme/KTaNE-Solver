from .other.header import header
import colorama as c  # type: ignore

def patchnotes():
    header()
    with open('ktanesolver/patchnotes.log', 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:
        print(line, end='')

    input()
