"""
File: dice_rolls_sum.py
Name:
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(8)


def dice_sum(target_sum):
    counter = [0]
    dice_sum_helper(target_sum, [], counter)
    print(counter)


def dice_sum_helper(target_sum, current_lst, counter):
    counter[0] += 1
    if sum(current_lst) <= target_sum:
        if sum(current_lst) == target_sum:
            print(current_lst)
        else:
            for roll in [6, 5, 4, 3, 2, 1]:
                if sum(current_lst) + roll <= target_sum:
                    # Choose
                    current_lst.append(roll)

                    # Explore
                    dice_sum_helper(target_sum, current_lst, counter)

                    # Un-choose
                    current_lst.pop()


if __name__ == '__main__':
    main()
