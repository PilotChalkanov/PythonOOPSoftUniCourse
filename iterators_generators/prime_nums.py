
def get_primes(list_num):

    def is_prime(n):
        return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

    for num in list_num:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))