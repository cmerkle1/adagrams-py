from random import randint

def draw_letters():
    '''
    Params: none
    Returns: 
        player_letters: an array of 10 strings containing
        exactly 1 letter each
    This function 'draws' letters for the player from a letter_dict and 
    establishes the hand for the Adagrams game.
    '''

    letter_dict = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
        'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
        'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
        }

    # ----- Additional code to account for letter weighting -----
    letter_pool = []

    for letter, quantity in letter_dict.items():
        for i in range(quantity):
            letter_pool.append(letter)

    # Draw letters from letter_dict using random, using dict index to draw while available
    player_letters = []
    max_letters = 10

    # While letters < 10, draw letters from letter_dict
    while len(player_letters) < max_letters:
        random_index = randint(0, len(letter_pool) - 1) 
        letter = letter_pool[random_index]

        player_letters.append(letter)
        letter_pool.pop(random_index)

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
    This function determines if there are available letters 
    to create a word.
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
    This function calculates a word score for a given word
    based on values in a score_dict.
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
    if len(word) in range(7, 11):
        score += 8

    return score


def get_highest_word_score(word_list):
    '''
    params:
        word_list(list) - a list of Adagram words
    returns:
        winner(tuple) - the winning word data including score
    This function finds the highest scoring word from a word_list
    using the criteria: highest score wins, then ties break down to
    winner if one word has a length of 10 and the other doesn't, winner 
    if one word is shorter (shorter wins), then breaks down further if 
    a 10 length tie occurs by the item with the earliest entry in the original list.
    '''
    scorekeeper = []

    #Iterate through word_list, use score_word function to find scores
    for word in word_list:
        score = score_word(word)
        scorekeeper.append([word, score])

    current_highest = 0
    winning_word = ''

    # Implement logic for determining winner
    for high_score in scorekeeper:
        if high_score[1] > current_highest: # Checks basic score logic
            current_highest = high_score[1]
            winning_word = high_score[0]
    
        elif high_score[1] == current_highest and high_score[1] != 0: # Checks tied scores
            if len(high_score[0]) == 10 and len(winning_word) != 10: # If one has len 10, that wins
                current_highest = high_score[1]
                winning_word = high_score[0]    

            if len(high_score[0]) < len(winning_word) and len(winning_word) != 10:
                current_highest = high_score[1]
                winning_word = high_score[0]
        
    winner = (winning_word, current_highest,) # Returned as a tuple

    return winner
        