from random import randint

def draw_letters():
    '''
    Params: none
    Returns: an array of 10 strings containing
    exactly 1 letter each
    '''

    letter_dict = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
        'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
        'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
        }
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # draw letters from letter_dict using random, using dict index to draw while available
    player_letters = []
    max_letters = 10

    # While letters < 10, draw letters from letter_dict
    while len(player_letters) < max_letters:
        random_index = randint(0, 25)
        letter = letters[random_index]

        # If less than 1 quantity remains, redraw
        while letter_dict[letter] < 1:
            random_index = randint(0, 25)
            letter = letters[random_index]

        player_letters.append(letter)
        letter_dict[letter] -= 1

    return player_letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass