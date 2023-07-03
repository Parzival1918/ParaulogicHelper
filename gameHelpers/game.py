#Functions to play the game

from . import beautiful_print as bp
from . import scrapping_paraulogic as sp

import importlib
importlib.reload(bp)
importlib.reload(sp)

#Ask for word
def ask_word():
    bp.print_word(' > ', bp.TextColour.BOLD + bp.TextColour.CYAN, end='')
    return input(bp.print_word('Enter a word: ', bp.TextColour.BOLD + bp.TextColour.GREEN, returnString=True)).strip().lower()

#Check if the word is valid
def check_valid(word: str, letters: str, words: list[str]):
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
                
            #Check that the word is in the list of words
            if word not in words:
                return False
            
            return True
        
#Function to get the words and letters from the game
def get_game_data():
    rawJSON = sp.get_raw_json()
    letters = rawJSON['l']
    words = rawJSON['p']
    return words, letters

#Count the points of a word
def count_points(word: str, letters: list[str]):
    points = 0

    letterCount = 0
    esTuti = False
    for letter in letters:
        if letter in word:
            letterCount += 1

    if letterCount == len(letters):
        points += 10
        esTuti = True

    if len(word) == 3:
        return points + 1, esTuti
    elif len(word) == 4:
        return points + 2, esTuti
    elif len(word) > 4:
        return points + len(word), esTuti
    
#Count max points in the game
def count_max_points(words: list[str], letters: list[str]):
    points = 0
    for word in words:
        if check_valid(word, letters, words):
            points += count_points(word, letters)[0]

    return points, len(words)