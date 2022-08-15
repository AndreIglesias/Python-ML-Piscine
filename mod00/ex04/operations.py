import sys


def sum_args(a, b):
    print('Sum:        ', a + b)
    print('Difference: ', a - b)
    print('Product:    ', a * b)
    try:
        assert b != 0, 'ERROR'
        print('Quotient:   ', a / b)
        print('Remainder:  ', a % b)
    except AssertionError as msg:
        print('Quotient:   ', msg, '(division by zero)')
        print('Remainder:  ', msg, '(modulo by zero)')


if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3, "Two arguments must be provided"
    except AssertionError as msg:
        if len(sys.argv) != 1:
            print('AssertionError:', msg)
        print('Usage: python3 operations.py <number1> <number2>')
        print('Example:\n\tpython3 operations.py 10 3')
    if len(sys.argv) == 3:
        try:
            try:
                int(sys.argv[1])
                x = True
            except Exception:
                x = False
            try:
                int(sys.argv[2])
                y = True
            except Exception:
                y = False
            assert x and y, "Argument is not an integer"
            sum_args(int(sys.argv[1]), int(sys.argv[2]))
        except AssertionError as msg:
            print('AssertionError:', msg)
