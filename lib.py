from abc import (
    ABCMeta,
    abstractmethod,
)
from functools import (
    reduce,
)
from math import (
    ceil,
    floor,
    log,
    sqrt,
)
from operator import (
    mul,
)
from pprint import (
    pprint
)
from time import (
    time,
)

def calculate_execution_time(func):
    def decorator(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        print(f'Execution time\t: {time()-start} seconds\n')
        return ret
    return decorator

class Logger:
    @staticmethod
    def info(val: str, file='info.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def warning(val: str, file='warning.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def error(val: str, file='error.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def terminal(val: str):
        print(val, flush=True)

class ProjectEuler(metaclass=ABCMeta):

    @calculate_execution_time
    def solve(self, *args, **kwargs):
        """Method to be called by user

        Warnings:
            - Do not implement this method in subclass
            - This is the only public method of this class that should be called by the user

        Returns:
            Result
        """
        return self.logic(*args, **kwargs)

    @abstractmethod
    def logic(self, *args, **kwargs):
        """Method (user-logic) to be implemented in subclass

        Raises:
            NotImplementedError: [description]
        """
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__

def sum_of_arithmetic_progression(first: int, diff: int, n: int) -> int:
    """Sum of Arithmetic Progression of 'n' elements with differnce 'diff' and 'first' as first element
    TC : O(1)
    SC : O(1)

    Arguments:
        first {int} -- first number in the progression
        diff {int} -- differnce between 2 consecutive numbers
        n {int} -- number of elements

    Returns:
        int -- sum of arithmetic progression
    """
    return (n*(2*first + (n-1)*diff)) >> 1

def prime_factorization(N: int) -> list:
    """Find prime factors and their count for given number 'N'
    TC : O(root(N))

    Arguments:
        N {int} -- Number

    Returns:
        List of sorted tuples -- (prime factors, count)
    """
    prime_factors = []
    # 2 is the only even prime number, solve for it first
    if N&1 == 0:
        count = 1
        N >>= 1
        while N&1 == 0:
            N >>= 1
            count += 1
        prime_factors.append((2, count))

    # iterate over odd numbers
    for factor in range(3, floor(sqrt(N))+1, 2):
        if N%factor == 0:
            count = 1
            N //= factor
            while N%factor == 0:
                N //= factor
                count += 1
            prime_factors.append((factor, count))

    if N != 1:
        prime_factors.append((N, 1))
        N = 1

    return prime_factors

def is_palindrome(inp: str) -> bool:
    """Checks if given string is palinrome or not

    Arguments:
        inp {str} -- input string

    Returns:
        bool -- True if palindrome ele False
    """
    return inp == inp[::-1]

def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor (Non-recursive)
    TC : O(log(min(a,b)))

    Arguments:
        a {int} -- number
        b {int} -- number

    Returns:
        int -- gcd
    """
    while a:
        a, b = b%a, a

    return b

def lcm(a: int, b: int) -> int:
    """Least Common Multiple
    TC : O(log(min(a,b)))

    Arguments:
        a {int} -- number
        b {int} -- number

    Returns:
        int -- lcm
    """
    return (a*b) // gcd(a, b)

pow = pow

def build_sieve(n: int) -> tuple:
    """Build sieve of Eratosthenes
    TC : O(n*log(log(n)))

    Arguments:
        n {int} -- upper limit

    Returns:
        tuple(list, list) -- list of primes, bitmask for primes
    """
    if n < 2:
        return [], [False]*n

    is_prime = [True if no&1 else False for no in range(n+1)]
    is_prime[1], is_prime[2], primes = False, True, [2]
    for no in range(3, n+1, 2):# ceil(sqrt(n))
        if is_prime[no]:
            primes.append(no)
            for multiple in range(no*no, n+1, no):
                is_prime[multiple] = False

    return primes, is_prime

def build_sieve_(n: int) -> list:
    """Build sieve of Eratosthenes

    Arguments:
        n {int} -- upper limit

    Returns:
        list -- list of primes
    """
    if n < 2:
        return []

    primes = [2]
    for n in range(3, n+1, 2):
        primes.append(n)
        limit = floor(sqrt(n))
        for prime in primes:
            if prime <= limit:
            # if prime*prime <= n:
                if n%prime == 0:
                    primes.pop()
                    break
            else:
                break

    return primes

max = max

if __name__ == '__main__':

    def unit_test(subject):
        def decorator(func):
            def wrapper():
                print(f'Unit Testing $({subject.__name__}):')
                ret = func()
                print()
                return ret
            return wrapper
        return decorator

    # unit testing
    @unit_test(sum_of_arithmetic_progression)
    def test_sum_of_arithmetic_progression():
        print(sum_of_arithmetic_progression(1, 1, 4) == 10)
        print(sum_of_arithmetic_progression(2, 3, 4) == 26)

    @unit_test(prime_factorization)
    def test_prime_factorization():
        print(prime_factorization(23) == [(23,1)])
        print(prime_factorization(20) == [(2,2), (5,1)])
        print(prime_factorization(169) == [(13,2)])

    @unit_test(is_palindrome)
    def test_is_palindrome():
        print(is_palindrome('racecar') == True)
        print(is_palindrome('1221') == True)
        print(is_palindrome('Racecar') == False)
        print(is_palindrome('hello world') == False)
        print(is_palindrome('1') == True)
        print(is_palindrome('') == True)

    @unit_test(gcd)
    def test_gcd():
        print(gcd(2, 3) == 1)
        print(gcd(1, 10) == 1)
        print(gcd(8, 12) == 4)

    @unit_test(lcm)
    def test_lcm():
        print(lcm(2, 3) == 6)
        print(lcm(1, 10) == 10)
        print(lcm(8, 12) == 24)

    @unit_test(build_sieve)
    def test_build_sieve():
        print(build_sieve(30)[0] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        print(build_sieve(1)[0] == [])

    @unit_test(build_sieve_)
    def test_build_sieve_():
        print(build_sieve_(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        print(build_sieve_(1) == [])
        print(build_sieve_(1000) == build_sieve(1000)[0])

    test_sum_of_arithmetic_progression()
    test_prime_factorization()
    test_is_palindrome()
    test_gcd()
    test_lcm()
    test_build_sieve()
    test_build_sieve_()
