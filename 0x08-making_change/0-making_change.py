#!/usr/bin/python3
"""Making changes"""


def makeChanges(coins, total):
    """generate changes needed to reach total
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += i
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
