#Functions to play the game

from . import beautiful_print as bp

import importlib
importlib.reload(bp)

#Ask for word
def ask_word():
    bp.print_word(' > ', bp.TextColour.BOLD + bp.TextColour.CYAN, end='')
    return input(bp.print_word('Enter a word: ', bp.TextColour.BOLD + bp.TextColour.GREEN, returnString=True))

#Check if the word is valid
def check_valid(word: str, letters: str):
    if len(word) < 3:
        bp.print_word('The word must be at least 3 letters long', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')
        return False
    else:
        if letters[-1] not in word:
            bp.print_word('The word must contain the centre letter', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')
            return False
        else:
            #Check that the letters in the word are all in the letters
            for letter in word:
                if letter not in letters:
                    bp.print_word('The word must contain only the letters given', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')
                    return False
            return True