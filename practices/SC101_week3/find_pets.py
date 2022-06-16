"""
File: student_info_dict.py
------------------------------
This program puts data in a text file
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'all_pets.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
    d = find_pets_dict()
    find_pets(d, ['Happy'])


def find_pets_dict():
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip().replace(",", "").split()
            name = line[0]
            line.pop(0)
            for adjective in line:
                if name not in d:
                    d[name] = []
                d[name].append(adjective)
    return d


def find_pets(d, adjectives):
    pets = []
    for adj in adjectives:
        for name, adj_lst in d.items():
            if adj in adj_lst and name not in pets:
                pets.append(name)

    if len(pets) != 0:
        for i, name in enumerate(pets):
            if i != len(pets)-1:
                print(name, end=', ')
            else:
                print(name)
    else:
        print('')


if __name__ == '__main__':
    main()
