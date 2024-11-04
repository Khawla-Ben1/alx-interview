#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    a method that determines if a given
    data set represents a valid UTF-8 encoding
    """
    r_bytes = 0

    for num in data:
        byte = format(num, '08b')[-8:]
        if r_bytes == 0:
            if byte.startswith('0'):
                continue
            elif byte.startswith('110'):
                r_bytes = 1
            elif byte.startswith('1110'):
                r_bytes = 2
            elif byte.startswith('11110'):
                r_bytes = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False
            r_bytes -= 1
    return r_bytes == 0
