from decorators import repeat

@repeat(n_times=4)
def greet(name):
    print(f"Hello {name}")

greet("Nik")