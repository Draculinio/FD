init python:
    import random

    def select_scramble(text,emotion):
        scrambling = {0:change_vowels,1:quit_vowels,2:mirror_text}
        return scrambling[emotion](text)

    def change_vowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i].lower() in vowels:
                final_string = final_string + vowels[random.randint(0,9)]
            else:
                final_string = final_string + text[i]
        return final_string

    def quit_vowels(text):
        final_string=''
        vowels = 'aeiouAEIOU'
        for i in range(0,len(text)):
            if text[i] not in vowels:
                final_string = final_string + text[i]
        return final_string

    def mirror_text(text):
        return text[::-1]
