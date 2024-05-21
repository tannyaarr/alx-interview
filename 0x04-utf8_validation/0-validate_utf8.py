#!/usr/bin/python3
"""method that determines if a given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    i = 0
    while i < len(data):
        if data[i] < 128:
            i += 1
        else:

            if data[i] >> 5 == 6:
                num_bytes = 2
            elif data[i] >> 4 == 14:
                num_bytes = 3
            elif data[i] >> 3 == 30:
                num_bytes = 4
            else:
                return False

            for j in range(1, num_bytes):
                if i + j >= len(data) or data[i + j] >> 6 != 2:
                    return False
            i += num_bytes

    return True
