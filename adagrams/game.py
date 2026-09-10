from random import randint

def draw_letters():
    '''
    Params: none
    Returns: 
        player_letters: an array of 10 strings containing
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
    '''
    params: 
        word(str) - an input word
        letter_bank(array) - drawn letters in a hand
    returns:
        boolean
        True if every letter in word is available in letter_bank
        Else False
    '''
    # Create a new list copy to avoid mutable object issues
    copy_bank = []

    for letter in letter_bank:
        copy_bank.append(letter)

    # Checking each letter in word to see if in copy_bank
    for letter in word:
        if letter.upper() in copy_bank:
            # Remove the letter to avoid counting duplicates
            copy_bank.remove(letter.upper())
        else:
            return False # Returns if any letters aren't found

    return True


def score_word(word):
    '''
    params:
        word(str) - the Adagrams word to score
    returns:
        score(int) - number of points scored
    '''
    score = 0

    score_dict = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1,
        'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4,
        'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
        }

    # Iterate through letters in word, case insensitive, adding value
    for letter in word:
        letter_value = score_dict[letter.upper()]
        score += letter_value

    # If the word contains between 7-10 letters, add 8 to score
    if len(word) in range(7, 10):
        score += 8

    return score


def get_highest_word_score(word_list):
    pass