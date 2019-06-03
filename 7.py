'''
https://projecteuler.net/problem=7

@math https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
'''

from lib import (
    build_sieve,
    ceil,
    floor,
    log,
    Logger,
    ProjectEuler,
    sqrt,
)
DEBUG = False

class ProjectEuler7(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 10001

        def logic1():
            '''
            ALgorithm:
            - #(primes < x) ~= x / ln(x)     (as x -> inf)
            - Here N = #(primes < x), then x?
            - binary search x and break when x / ln(x) <= 2*N
            '''
            low, up = 1<<1, 1<<63
            while True:
                x = (low+up)//2
                prime_count = x // ceil(log(x))
                if prime_count <= (N<<1):
                    break
                elif prime_count < N:
                    low = x
                elif N < prime_count:
                    up = x

            primes = []
            while len(primes) < N:# if you dont find it 1st attempt (remember x is found as a result of approximation)
                primes, _ = build_sieve(x)
                if DEBUG: Logger.info(f'Limit: {x}, Length of list: {len(primes)}')
                x += N

            print(primes[N-1])
            return primes[N-1]

        def logic2():
            '''
            Algorithm:
            - Keep on finding primes till Nth prime is found
            - Iterate over odd numbers
                - Iterate over primes, check if prime|odd_number upto prime<=root(odd_number)
                - If it does, then it means it's not prime
            '''
            primes = [2]
            n = 3
            while len(primes) < N:
                primes.append(n)
                limit = floor(sqrt(n))
                for prime in primes:
                    if prime <= limit:
                        if n%prime == 0:
                            primes.pop()
                            break
                    else:
                        break
                n += 2
            print(primes[N-1])
            return primes[N-1]

        ans = logic1()
        # ans = logic2()
        return ans

if __name__ == '__main__':
    pe = ProjectEuler7()
    pe.solve(6)
    pe.solve(10001)
    pe.solve(100001)