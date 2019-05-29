from time import time
from abc import ABCMeta, abstractmethod

def calculate_execution_time(func):
    def decorator(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        print(f'Execution time\t: {time()-start} seconds')
        return ret
    return decorator

class Logger:
    @staticmethod
    def info(val, file='info.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def warning(val, file='warning.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def error(val, file='error.log'):
        print(val, file=open(file, 'a'), flush=True)

    @staticmethod
    def terminal(val):
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

def sum_of_arithmetic_progression(first, diff, n):
    """Sum of Arithmetic Progression of 'n' elements with differnce 'diff' and 'first' as first element

    Arguments:
        first {int} -- first number in the progression
        diff {int} -- differnce between 2 consecutive numbers
        n {int} -- number of elements

    Returns:
        int -- sum of arithmetic progression
    """
    return (n*(2*first + (n-1)*diff)) >> 1