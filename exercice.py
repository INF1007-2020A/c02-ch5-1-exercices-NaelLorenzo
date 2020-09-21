#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    return "uuu"


def format_number(number, num_decimal_digits):
    # Séparation entier décimal
    decimal_part = abs(number) % 1.0
    whole_part = int(abs(number))

    # Formater partie décimal
    #    Approche plus automatique : decimal_string = f"(decimal_part :.{num_decimal_digits}f"[1:]
    decimal_str = str(int(round(decimal_part * 10 ** num_decimal_digits)))
    decimal_str = "."+"0"*(num_decimal_digits) - len()
    # Formater partie entière
    while whole_part >= 1000:
        digits = whole_part % 1000
        digit_string = f"{digits :.0}"

    # Concaténer les 2


    return ""


def get_triangle(num_rows):
    border_char = '+'
    triangle_char = 'A'

    triangle_width = '...'
    return ""


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
