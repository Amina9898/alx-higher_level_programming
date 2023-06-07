#!/usr/bin/python3
"""This is a module that defines the text_indentation() function."""


def text_indentation(text):
    """
    Defines a function that prints a text with 2 new
    lines after each of these characters: . ? :

    args:
        text: input to iterate through and indent
    Returns: indented text
    """
    txt = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        txt += i
        if i == "." or i == "?" or i == ":":
            print(txt.strip())
            print()
            print()
            txt = ""

    print(txt.strip())
