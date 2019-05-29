'''
https://projecteuler.net/problem=1

@math Arithmetic progression
@combinatorics Inclusion-Exclusion principle

For extra reading
@note https://cp-algorithms.com/combinatorics/inclusion-exclusion.html
'''

from lib import (
    Logger,
    ProjectEuler,
    sum_of_arithmetic_progression,
)
DEBUG = False

class ProjectEuler1(ProjectEuler):
    def logic(self, *args, **kwargs):
        ans = None
        N = kwargs['N'] if 'N' in kwargs else args[0]

        sum_of_multiples_of_3 = sum_of_arithmetic_progression(3, 3, (N-1)//3)
        sum_of_multiples_of_5 = sum_of_arithmetic_progression(5, 5, (N-1)//5)
        sum_of_multiples_of_15 = sum_of_arithmetic_progression(15, 15, (N-1)//15)

        if DEBUG: Logger.info(f'sum_of_multiples_of_3  : {sum_of_multiples_of_3}')
        if DEBUG: Logger.info(f'sum_of_multiples_of_5  : {sum_of_multiples_of_5}')
        if DEBUG: Logger.info(f'sum_of_multiples_of_15 : {sum_of_multiples_of_15}')

        # A => multiples of 3
        # B => multiples of 5
        # n(A U B) = n(A) + n(b) - n(A intersection B)
        ans = sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler1()
    pe.solve(N=10)
    pe.solve(N=1000)
