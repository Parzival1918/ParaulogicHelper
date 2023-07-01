#Functions and modules to play todays game

from . import scrapping_paraulogic as sp
from . import beautiful_print as bp
from . import game

import importlib
importlib.reload(sp)
importlib.reload(bp)
importlib.reload(game)

def play_today():
    #Get the words
    rawJSON = sp.get_raw_json()
    #print(rawJSON)
    #print(rawJSON['paraules'])
    letters = rawJSON['l']
    words = rawJSON['p']
    #print(words)

    #Print the letters
    #bp.print_letters(letters)
    bp.print_letters_hex(letters, bp.TextColour.YELLOW, bp.TextColour.CYAN)

    user_input = ""
    while user_input != "exit":
        user_input = game.ask_word()
        if game.check_valid(user_input, letters):
            pass