from time import time
from abc import ABCMeta, abstractmethod
from math import sqrt, floor

def calculate_execution_time(func):
    def decorator(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        print(f'Execution time\t: {time()-start} seconds')
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

def prime_factorization(N: int):
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

if __name__ == '__main__':
    # unit testing
    print(sum_of_arithmetic_progression(1, 1, 4) == 10)
    print(sum_of_arithmetic_progression(2, 3, 4) == 26)

    print(prime_factorization(23) == [(23,1)])
    print(prime_factorization(20) == [(2,2), (5,1)])
    print(prime_factorization(169) == [(13,2)])
