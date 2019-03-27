"""Only contains functions that deals with unvalidated input."""

import decimal


def format2_parse_input(input):
    """Splits a string of values into strings containing one value.

    The string of values are separated by commas, which are split into
    into separate strings within a list.
    """
    input = "".join(input.split())  # Remove all whitespace
    input = input.replace(",", " ")  # Replace commas with a space
    input = input.split()  # Split each number into a separate string
    return input


def format2_check_numbers(*inputs):
    """Returns whether a list of strings only contains numbers.

    This should take a list(s) of strings that contain one value in
    each string from format2_parse_input, and checks if it only
    contains numbers. If it contains non-numbers, it returns False. If
    it contains only numbers, it returns True.
    """
    for i in inputs:
        try:
            float("".join(i))
        except ValueError:
            return False
    return True


def input_Decimal(prompt="", error="Invalid number! Try again."):
    """Prompt the user to input a number, which is only accepted if it
    can be converted to a Decimal. 
    
    Returns the number if it is valid input, otherwise the user is
    re-prompted if an invalid number is input.
    """
    while True:
        number = input(prompt)
        try:
            number = decimal.Decimal(number)
        except ValueError:
            print(error)
        else:
            return number


def input_int_precision(prompt="", error="Invalid number! Try again."):
    """Prompt the user to input an int, which will be used to set the
    precision of the formatted exponentiation table in format2.

    Returns a default value of 6 if nothing is entered, and re-prompts
    the user if an invalid number is input.
    """
    while True:
        number = input(prompt)
        try:
            if number.split() == []:  # No value entered
                return 6
            if not float(number).is_integer():
                raise ValueError
        except ValueError:
            print(error)
        else:
            return int(number)
