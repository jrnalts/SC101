"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19
4
If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dic = []


def main():
    global dic
    dic = read_dictionary()

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = str(input('Find anagrams for: '))

        if s == EXIT:
            break
        else:
            start = time.time()
            ####################

            find_anagrams(s)

            ####################
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global dic

    with open(FILE) as f:
        for line in f:
            word = line.strip()
            dic.append(word)

    return dic


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    anagrams = []
    for word in dic:
        if len(s) == len(word):
            if sorted(word) == sorted(s):
                print('Searching...')
                anagrams.append(word)
                print(f'Found: {word}')

    print(f'{len(anagrams)} anagrams: {anagrams}')


if __name__ == '__main__':
    main()