"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
    word_d = {}
    with open(FILE) as f:
        for line in f:
            tokens = line.split()
            for token in tokens:
                token = string_manipulation(token)
                if token not in word_d:
                    word_d[token] = 1
                else:
                    word_d[token] += 1
        print_out_d(word_d)
        # print(f'The maximum word: "{max_token}": {max_count}')


def string_manipulation(s):
    ans = ''
    for ch in s:
        if ch.isdigit() or ch.isalpha() and ch not in PUNCTUATION:
            ans += ch.lower()
    return ans


def print_out_d(d):
    """
    : param d: (dict) key of type str is a word
                    value of type int is the word occurrence
    ---------------------------------------------------------------
    This function prints out all the info in d
    """
    # max_token = ''
    # max_count = 1

    for token, count in sorted(d.items(), key=lambda ele: ele[1]):
        # if count > max_count:
        #     max_token = token
        #     max_count = count
        print(f'{token}: {count}')
    # return max_token, max_count


if __name__ == '__main__':
    main()
