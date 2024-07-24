import random

from words  import words

from hangman_visual import lives_visual_dict

import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed.

    lives = 7

    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        #Letters already used
        print('You have', lives, 'lives left and you have already used these letters: ', ' '.join(used_letters))

        #What current word is  (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
              word_letters.remove(user_letter)
              print('')

            else:
               lives = lives -1 #Take away a life if wrong
               print('\nYour letter,', user_letter, 'is not in the word.')


        elif user_letter in used_letters:
            print('\nYou have already chosen that letter. Please choose again!')

        else:
            print('\nInvalid character. Please try again!')

    # Gets here when len (word_letters) == 0 OR when  lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
       print('You guessed the correct word', word, '!!')



if __name__ == '__main__':
    hangman()
