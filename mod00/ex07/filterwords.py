import sys
import string


if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3, "Two arguments must be provided"
    except AssertionError as msg:
        print("AssertionError:", msg)
        print('Usage: python3 filterwords.py <string> <number>')
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
            phrases = [x for x in sys.argv[1].split(' ') if x != '']
            print([x for x in phrases if len(x) > int(sys.argv[2])])
        except AssertionError as msg:
            print("AssertionError:", msg)
            print('Usage: python3 filterwords.py <string> <number>')
