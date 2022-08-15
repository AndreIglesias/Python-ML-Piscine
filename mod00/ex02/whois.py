import sys

if __name__ == '__main__':
    try:
        assert len(sys.argv) <= 2, "More than one argument are provided"
    except AssertionError as msg:
        print('AssertionError:', msg)
    if len(sys.argv) == 2:
        try:
            try:
                int(sys.argv[1])
                x = True
            except Exception:
                x = False
            assert x, "Argument is not an integer"
            if int(sys.argv[1]) == 0:
                print('I\'m Zero.')
            elif int(sys.argv[1]) % 2 == 0:
                print('I\'m Even.')
            else:
                print('I\'m Odd.')
        except AssertionError as msg:
            print('AssertionError:', msg)
    else:
        print('Usage: python3 whois.py <Number>')
