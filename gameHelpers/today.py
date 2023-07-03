#Functions and modules to play todays game

from . import scrapping_paraulogic as sp
from . import beautiful_print as bp
from . import game

import importlib
importlib.reload(sp)
importlib.reload(bp)
importlib.reload(game)

def play_today():
    #Get the words and letters
    words, letters = game.get_game_data()

    #Print the letters
    bp.print_letters(letters)
    #bp.print_letters_hex(letters, bp.TextColour.YELLOW, bp.TextColour.CYAN)

    #Print max points and words in the game
    maxPoints, maxWords = game.count_max_points(words, letters)
    bp.print_word(f'Max points:', bp.TextColour.BOLD + bp.TextColour.CYAN, end=' ')
    bp.print_word(f'{maxPoints}', bp.TextColour.BOLD + bp.TextColour.GREEN, end=' ')
    bp.print_word(f'Words:', bp.TextColour.BOLD + bp.TextColour.CYAN, end=' ')
    bp.print_word(f'{maxWords}', bp.TextColour.BOLD + bp.TextColour.GREEN, end='\n')


    user_input = ""
    totalPoints = 0
    previousWords = []
    while user_input != "q":
        user_input = game.ask_word()

        if user_input in previousWords:
            bp.print_word(f'Word already used', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')
            continue

        if user_input == "q":
            bp.print_word(f'Final Points:', bp.TextColour.BOLD + bp.TextColour.YELLOW, end=' ')
            bp.print_word(f'{totalPoints}', bp.TextColour.BOLD + bp.TextColour.GREEN, end='\n')

            #Print the words
            bp.print_word(f'Words:', bp.TextColour.BOLD + bp.TextColour.CYAN, end=' ')
            for word in previousWords:
                bp.print_word(f'{word}', bp.TextColour.BOLD + bp.TextColour.GREEN, end=' ')
            print() #Line

            break

        if game.check_valid(user_input, letters, words):
            previousWords.append(user_input)
            points, esTuti = game.count_points(user_input, letters)
            totalPoints += points
            if esTuti:
                bp.print_word(f'TUTTI', bp.TextColour.BOLD + bp.TextColour.CYAN, end=' ')
                bp.print_word(f'Points:', bp.TextColour.BOLD + bp.TextColour.YELLOW, end=' ')
                bp.print_word(f'{points}', bp.TextColour.BOLD + bp.TextColour.GREEN, end=' ')
                bp.print_word(f'Total:', bp.TextColour.BOLD + bp.TextColour.YELLOW, end=' ')
                bp.print_word(f'{totalPoints}', bp.TextColour.BOLD + bp.TextColour.GREEN, end='\n')
            else:
                bp.print_word(f'Points:', bp.TextColour.BOLD + bp.TextColour.YELLOW, end=' ')
                bp.print_word(f'{points}', bp.TextColour.BOLD + bp.TextColour.GREEN, end=' ')
                bp.print_word(f'Total:', bp.TextColour.BOLD + bp.TextColour.YELLOW, end=' ')
                bp.print_word(f'{totalPoints}', bp.TextColour.BOLD + bp.TextColour.GREEN, end='\n')
        else:
            bp.print_word(f'Invalid word', bp.TextColour.BOLD + bp.TextColour.RED, end='\n')