
# function soulution
def even_int_func(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
        return result


# generator solution
def even_int_func(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
