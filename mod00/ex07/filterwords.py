import sys
import string


if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3, 'Usage: python3 filterwords.py <string> <number>'
    except AssertionError as msg:
        print(msg)
    if len(sys.argv) == 3:
        try:
            try:
                int(sys.argv[2])
                x = True
            except Exception:
                x = False
            try:
                int(sys.argv[1])
                y = False
            except Exception:
                y = True
            assert y, "First argument is not a string"
            assert x, "Second argument is not an integer"

            for x in string.punctuation:
                sys.argv[1] = sys.argv[1].replace(x, '')
            phrases = list(filter(lambda x: x != '', sys.argv[1].split(' ')))
            print(list(filter(lambda x: len(x) > int(sys.argv[2]), phrases)))
        except AssertionError as msg:
            print("AssertionError:", msg)
            print('Usage: python3 filterwords.py <string> <number>')
