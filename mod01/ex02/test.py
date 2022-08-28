from vector import Vector

if __name__ == '__main__':
    v1 = Vector([[3.0], [2.0], [1.0]])
    v2 = Vector((1, 4))
    v3 = Vector(3)
    print(v1, '+', v2, '=', v1 + v2)
    print(v1, '-', v2, '=', v1 - v2)
    print(v2, '-', v1, '=', v2 - v1)

    print(v1, '*', str(3), '=', v1 * 3)
    print(str(3), '*', v1, '=', v1 * 3)

    print(v1, '/', str(3), '=', v1 / 3)
    try:
        print(str(3), '/', v1, '=', 3 / v1)
    except NotImplementedError as msg:
        print('NotImplementedError:', msg)

    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    v2 = v1 / 2.0
    print(v2)
    try:
        v1 / 0.0
    except ZeroDivisionError as msg:
        print('ZeroDivisionError:', msg)
    try:
        2.0 / v1
    except NotImplementedError as msg:
        print('NotImplementedError:', msg)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    print(v1.T())
    print(v1.T().shape)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    print(v1.T())
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    print(v2.T())
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    print(v1)
