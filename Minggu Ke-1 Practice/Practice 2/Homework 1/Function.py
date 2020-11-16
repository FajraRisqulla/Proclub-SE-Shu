from switchcase import switch
from os import system


def half_pyramid_pattern(row):
    for _ in range(0, row):
        for __ in range(0, _ + 1):
            print("*", end="")
        print()
    print()


def half_pyramid_pattern_inverted(row):
    for _ in range(0, row):
        for __ in range(0, row - _):
            print("*", end="")
        print()
    print()


def half_pyramid_pattern_mirrored(row):
    for _ in range(0, row):
        for __ in range(0, row - _ - 1):
            print(" ", end="")
        for __ in range(0, _ + 1):
            print("*", end="")
        print()
    print()


def full_pyramid_pattern(row):
    for _ in range(0, row):
        for __ in range(0, row - _ - 1):
            print(" ", end="")
        for __ in range(0, _ + 1):
            print("*", end="")
        for __ in range(0, _):
            print("*", end="")
        print()
    print()


def full_pyramid_pattern_inverted(row):
    for _ in range(0, row):
        for __ in range(0, _):
            print(" ", end="")
        for __ in range(0, row - _):
            print("*", end="")
        for __ in range(0, row - _ - 1):
            print("*", end="")
        print()
    print()


def print_pattern(pattern, row):
    for case in switch(pattern):
        if case(1):
            print()
            half_pyramid_pattern(row)
        elif case(2):
            print()
            half_pyramid_pattern_inverted(row)
        elif case(3):
            print()
            half_pyramid_pattern_mirrored(row)
        elif case(4):
            print()
            full_pyramid_pattern(row)
        elif case(5):
            print()
            full_pyramid_pattern_inverted(row)
        else:
            print("Invalid")


def tampil_menu_segitiga():
    print("1. Half Pyramid Pattern")
    print("2. Half Pyramid Pattern Inverted")
    print("3. Half Pyramid Pattern Mirrored")
    print("4. Full Pyramid Pattern")
    print("5. Full Pyramid Pattern Inverted")
