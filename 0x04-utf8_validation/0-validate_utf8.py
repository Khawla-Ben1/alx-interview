#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    a method that determines if a given
    data set represents a valid UTF-8 encoding
    """
    nbr = 0

    for nbr in data:
        binary_rep = format(nbr, '#010b')[-8:]
        if nbr == 0:
            for i in binary_rep:
                if i == '0':
                    break
                nbr += 1
            if nbr == 0:
                continue
            if nbr == 1 or nbr > 4:
                return False
        else:
            if not binary_rep.startswith('10'):
                return False
        nbr -= 1

    return nbr == 0
