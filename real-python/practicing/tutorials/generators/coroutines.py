
# * Example 1

def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)


c = counter('California')
next(c)
c.send('Cali')
c.send('nia')
c.send(5)
c.send('hello')


# * Example 2

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap


@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        print(x)


c = coroutine_example()
c.send('success!')

# * Example 3


def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()


@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print(f'{string}: {count}')


c = match_counter('Da')
sender('names.txt', c)


@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line) > n:
                print(line)
                count += 1
    except GeneratorExit:
        print(f'longer than {n}: {count}')


l = longer_than(20)
sender('names.txt', l)


# * Example 4

@coroutine_decorator
def router():
    try:
        while True:
            line = yield
            (first, last) = line.split(' ')
            fnames.send(first)
            lnames.send(last.strip())
    except GeneratorExit:
        fnames.close()
        lnames.close()


@coroutine_decorator
def file_write(filename):
    try:
        with open(filename, 'a') as file:
            while True:
                line = yield
                file.write(line+'\n')
    except GeneratorExit:
        file.close()
        print('one file created')


if __name__ == "__main__":
    fnames = file_write('first_names.txt')
    lnames = file_write('last_names.txt')
    router = router()
    for name in open('names.txt'):
        router.send(name)
    router.close()
