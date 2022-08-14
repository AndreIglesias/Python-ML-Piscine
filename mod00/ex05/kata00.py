kata = (19, 42, 21)

if __name__ == '__main__':
    print('The',len(kata) ,'numbers are:', end=' ')
    print(*kata, sep=', ')
