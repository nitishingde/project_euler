'''
https://projecteuler.net/problem=6

@note http://mathworld.wolfram.com/PowerSum.html
'''

from lib import (
    Logger,
    pow,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler6(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 100

        # sum of squares 1st N natural numbers: N(N+1)(2N+1)/6
        # sum of 1st N natural numbers: N(N+1)/2

        # sum_of_squares = (N * (N+1) * (2*N+1)) // 6
        # square_of_sums = ((N * (N+1)) // 2)**2
        # ans = square_of_sums - sum_of_squares

        ans = (3*pow(N, 4) + 2*pow(N, 3) - 3*pow(N, 2) - 2*pow(N, 1)) // 12

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler6()
    pe.solve(10)
    pe.solve(100)