import string
import sys
import itertools

def minion(str):
    personAname = input("Enter your name, player1: ")
    personBname = input("Enter your name, player2: ")
    listOfLetters = [a for a in str]
    l = len(listOfLetters)
    vowel = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    all_word = []
    personAwords = []
    personBwords = []
    #all_word = [letter_list[start:end+1] for start in range(l) for end in range(start, l)]
    all_word=[]
    for start in range(l):
        for end in range(start, l):
            all_word.append(listOfLetters[start:end+1])
    for array in all_word:
        if array[0] in vowel:
            personBwords.append(array)
    for array in all_word:
        if array[0] in consonants:
            personAwords.append(array)
    if len(personAwords) == len(personBwords):
        print ('Draw')
    if len(personAwords) > len(personBwords):
        print (personAname, len(personAwords))
    if len(personBwords) > len(personAwords):
        print (personBname, len(personBwords))

def main():
    str = input()
    return(minion(str.upper()))
print(main())
