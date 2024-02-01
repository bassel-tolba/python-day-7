word_list = ["a d v a r k", "c a m e ", "b a o o n"]

import random

word = random.randint(0 , 2)
rand_word = word_list[word]
rand_word_list = rand_word.split(" ")
rand_word_len = len(rand_word_list)

guess =  input("guess a letter.")
print(guess)
for char in rand_word_list:
    
    if guess == char:
        print("True")
    else:
        print("False")

