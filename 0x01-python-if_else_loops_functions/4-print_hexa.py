#!/usr/bin/python3

def get_char(num:int):
    if num == 0:
        return 'a'
    elif num == 1:
        return 'b'
    elif num == 2:
        return 'c'
    elif num == 3:
        return 'd'
    elif num == 4:
        return 'e'
    else:
        return 'f'

def print_hexa(num, num1, num2):
    print("{} = 0X{}{}".format(num, num1, num2))

for num in range(0, 99):
    if num < 10:
        print_hexa(num, num, '')
    elif num > 9 and num < 16:
        print_hexa(num, get_char(num % 10), '')
    elif num > 15 and num < 26:
        print_hexa(num, 1, num - 16)
    elif num > 25 and num < 32:
        print_hexa(num, 1, get_char(num % 26))
    elif num > 31 and num < 42:
        print_hexa(num, 2, num - 32)
    elif num > 41 and num < 48:
        print_hexa(num, 2, get_char(num % 42))
    elif num > 47 and num < 58:
        print_hexa(num, 3, num - 48)
    elif num > 57 and num < 64:
        print_hexa(num, 3, get_char(num % 58))
    elif num > 63 and num < 74:
        print_hexa(num, 4, num - 64)
    elif num > 73 and num < 80:
        print_hexa(num, 4, get_char(num % 74))
    elif num > 79 and num < 90:
        print_hexa(num, 5, num - 80)
    elif num > 89 and num < 96:
        print_hexa(num, 5, get_char(num % 90))
    else:
        print_hexa(num, 6, num - 96)
