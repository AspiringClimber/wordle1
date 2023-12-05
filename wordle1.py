# first try doing this with python instead of grep

import re

wordlistfile = "valid-wordle-words.txt"


# get first answer's clues: grey, green, yellow
def get_wrong_letters_as_array():
    #     bads = []
    s = input("enter non-matching letters as a string:  ")
    return string_to_array(s)


def get_greens_as_re():
    s = input("enter the greens as a regular expression (eg: '..a..'):  ")
    return s


def get_yellows_as_array():
    s = input("enter yellow letters as a string:  ")
    return string_to_array(s)


def string_to_array(s):
    return [c for c in s]


def matches_any_bad(bads, line):
    match = False
    for index in bads:
        if index in line:
            match = True
    return match


def matches_all(yellows, line):
    match = True
    for index in yellows:
        if index not in line:
            match = False
    return match


def main():
    print("Hello World!")
    f = open(wordlistfile, "r", encoding="utf-8")
    # reader = ""

    bads = get_wrong_letters_as_array()
    yellows = get_yellows_as_array()
    greens = get_greens_as_re()

    # evaluate each line of the wordlist
    for line in f:
        #    reader = reader + "."
        # eliminate greys
        if matches_any_bad(bads, line):
            # reader = reader + "b"
            pass
        elif re.search(greens, line):
            #       reader = reader + "g"
            if matches_all(yellows, line):
                print(line, end="")
    #          reader = reader + "y"


#   print(reader)


if __name__ == "__main__":
    main()
