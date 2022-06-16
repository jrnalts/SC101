"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    start = time.time()
    ####################

    lst = give_letters()
    # example for testing
    # lst = (['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u'])

    boggle(lst, read_dictionary(flatten(lst)))

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(lst):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            ls = line.strip()
            if len(ls) >= 4:
                if ls.startswith(lst):
                    d[ls] = ''
    return d


def boggle(lst, all_words):
    ans = []
    for sub_idx, sub_lst in enumerate(lst):  # 拋出每一列
        for ch_idx, ch in enumerate(sub_lst):  # 拋出每一列裡的字母
            if has_prefix(ch, all_words):
                path = []
                boggle_helper(ch, lst, sub_idx, ch_idx, ans, path, all_words)
    print(f'There are {len(ans)} words in total')


def index_exist(lst, index):
    if 0 <= index < len(lst):
        return True
    return False


def flatten(lst):
    flatten_lst = []
    for sub_lst in lst:
        if type(sub_lst) is not list:
            pass
        else:
            for e in sub_lst:
                flatten_lst.append(e)
    return tuple(flatten_lst)


def boggle_helper(current_s, lst, sub_idx, ch_idx, ans, path, all_words):
    if has_prefix(current_s, all_words):
        # Base case
        if current_s in all_words and current_s not in ans:
            ans.append(current_s)
            print(f'Found "{current_s}"')

        # Recursive case
        for i in range(3):
            n_sub_idx = sub_idx + i - 1
            if index_exist(lst, n_sub_idx):
                for j in range(3):
                    n_ch_idx = ch_idx + j - 1
                    # skip case: self / path repeated / index not exist
                    if i == 1 and j == 1 or \
                            (n_sub_idx, n_ch_idx) in path or \
                            not index_exist(lst[n_sub_idx], n_ch_idx):
                        pass
                    else:
                        add_ch = lst[n_sub_idx][n_ch_idx]
                        if current_s.count(add_ch) < sum(ch.count(add_ch) for ch in lst):
                            boggle_helper(current_s + add_ch, lst, n_sub_idx, n_ch_idx,
                                          ans, path + [(n_sub_idx, n_ch_idx)], all_words)


def has_prefix(sub_s, words):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in words:
        if word.startswith(sub_s):
            return True
    return False


def give_letters():
    lst = []
    i = 1
    while True:
        if len(lst) == 4:
            break
        else:
            s = str(input(f'{i} row of letters: ')).lower()
            if len(s.replace(' ', '')) != 4 or len(s.split(' ')) != 4 or not s.replace(' ', '').isalpha():
                print('Illegal input')
                pass
            else:
                lst.append(s.split(' '))
                i += 1
    return tuple(lst)


if __name__ == '__main__':
    main()
