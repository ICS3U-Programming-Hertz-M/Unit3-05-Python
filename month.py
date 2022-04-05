#!/usr/bin/env python3
# Created by Hertz Antonella
# Created 4 April 2022
# This is a programs compares user number to the 12 month of the year


user_numb = input("Enter a number representing a month: ")

# Ask the user to enter a month number

user_numb = int(user_numb)

# Check the numbers and display the output


def find_month(month):
    months = {
        1: "{} is January.".format(month),
        2: "{} is February.".format(month),
        3: "{} is March.".format(month),
        4: "{} is April.".format(month),
        5: "{} is May.".format(month),
        6: "{} is June.".format(month),
        7: "{} is July.".format(month),
        8: "{} is August.".format(month),
        9: "{} is September.".format(month),
        10: "{} is October.".format(month),
        11: "{} is November.".format(month),
        12: "{} is December.".format(month),
    }
    return months.get(month, "Error.{} is not a month number".format(month))


if __name__ == "__main__":
    print(find_month(user_numb))
