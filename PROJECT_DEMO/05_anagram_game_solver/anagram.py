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
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
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

            find_anagrams(s, len(s))

            ####################
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global dic

    with open(FILE) as f:
        for line in f:
            dic.append(line.strip())
    return dic


def find_anagrams(s, len_s):
    """
    :param s:(str) input word for searching
    :param len_s:(int) length of input word
    :return: anagrams of the input word
    """
    anagrams = set()
    for voc in dic:
        if len(voc) == len_s:
            if sorted(voc) == sorted(s):
                print('Searching...')
                find_anagrams_helper(s, len_s, '', anagrams, voc)

    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, len_s, current_s, anagrams, voc):
    if voc.startswith(current_s):  # Prunning for faster searching
        if len(current_s) == len(voc):  # Compare length
            if current_s == voc and current_s not in anagrams:  # Check if word in the dictionary and we don't have it.
                print(f'Found: {current_s}')
                anagrams.add(current_s)  # Collect the match word into anagrams
        else:
            for ch in s:
                if current_s.count(ch) == s.count(ch):
                    pass
                else:
                    find_anagrams_helper(s, len_s, current_s + ch, anagrams, voc)


if __name__ == '__main__':
    main()
