import string
import sys


def text_analyzer(s=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if s is not None:
        try:
            assert isinstance(s, str), "Argument is not a string"
        except AssertionError as msg:
            print('AssertionError:', msg)
            return
        print('The text contains', len(s), 'character(s):')
        ls = len(list(filter(lambda x: x.isupper(), s)))
        print('-', ls, 'upper letter(s)')
        ls = len(list(filter(lambda x: x.islower(), s)))
        print('-', ls, 'lower letter(s)')
        ls = len(list(filter(lambda x: x in string.punctuation, s)))
        print('-', ls, 'punctuation mark(s)')
        ls = len(list(filter(lambda x: x == ' ', s)))
        print('-', ls, 'space(s)')
    else:
        s = input('What is the text to analyze?\n>>> ')
        text_analyzer(s)


if __name__ == '__main__':
    try:
        assert len(sys.argv) <= 2, "More than one argument are provided"
    except AssertionError as msg:
        print('AssertionError:', msg)
        print("Usage: python3 count.py <Text>")
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv) == 1:
        text_analyzer(input('Text to analyze:\n>> '))
