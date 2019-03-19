import string

guesses_available = 4
# add one more guess to account for missed letter guesses

user_input = ''
guessed_letter_bank = tuple()
alphabet = list(string.ascii_letters)

#TODO random word generator
word = "Pina Colada"


def get_input():
    print('You have {} guesses left'.format(guesses_available - 1))
    print('Guess a letter!')
    return input()


def get_visual_spacing_for_word_to_guesses_as_string(word):
    """Populates visual 'spaces' for guesser"""
    spaces_word = []
    for letter in word:
        for guessed_letter in guessed_letter_bank:
            if letter == guessed_letter:
                spaces_word.append(guessed_letter.lower())
                continue
        if letter.isalpha():
            spaces_word.append('_')
        elif letter == ' ':
            spaces_word.append(' ')
            continue
        # append a space here to prevent word spaces from being smooshed
        spaces_word.append(' ')

    return ''.join(spaces_word)


while guesses_available >= 0:
    print(get_visual_spacing_for_word_to_guesses_as_string(word=word))
    input = get_input()
