'''
https://projecteuler.net/problem=15

@combinatorics

@note http://mathworld.wolfram.com/Permutation.html
'''

from lib import (
    factorial,
    Logger,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler15(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 20
        '''
        Algorithm:
        - Only moves allowed are Down(D) and Right(R)
        - No matter what path is taken, one needs N D-moves and N R-moves to reach the destination
        - Let's describe the path taken as a string in terms of D and R moves : 'DDD...RRR...'
        - Permutation of above string is (2N)! / ((N!)*(N!))
        '''

        ans = factorial(2*N)//(factorial(N)**2)

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler15()
    pe.solve(2)
    pe.solve(20)