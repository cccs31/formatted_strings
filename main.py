"""The main file for the user to choose which function to run."""

import powers
import input_checks as ic


def main():
    print("Enter an integer to select a function to run. Invalid numbers will run all.")
    print("1 - single-line power")
    print("2 - table power")

    request = int(ic.input_Decimal())
    print()

    """Change later to remove else. if > or < than number of blocks, print all"""
    if request == 1:
        powers.format1()
    elif request == 2:
        powers.format2()
    else:
        powers.format1()
        print()
        powers.format2()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # Handles Ctrl+C to quit the program without errors
        raise SystemExit
