def fibonacci():

    fib0 = 0
    fib1 = 1
    yield fib0
    yield fib1
    while True:
        fib2 = fib0 + fib1
        fib0,fib1 = fib1,fib2
        yield fib2


generator = fibonacci()
for i in range(5):
    print(next(generator))
