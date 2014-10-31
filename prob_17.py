#!/usr/bin/env python

"""
Project Euler
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, 
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used?
"""

NUM_WORD_MAP = {1 : 'one',
                2 : 'two',
                3 : 'three',
                4 : 'four',
                5 : 'five',
                6 : 'six',
                7 : 'seven',
                8 : 'eight',
                9 : 'nine',
                10 : 'ten',
                11 : 'eleven',
                12 : 'twelve',
                13 : 'thirteen',
                14 : 'fourteen',
                15 : 'fifteen',
                16 : 'sixteen',
                17 : 'seventeen',
                18 : 'eighteen',
                19 : 'nineteen',
                20 : 'twenty',
                30 : 'thirty',
                40 : 'forty',
                50 : 'fifty',
                60 : 'sixty',
                70 : 'seventy',
                80 : 'eighty',
                90 : 'ninety'}

def print_num(n):
    """ Want to print English representation of n """
    n_digits = len(str(n))
    
    # We presume that we will not be seeing numbers with > 4 digits
    if n_digits == 1:
        return NUM_WORD_MAP[n]
    elif n_digits == 2:
        # If n > 20, need to use modulus to get name of tens digit
        if n > 20:
            tens_num = n / 10 * 10
            ones_num = n % 10
            if ones_num == 0:
                return NUM_WORD_MAP[tens_num]
            else:
                return " ".join([NUM_WORD_MAP[tens_num],
                                 NUM_WORD_MAP[ones_num]])
        else:
            return NUM_WORD_MAP[n]
    elif n_digits == 3:
        to_return = " ".join([NUM_WORD_MAP[n / 100], "hundred"])
        tens_digit = n % 100 / 10
        ones_digit = n % 10
        if (tens_digit == 0) & (ones_digit == 0):
            return to_return    
        elif tens_digit == 0:
            to_return = " ".join([to_return,
                                  "and",
                                  NUM_WORD_MAP[ones_digit]])
        elif ones_digit == 0:
            to_return = " ".join([to_return,
                                  "and",
                                  NUM_WORD_MAP[tens_digit * 10]])
        else:
            to_return = " ".join([to_return,
                                  "and",
                                  NUM_WORD_MAP[tens_digit * 10],
                                  NUM_WORD_MAP[ones_digit]])
        return to_return
    elif n_digits == 4:
        thou_digit = n / 1000
        hund_digit = n % 1000 / 100
        tens_digit = n % 100 / 10
        ones_digit = n % 10
        to_return = " ".join([NUM_WORD_MAP[thou_digit],
                              "thousand"])
        if hund_digit == 0 & tens_digit == 0 & ones_digit == 0:
            return to_return
        elif hund_digit == 0 & tens_digit == 0:
            to_return = " ".join([to_return,
                                  "and",
                                  NUM_WORD_MAP[ones_digit]])
        elif tens_digit == 0:
            to_return = " ".join([to_return, 
                                  "and",
                                  NUM_WORD_MAP[hund_digit],
                                  "hundred and",
                                  NUM_WORD_MAP[ones_digit]])
        else:
            to_return = " ".join([to_return,
                                  "and",
                                  NUM_WORD_MAP[hund_digit],
                                  "hundred and",
                                  NUM_WORD_MAP[tens_digit*10],
                                  NUM_WORD_MAP[ones_digit]])
        return to_return

if __name__ == "__main__":
    num_letters = 0
    nums_as_strs = []
    for i in range(1, 1001):
        num_as_str = print_num(i)
        nums_as_strs.append(num_as_str)
        num_letters += len("".join(str.split(num_as_str, " ")))
    
    print num_letters
    

    
