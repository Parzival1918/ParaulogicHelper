#Functions to print with colours and format

#Text colour class
class TextColour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

#Print a word with a colour
def print_word(word: str, colour: TextColour = TextColour.END, end: str = "", returnString: bool = False):
   string = colour + word + TextColour.END
   if returnString:
      return string + end
   else:
      print(string, end=end)

#Print the letters of paraulogic
def print_letters(letters: list[str]):
   print_word(' |-> Letters: ')
   for pos,letter in enumerate(letters):
      if pos+1 == len(letters):
         print_word(letter.upper(), colour = TextColour.BOLD + TextColour.CYAN, end='\n')
      else:
         print_word(letter.upper(), end=' - ')

#Print letters with hexagons
def print_letters_hex(letters: list[str], colour: TextColour = TextColour.END, centreColour: TextColour = TextColour.BOLD):
   if len(letters) != 7:
      for _ in range(0, 7-len(letters)):
         letters.insert(0, ' ')

   #Set letters uppercase
   letters = [letter.upper() for letter in letters]
   
   #First line
   print("      ___     ___")
   print("     /   \\   /   \\")
   print("    |  " + colour + letters[0] + TextColour.END + "  | |  " + colour + letters[1] + TextColour.END + "  |")
   print("     \\___/   \\___/")

   #Second line
   print("  ___     ___     ___")
   print(" /   \\   /   \\   /   \\")
   print("|  " + colour + letters[2] + TextColour.END + "  | |  " + centreColour + letters[-1] + TextColour.END + "  | |  " + colour + letters[3] + TextColour.END + "  |")
   print(" \\___/   \\___/   \\___/")

   #Third line
   print("      ___     ___")
   print("     /   \\   /   \\")
   print("    |  " + colour + letters[4] + TextColour.END + "  | |  " + colour + letters[5] + TextColour.END + "  |")
   print("     \\___/   \\___/\n")