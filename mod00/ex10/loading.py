import time


def ft_progress(lst):
    t = time.process_time()
    t2 = t
    ln = len(lst)
    for i in range(ln):
        progress = (int((i / ln) * 20))
        print('ETA: {:.02f}s [{: 3d}%] [{:20s}] {:}/{:}\
 | elapsed time {:.02f}s'.format(
            (100 * (t2 - t) / (i + int(i == 0))) * ln, int(i / ln * 100),
            '='*progress + '>', i + 1, ln,
            100 * (time.process_time() - t)), end='\r')
        t2 = time.process_time()
        yield lst[i]
    print('ETA: {:.02f}s [{: 3d}%] [{:20s}] {:}/{:}\
 | elapsed time {:.02f}s'.format(
            100 * (time.process_time() - t), 100, '='*20, ln, ln,
            100 * (time.process_time() - t)), end='\r')


if __name__ == '__main__':
    from time import sleep
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
