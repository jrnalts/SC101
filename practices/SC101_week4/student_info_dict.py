"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""

# The file name of our target text file
FILE = 'students_info.txt'


def main():
    all_d = {}
    ######################
    with open(FILE) as f:
        for line in f:
            info = line.split()
            all_d[info[0]] = {
                'AGE': info[1],
                'EMAIL': info[2],
                'FOOD': info[3:],
            }
        # d_student = {}
        # name = info[0]
        # d_student[name] = name
        # d_student['AGE'] = info[1]
        # d_student['EMAIL'] = info[2]
        # d_student['FOOD'] = info[3:]
        # print(hex(id(d_student)))
        # all_d[name] = d_student
    ######################
    print_out_d(all_d)


def print_out_d(d):
    """
    param d: (dict) key of type str is the name of student
    value of type dict is the info of the student
    ---------------------------------------------------------------
    This function prints out a nested data structure on console
    """
    for name, d_name in d.items():
        print('-' * 12)
        print(name)
        print(d_name)
        print('-' * 12)


if __name__ == '__main__':
    main()
