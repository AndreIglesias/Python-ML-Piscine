kata = (2019, 9, 25, 3, 30)

if __name__ == '__main__':
    print("{:02d}/{:02d}/{:04d}".format(kata[1], kata[2], kata[0]), end=' ')
    print("{:02d}:{:02d}".format(*kata[3:]))
