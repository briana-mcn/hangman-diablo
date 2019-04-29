import string

from random_word import RandomWords


def initialize_game_variables():
    global guesses_available
    global win
    global letter_bank
    global guess_bank
    global word

    # add one more guess to account for missed letter guesses (guesses == 4)
    guesses_available = 5
    # holds winning state of game
    win = False
    letter_bank = list(string.ascii_lowercase)
    guess_bank = []
    word = RandomWords().get_random_word()


def get_input():
    return input().lower()


def get_visual_spacing_for_word_to_guesses_as_string():
    """Populates visual 'spaces' for guesser"""
    spaces_word = []
    for letter in word:
        if letter in guess_bank:
            spaces_word.append(letter)
        elif letter.isalpha() and letter not in guess_bank:
            spaces_word.append('_')
        elif letter == ' ':
            spaces_word.append(' ')
        # append a space here to prevent word spaces from being smooshed
        spaces_word.append(' ')

    return ''.join(spaces_word)


def check_guessed_letter(user_input):
    # check if letter is in guessed bank
    if user_input in guess_bank:
        return None
    # check if it's in the word
    elif user_input in word:
        # add to guessed letter bank
        guess_bank.append(user_input)
        return True
    elif user_input not in word:
        guess_bank.append(user_input)
        return False


def get_round_header():
    print('Letter Bank: {}'.format(', '.join(letter_bank)))
    print("Guessed Letters: {}".format(tuple(guess_bank)))
    print('You have {} guesses available'.format(guesses_available - 1))
    print('Guess a letter!')
    letter_status = get_visual_spacing_for_word_to_guesses_as_string()
    print(letter_status)


def play_another_game_input():
    input = input('Play again?')
    if input is 'y':
        start_game()
    else:
        print('Bye!')
        exit()


def start_game():
    initialize_game_variables()

    print("Let's play some hangman!")
    print("You have {} total guesses".format(guesses_available))
    print("_~_~_~_~_~_~_~_~_~_~_~_~_")

    while guesses_available > 1 or win == False:
        play_game()

    if win:
        print('You WON!')
        print('You guessed it correctly! {}'.format(word))
        play_another_game_input()
    else:
        print("You lose :'(")
        print('The word was {}'.format(word))
        play_another_game_input()


def play_game():
    get_round_header()
    #get input
    user_input = get_input()
    # get the game details of the guessed letter
    guess_round = check_guessed_letter(user_input)
    if guess_round is None:
        print('Letter "{}" already guessed'.format(user_input))
    elif guess_round == False:
        guesses_available -= 1
        letter_bank.remove(user_input)
        print('"{}" is not in the word!'.format(user_input))
        print()
    elif guess_round == True:
        letter_bank.remove(user_input)
        letter_status = get_visual_spacing_for_word_to_guesses_as_string()
        print('Great! You guessed a correct letter')
        if '_' not in list(letter_status):
            win = True

# needs to call main game function
if __name__ == "__main__":
    start_game()
