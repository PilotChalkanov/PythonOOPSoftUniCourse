n = int(input())
def print_space(count):
    rhumbs = ""
    for _ in range(count):
        rhumbs += " "
    return rhumbs

def print_star(count):
    stars = ""
    for _ in range(count):
        stars += " *"
    return stars

for i in range(n):
    print(print_space(n - i) + print_star(i))
for i in range(n, 0, -1):
    print(print_space(n - i) + print_star(i))
