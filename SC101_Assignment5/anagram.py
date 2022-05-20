"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

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
dic = {}


def main():
    global dic

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = str(input('Find anagrams for: '))
        dic = read_dictionary(s)
        if s == EXIT:
            break
        else:
            start = time.time()
            ####################

            find_anagrams(s, len(s))

            ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(s):
    global dic

    with open(FILE) as f:
        for line in f:
            word = line.strip()
            for ch in s:
                if word.startswith(ch) and len(word) == len(s):
                    dic[word] = ''
    return dic


def find_anagrams(s, len_s):
    """
    :param s:
    :return:
    """
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, len_s, '', anagrams)

    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, len_s, current_s, anagrams):
    if len(current_s) == len_s:
        if current_s in dic and current_s not in anagrams:
            print(f'Found: {current_s}')
            anagrams.append(current_s)
    else:
        for ch in s:
            if current_s.count(ch) == s.count(ch):
                pass
            else:
                find_anagrams_helper(s, len_s, current_s + ch, anagrams)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
