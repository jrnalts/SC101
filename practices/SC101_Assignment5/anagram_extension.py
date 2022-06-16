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
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
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
            if len(s) == len(word):
                if sorted(word) == sorted(s):
                    dic[word] = ''
    return dic


def find_anagrams(s, len_s):
    """
    :param s:
    :return:
    """
    anagrams = []
    for voc in dic:
        find_anagrams_helper(s, len_s, [], anagrams, voc)

    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, len_s, current_s, anagrams, voc):
    word = ''.join(current_s)
    if voc.startswith(word):
        if word not in anagrams:
            if len(word) == len_s:
                print('Searching...')
                anagrams.append(word)
                print(f'Found: {word}')
            else:
                for ch in s:
                    if current_s.count(ch) != s.count(ch):
                        # Choose
                        current_s.append(ch)

                        # Explore
                        find_anagrams_helper(s, len_s, current_s, anagrams, voc)

                        # Un-choose
                        current_s.pop()


if __name__ == '__main__':
    main()

