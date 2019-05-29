'''
https://projecteuler.net/problem=2

@dp Fibonacci numbers

For extra reading
@note https://cp-algorithms.com/algebra/fibonacci-numbers.html
'''

from lib import (
    Logger,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler2(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = 0
        limit = args[0] if len(args) else 4000000

        a, b = 1, 2
        if DEBUG:
            Logger.info(f'Fibonacci series upto {limit}:')
            Logger.info(f'{a}')
            Logger.info(f'{b}')

        while b < args[0]:
            # add b only if even
            ans += b if b&1 == 0 else 0
            a, b = b, a+b
            if DEBUG: Logger.info(f'{b}')

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler2()
    pe.solve(90)
    pe.solve(4000000)