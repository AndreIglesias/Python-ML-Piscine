def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("ft_reduce() arg 2 must support iteration")
    #try:
    for x in range(len(iterable)):
        if x == 0:
            if isinstance(iterable[x], str):
                c = ''
            elif isinstance(iterable[x], int) or isinstance(iterable[x], float):
                c = 0
            elif isinstance(iterable[x], list):
                c = []
            elif isinstance(iterable[x], tuple):
                c = ()
            else:
                c = None
        c = function_to_apply(c, iterable[x])
    return c
    #except Exception:
    #    return None
