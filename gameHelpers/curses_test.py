#Test the curses module

import curses
from curses import wrapper

def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()

    stdsrc.getch()

def start_curses():
    wrapper(main)