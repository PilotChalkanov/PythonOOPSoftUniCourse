def even_parameters(f):
    def wrappper(*args):
        if all([isinstance(x, int) and x % 2 == 0 for x in args]):
            return f(*args)
        else:
            return "Please use only even numbers!"
    return wrappper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))