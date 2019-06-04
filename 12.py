'''
https://projecteuler.net/problem=12
@math A.P, Factorization
@note https://cp-algorithms.com/algebra/factorization.html
'''

from lib import (
    factorization,
    Logger,
    ProjectEuler,
    sum_of_arithmetic_progression,
)
DEBUG = False

class ProjectEuler12(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = 0
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 500

        n, triangular_number = 1, sum_of_arithmetic_progression(1, 1, 1)
        factors = factorization(triangular_number)
        while len(factors) <= N:
            n, triangular_number = n+1, sum_of_arithmetic_progression(1, 1, n+1)
            factors = factorization(triangular_number)
            if DEBUG: Logger.info(f'n : {n} triangular number : {triangular_number}')
            if DEBUG: Logger.info(f'factors({triangular_number}) : {factors} Total : {len(factors)}')

        print(triangular_number)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler12()
    pe.solve(5)
    pe.solve(500)