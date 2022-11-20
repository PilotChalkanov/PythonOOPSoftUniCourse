def cache(func):
    log = {}
    def wrapper(n):
        if n in log:
            return log[n]
        else:
            log[n] = func(n)
            return func(n)
    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print(fibonacci.log)