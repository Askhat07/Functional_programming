def lazy_primes():
    num = 2
    primes = []
    while True:
        if all(num % p != 0 for p in primes):
            yield num
            primes.append(num)
        num += 1

# Пример использования:
prime_generator = lazy_primes()
for _ in range(10):
    print(next(prime_generator))
