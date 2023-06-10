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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
