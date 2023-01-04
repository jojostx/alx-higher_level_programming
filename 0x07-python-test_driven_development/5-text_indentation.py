#!/usr/bin/python3
"""
This module is composed of a function that prints a text 
with 2 new lines after each of these characters: '.', '?' and ':'

"""


def text_indentation(text):
    """ Function that adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    """ iterate through string, 
        and print each character
        if the current character is '.', '?' or ':'
            print the character followed by two newlines
    """

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
