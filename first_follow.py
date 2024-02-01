

import hangman_words
import hangman_art
import random
word_list = hangman_words.word_lost
rando_word = random.choice(word_list)

#here
print(hangman_art.logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



chosen_word = rando_word
print(f'pssst, the solution is {chosen_word}.')
display = []
for char in chosen_word:
    display += "_"
lives = 6
while "".join(display) != chosen_word and lives != 0:
    
    guess = input("guess a letter .").lower()
    count = 0
    if guess in display:
        print("bro you already written that letter once xd")
    #here
    for char in rando_word:
        count = count + 1
        if guess == char:
            display[count - 1] = guess
        
    if guess not in display:
        lives -= 1
        print("well......that letter is not in the word my friend :d")

    print(display)
    print(hangman_art.stages[lives])       
if lives == 0:
    print("game over you loser !xd")
elif "".join(display) == chosen_word:
    print("you win you winner :D")
# for char in rando_word:
#     if guess == char:
#         print("true")
#     elif guess != char:
#         print("false") 

#here
