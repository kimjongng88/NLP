#!/usr/bin/env python3

"""
ENLP A0: The Basics

Usage: on the Unix command line,
  python basics.py
to run doctests. If all tests pass, the program will exit silently.

@author: Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""


import re, doctest

def validate1(s):
    """
    Checks whether the string is a valid employee ID using a single regular expression.
    An employee ID is valid if and only if it consists
    only of 6-10 alphabetic characters (letters), followed by 2 numeric digits.

    (Assumes s is a string without any non-ASCII characters.
    Otherwise, does not make any assumptions about the string.)

    The lines below give example inputs and correct outputs using doctest notation,
    and can be run to test the code. Passing these tests is NOT sufficient
    to guarantee your implementation is correct. You may add additional test cases.

    >>> validate1('AbCdEf00')
    True
    >>> validate1('$0RQLpCHz49')
    False
    """
    EMPLOYEE_RE = '^[A-Za-z]{6,10}\d\d'
    if re.search(EMPLOYEE_RE, s):
        return True
    return False

def validate2(s):
    """
    >>> validate2('AbCdEf00')
    True
    >>> validate2('$0RQLpCHz49')
    False
    """
    # Implement the validation another way, without using a regex or any libraries.
    # You may use the .isalpha() and .isdigit() methods,
    # variables, standard data structures such as lists,
    # if statements, loops, etc.
    # As far as a caller is concerned, this function should have the
    # same behavior as validate1().
    count = 0
    digit = 0
    for i in s:
        if (i.isalpha()) == True & count < 10:
            count+=1
        elif (i.isdigit()) == True & count >= 6 & count <= 10 & digit <= 2:
            digit += 1
    if count >= 6 & count <= 10 & digit <= 2:
        return True
    return False


def dna_prob(seq):
    """
    Given a sequence of the DNA bases {A, C, G, T},
    stored as a string, returns a conditional probability table
    in a data structure such that one base (b1) can be looked up,
    and then a second (b2), to get the probability p(b2 | b1)
    of the second base occurring immediately after the first.
    (Assumes the length of seq is >= 3, and that the probability of
    any b1 and b2 which have never been seen together is 0.
    Ignores the probability that b1 will be followed by the
    end of the string.)

    >>> tbl = dna_prob('ATCGATTGAGCTCTAGCG')
    >>> tbl['T']['T']
    0.2
    >>> tbl['G']['A']
    0.5
    >>> tbl['C']['G']
    0.5
    """
    # You may use the collections module, but no other libraries.
    dic = {'A': {'A': 0, 'C': 0, 'G': 0, 'T': 0},
            'C': {'A': 0, 'C': 0, 'G': 0, 'T': 0},
            'G': {'A': 0, 'C': 0, 'G': 0, 'T': 0},
            'T': {'A': 0, 'C': 0, 'G': 0, 'T': 0}}

    for i in range(len(seq) - 1):
        b1, b2 = seq[i], seq[i+1]
        dic[b1][b2] += 1

    for i in dic:
        total = sum(dic[i].values())
        for j in dic[i]:
            if total > 0:
                dic[i][j] /= total
            else:
                dic[i][j] = 0
    return dic

def dna_bp(seq):
    """
    Given a string representing a sequence of DNA bases,
    returns the paired sequence, also as a string,
    where A is always paired with T and C with G.

    >>> dna_bp('ATCGATTGAGCTCTAGCG')
    'TAGCTAACTCGAGATCGC'
    """
    # Do not use any libraries.
    # Hint: this can be done in one line. (More than one line is OK too.)
    return seq.translate(str.maketrans('ATCG', 'TAGC'))

if __name__=='__main__':
    doctest.testmod() # This runs the doctests and prints any failures.