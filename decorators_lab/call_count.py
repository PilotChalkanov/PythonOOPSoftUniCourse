import functools
class count_call:

    def __init__(self,func):
        self.count = 0
        self.func = func
        functools.update_wrapper(self,func)
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@count_call
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

