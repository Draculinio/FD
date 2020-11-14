# The script of the game goes in this file.



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define i = Character("Impostor")

define j = Character(random.choice(['p1','p3','p4']))
# The game starts here.

label start:

    # scene 1

    call beggining



    $ introversion = 0
    $ text = select_scramble("Hola mundo",introversion)
    j "[text]"
    $ introversion = 1
    $ text = select_scramble("Que tal te va",introversion)
    j "[text]"
    $introversion = 2
    $ text = select_scramble("Mirror",introversion)
    j "[text]"
    # This ends the game.

    return


label variables:

    $ introversion = 0
    $ evasion = 0
    $ escapism = 0
    $ suspicion = 0
    $ absurdity = 0
    $ text = ''
    return
