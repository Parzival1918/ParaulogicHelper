#!/opt/homebrew/bin/python3
#CHANGE FIRST LINE TO YOUR PYTHON PATH

#Programa per jugar al paraulogic en el terminal, o obtenir els resultats del joc del dia

import argparse as ap

#Local imports
from gameHelpers import today
from gameHelpers import beautiful_print as bp

import importlib
importlib.reload(today)
importlib.reload(bp)

parser = ap.ArgumentParser()

# parser.add_argument('-t', '--today', help='Play today\'s game', action='store_true')
parser.add_argument('-j', '--json-output', help='Output the game data as json', action='store_true')

args = parser.parse_args()

bp.print_word('Today\'s game: ', bp.TextColour.YELLOW, end='\n')
today.play_today()