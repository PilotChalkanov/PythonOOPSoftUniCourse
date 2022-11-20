import functools

def cache(func):
    cache_dict={}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper


@cache
def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    print(f"fibonacci {n}: {result}")
    return result

fib(5)


