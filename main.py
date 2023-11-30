def toMorse():

    # Dictionary with format "Letter/symbol":"Morse Code"
    code = {"A":".-" , "B":"-..." , "C":"-.-." , "D":"-.." , "E":"." , "F":"..-." , "G":"--." , "H":"....",
        "I":".." , "J":".---" , "K":"-.-" , "L":".-.." , "M":"--" , "N":"-." , "O":"---" , "P":".--.",
        "Q":"--.-" , "R":".-." , "S":"..." , "T":"-" , "U":"..-" , "V":"...-" , "W":".--" , "X":"-..-",
        "Y":"-.--" , "Z":"--.." , "0": "-----" , "1":".----" , "2":"..---" , "3":"...--" , "4":"....-",
        "5":"....." , "6":"-...." , "7":"--..." , "8":"---.." , "9":"----." , ".":".-.-.-" , ",":"--..--",
        "?":"..--.." , "'":".---." , "!":"-.-.--" , "/":"-..-." , "(":"-.--." , ")":"-.--.-" , "&":".-...",
        ":":"---..." , ";":"-.-.-." , "=":"-...-" , "+":".-.-." , "-":"-....-" , "_":"..--.-" , "\"":".-..-.",
        "$":"...-..-" , "@":".--.-." , " ":"/"}

    phrase = input("Enter a phrase in English: ")

    # Go through user input and print each character's Morse Code equivalent.
    for x in phrase:
        if (x.upper() in code):
            #print(x, "=" , code[x.upper()], end = "")
            print(code[x.upper()], end = " ")
        else:
            print()

def fromMorse():
    # Dictionary with format "Letter/symbol":"Morse Code"
    code = {"A":".-" , "B":"-..." , "C":"-.-." , "D":"-.." , "E":"." , "F":"..-." , "G":"--." , "H":"....",
        "I":".." , "J":".---" , "K":"-.-" , "L":".-.." , "M":"--" , "N":"-." , "O":"---" , "P":".--.",
        "Q":"--.-" , "R":".-." , "S":"..." , "T":"-" , "U":"..-" , "V":"...-" , "W":".--" , "X":"-..-",
        "Y":"-.--" , "Z":"--.." , "0": "-----" , "1":".----" , "2":"..---" , "3":"...--" , "4":"....-",
        "5":"....." , "6":"-...." , "7":"--..." , "8":"---.." , "9":"----." , ".":".-.-.-" , ",":"--..--",
        "?":"..--.." , "'":".---." , "!":"-.-.--" , "/":"-..-." , "(":"-.--." , ")":"-.--.-" , "&":".-...",
        ":":"---..." , ";":"-.-.-." , "=":"-...-" , "+":".-.-." , "-":"-....-" , "_":"..--.-" , "\"":".-..-.",
        "$":"...-..-" , "@":".--.-." , "/":" "}

    # Create parallel lists of dictionary's key and values to use later
    codeKeys = list(code.keys())
    codeValues = list(code.values())

    phrase = input("Enter a phrase in Morse Code: ")

    # Separate user input into list for easy translation of each letter
    phraseSplit = phrase.split()

    for lett in phraseSplit:
        #print(lett)

        # Only translate if the character is in the values of the dictionary
        if (lett in code.values()):
            print(codeKeys[codeValues.index(lett)], end = "")
        else:
            print("Symbol not valid", end = "")

def main():
    # Allow endless repetition; end at user discretion
    again = "yes"
    while (again!= "no"):
        try:
            translateMode = int(input("1.) To Morse Code\n2.) From Morse Code\nWould you like to translate a phrase to or from Morse Code? "))
            if (translateMode == 1):
                toMorse()
            elif (translateMode == 2):
                fromMorse()
            # Allow try again if user enters a number, not 1 or2
            else:
                print("\nInvalid input. Try again.")
                translateMode = int(input("1.) To Morse Code\n2.) From Morse Code\nWould you like to translate a phrase to or from Morse Code? "))

        # Allow try again if user enters a non-number
        except:
            print("\nInvalid input. Try again.")
            translateMode = int(input("1.) To Morse Code\n2.) From Morse Code\nWould you like to translate a phrase to or from Morse Code? "))
        
        again = input("\nWould you like to try a new phrase? Enter \"yes\" or \"no: ")


    '''
    Planned updates
    1.) Allow user to enter a phrase
    2.) Program will determine whether to translate to or from Morse Code
    3.) If a character is invalid, print the character as is
    4.) Add sound to translations to Morse Code
    '''
            

main()