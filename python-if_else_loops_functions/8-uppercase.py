#!/usr/bin/python3
def uppercase(str):
    conv_str = ''
    for c in str:
        if 97 <= ord(c) <= 122:
            conv_str += chr(ord(c) - 32)
        else:
            conv_str += c
    print('{}'.format(conv_str))
