#!/usr/bin/python3
""" python script to check for uy=tf-8 validation"""


def validUTF8(data):
    """function to validate utf-8  characters"""
    i = 0
    while i < len(data):
        numOfBytes = 0
        val = data[i]
        if val >= 255:
            return False
        elif val & 128 == 0:
            numOfBytes = 1
        elif val & 224 == 192:
            numOfBytes = 2
        elif val & 240 == 224:
            numOfBytes = 3
        elif val & 248 == 240:
            numOfBytes = 4
        else:
            return False
        j = 1
        while j < numOfBytes:
            if j + i > len(data):
                return False
            elif data[i + j] & 192 != 128:
                return False
            j += 1
        i = i + numOfBytes - 1
        i++
    return True
