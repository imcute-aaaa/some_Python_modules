def check(*args):
    for index, i in enumerate(args):
        print('%d:%s' % (index+1, i))
    a = input('Which one do you choose?')
    return a, args[a]


def inptype(a, b):
    i = input(a)
    try:
        k = b(i)
        return k
    except:
        print('Ilegal input!')
        return inptype(a, b)


