# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 25
# December 29, 2021

#This program takes a sentence and breaks it up.  It sorts it and also prints the first and last words of the sentence.
# To run this program you will need to run python within a terminal or cmd window.  then you will need to do the following
# import Exercise_25
# sentence = "All good things come to those who wait."
# words = Exercise_25.break_words(sentence)
# words
# sorted_words = Exercise_25.sort_words(words)
# sorted_words
# Exercise_25.print_first_word(words)
# Exercise_25.print_last_word(words)
# words
# Exercise_25.print_first_word(sorted_words)
# Exercise_25.print_last_word(sorted_words)
# sorted_words
# sorted_words = Exercise_25.sort_sentence(sentence)
# sorted_words
# Exercise_25.print_first_and_last(sentence)
# Exercise_25.print_first_and_last_sorted(sentence)

def break_words(stuff):
    """This function will break up workds for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prionts the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words oft he sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

