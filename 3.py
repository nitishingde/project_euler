'''
https://projecteuler.net/problem=3
'''

from lib import (
    Logger,
    prime_factorization,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler3(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 600851475143

        prime_factors = prime_factorization(N)
        if DEBUG: Logger.info(f'Prime factors of {N}: {prime_factors}')
        ans = prime_factors[-1][0]

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler3()
    pe.solve(13195)
    pe.solve(600851475143)