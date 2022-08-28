import random

# function prototype
def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded."""
    if type(text) != str or type(sep) != str or \
       (option != None and type(option) != str) or \
       (option != None and option not in {'shuffle', 'unique', 'ordered'}):
        print("ERROR")
        return
    if sep == "":
        yield text
        return
    tab = text.split(sep)
    if option == 'ordered':
        tab.sort()
    elif option == 'unique':
        tab = [*set(tab)]
    elif option == 'shuffle':
        for i in range(len(tab) - 1, 0, -1):
            j = random.randint(0, i)
            tab[i], tab[j] = tab[j], tab[i]
    for x in tab:
        yield x

if __name__ == '__main__':

    #for x in generator("z x p w e a b a z x", option="shuffle"):
    #    print(x)

    txt = "This is a simple string for a basic test. Very simple."
    for x in generator(txt, sep=" ", option="shuffle"):
        print(x)
