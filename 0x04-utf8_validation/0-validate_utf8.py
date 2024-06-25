#!/usr/bin/python3
"""utf-8 validation"""


def get_leading_set_bits(num):
    """return the number of leading set bits"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            if bits_count == 0:
                continue
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
