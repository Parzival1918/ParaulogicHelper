#!/opt/homebrew/bin/python3
#CHANGE FIRST LINE TO YOUR PYTHON PATH

#Programa per jugar al paraulogic en el terminal, o obtenir els resultats del joc del dia

import argparse as ap

#Local imports
from gameHelpers import today
from gameHelpers import date
from gameHelpers import beautiful_print as bp
from gameHelpers import curses_test

import importlib
importlib.reload(today)
importlib.reload(bp)
importlib.reload(date)
importlib.reload(curses_test)

parser = ap.ArgumentParser()

parser.add_argument('-d', '--date', type=str, help='Date of the game in format YYYY-MM-DD')
parser.add_argument('-t', '--today', help='Play today\'s game', action='store_true')
parser.add_argument('-j', '--json-output', help='Output the game data as json', action='store_true')
parser.add_argument('-c', '--curses', help='Curses module test', action='store_true')

args = parser.parse_args()

if args.curses:
    curses_test.start_curses()
    exit(0)

if args.today:
    bp.print_word('Today\'s game: ', bp.TextColour.YELLOW, end='\n')
    today.play_today()
elif args.date:
    bp.print_word('Unsupported function "-d/--date"', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')
    exit(0)
    # bp.print_word('Game of ', bp.TextColour.YELLOW)
    # bp.print_word(args.date, bp.TextColour.BOLD + bp.TextColour.BLUE, end=':\n')
    # date.play_date(args.date)