import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for x in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[x][::-1].swapcase() + ' ' * (x != 1), end='')
        print()
    else:
        print('Usage: python3 exec.py <Arg> [Arg] ...')
