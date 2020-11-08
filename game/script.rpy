# The script of the game goes in this file.

init python:
    import random

    def select_scramble(text,emotion):
        if emotion == 0:
            return changeVowels(text)
        if emotion == 1:
            return quitVowels(text)

    def changeVowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i].lower() in vowels:
                final_string = final_string + vowels[random.randint(0,9)]
            else:
                final_string = final_string + text[i]
        return final_string

    def quitVowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i] not in vowels:
                final_string = final_string + text[i]
        return final_string

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    $ emotion = 0
    $ text = select_scramble("Hola mundo",emotion)
    e "Hello, I am [text]."
    $ emotion = 1
    $ text = select_scramble("Hola mundo",emotion)
    e "[text]"
    # This ends the game.

    return


label variables:
    #$ scramble = Scramble()
    #$ text = scramble.move_vowels('Hello World')
    $ emotion = 0
    $ text = ''
    return
