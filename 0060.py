from euler_utils import isPrime, listPrimes2


def prime_pair(x, y):
    return isPrime(int(str(x) + str(y))) and isPrime(int(str(y) + str(x)))


def find_pairs(primes):
    prime_pairs = {}
    for i, p in enumerate(primes):
        pairs = set()
        for j in range(i + 1, len(primes)):
            if prime_pair(p, primes[j]):
                pairs.add(primes[j])
        prime_pairs[p] = pairs
    return prime_pairs


def find_groups(max_prime=9000, n=5):
    def fully_connected(p, path):
        return all(p in prime_pairs.get(path_item, set()) for path_item in path)

    def backtracking(prime_pairs, n, path=None):
        if path is None:
            path = []

        if len(path) == n:
            yield path[:]
        else:
            if not path:
                for p, v in prime_pairs.items():
                    if v:
                        yield from backtracking(prime_pairs, n, path + [p])
            else:
                p = path[-1]
                for t in sorted(prime_pairs[p]):
                    if t > p and fully_connected(t, path):
                        yield from backtracking(prime_pairs, n, path + [t])

    primes = list(listPrimes2(max_prime))
    prime_pairs = find_pairs(primes)

    return next(backtracking(prime_pairs, n), None)


def main():
    print(sum(find_groups(9000, 5)))


main()
