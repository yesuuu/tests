def a(x, y):
    try:
        x/y
    except:
        return 'bsd'
    finally:
        print 'asasdasdasdasdd'
    # return x/y


def b(x, y):

    # shang = 1
    # try:
    #     shang = a(x, y)
    # finally:
    #     pass
    #
    # return shang

    return a(x, y)

shang = b(100, 0)
