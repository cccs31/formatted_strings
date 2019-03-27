"""Contains functions that only use validated input."""

import decimal
import input_checks as ic


def format1():
    """Exponentiates a number to an exponent and prints the result."""
    print("1 - single-line power")
    # TODO: round and auto convert num and exp to int if needed
    num = ic.input_Decimal("Enter a number: ")
    exp = ic.input_Decimal("Enter an exponent: ")
    print("{} to the {} is {}".format(num, exp, num**exp))


def format2():
    """Prints a formatted table of exponentiated numbers.
    
    The user is prompted to enter two strings of numbers and exponents,

    """
    print("2 - table power")

    nums = format2_get_input("Enter numbers separated by commas: ")
    exps = format2_get_input("Enter exponents separated by commas: ")

    results = []
    # Exponentiate the numbers using exponents round to an int at a given precision if it is not an int already
    for num in nums:
        for exp in exps:
            if not float(exp).is_integer() or not float(num).is_integer():
                PRECISION = ic.input_int_precision("Enter a precision (default 6): ")
                results.append(round(num**exp, PRECISION))
            else:  # No need to round if result is an integer
                results.append(num**exp)

    print(nums)
    print(exps)
    print(results)
    return

    # Calculate width of the results to set table column width
    # TODO: Calculate results width
    results_width = []
    for i in results:
        results_width.append(len(num))
    print(results_width)
    # Prints variable-width table according to user input
    # Rows contain numbers, columns contain exponents
    MAX_NUM_WIDTH = max(list(map(len, str(nums))))
    # TODO: Clean up this section after completing above
    #MAX_RESULTS_WIDTH = [[len(j) for j in i]  for i in results]
    # print(MAX_RESULTS_WIDTH)
    # MAX_RESULTS_WIDTH = max(list(map(len, results)))
    HEADER_PADDING = "    "  # Padding between each exp in header
    div_width_total = 0

    # Header row
    # TODO: Use result width to set column width
    print(" " * MAX_NUM_WIDTH, end="")  # Align header to exps columns
    div_width_total += MAX_NUM_WIDTH  # Include inital header alignment padding
    for exp in exps:
        num_width = len(exp)
        div_width_total += num_width + len(HEADER_PADDING)
        print("{}{:>}".format(HEADER_PADDING, exp), end="")
    print()
    print("-" * div_width_total)  # Dashed divider line

    # Number rows
    for num in nums:
        print("{}{} |".format(num, " " * (MAX_NUM_WIDTH - len(num))))
        # print(num)

# Reads a user-inputted string and checks to see if it is valid


def format2_get_input(prompt):
    """Returns formatted numbers for the function format2.
     which prompts
    the user for a list of numbers and exponents to exponentiate.
    """
    while True:
        # Prompt and parse input to strings for each number, with each
        # number in a separate string in a list
        inputs = ic.format2_parse_input(input(prompt))

        # Only allow numbers as input, reprompt if invalid
        if not ic.format2_check_numbers(inputs):
            print("Invalid input! Try again.")
        else:
            # Convert strings to Decimals
            return [decimal.Decimal(i) for i in inputs]
