import multiprocessing


def square(num):
    print(num * num)


def cube(num):
    print(num * num * num)


if __name__ == '__main__':
    # print(multiprocessing.cpu_count())

    p1 = multiprocessing.Process(target=square, args=(3,))
    p2 = multiprocessing.Process(target=cube, args=(3,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
