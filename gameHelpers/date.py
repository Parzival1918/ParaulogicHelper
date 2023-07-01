#Function to play games from any date

from . import scrapping_paraulogic as sp
from . import beautiful_print as bp

import importlib
importlib.reload(sp)
importlib.reload(bp)

def play_date(date: str):
    #Get the words
    print(sp.URL_DATE + date)
    rawJSON = sp.get_raw_json(sp.URL_DATE + date)
    print(rawJSON)
    #print(rawJSON['paraules'])
    # letters = rawJSON['l']
    # words = rawJSON['p']
    # #print(words)

    # #Print the letters
    # bp.print_letters(letters)