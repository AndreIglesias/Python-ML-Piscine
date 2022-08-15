import sys
import string

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        string = ' '.join(sys.argv[1:])
        try:
            s = set(map(lambda x: x.isalnum() or x == ' ', string))
            assert False not in s, 'The program supports space\
 and alphanumeric characters'
            for c in range(len(string)):
                print(morse[string[c].lower()], end='')
                if c != len(string) - 1:
                    print(' ', end='')
            print()
        except AssertionError as msg:
            print('AssertionError:', msg)
    else:
        print('Usage: python3 sos.py <message> [message] ...')
