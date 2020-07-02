# 13195 are 5, 7, 13 and 29

# find prime factors of the number 600851475143


def get_prime_factors_2(number_to_factor):
    limit = int(number_to_factor**(1/2))
    primes = [num for num in range(2, limit) if all(num % m != 0 for m in range(2, int(num**(1/2))))]
    return [prime for prime in primes if number_to_factor % prime == 0]


print(get_prime_factors_2(600851475143))
