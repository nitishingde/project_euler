'''
https://projecteuler.net/problem=66

http://www.kurims.kyoto-u.ac.jp/EMIS/journals/GMN/yahoo_site_admin/assets/docs/1_GMN-8492-V28N2.190180001.pdf

TODO: https://en.wikipedia.org/wiki/Chakravala_method
'''

from lib import (
    Logger,
    ProjectEuler,
    floor,
    sqrt,
)
DEBUG = False

class ProjectEuler66(ProjectEuler):
    def logic(self, *args, **kwargs):
        ans = None
        N = kwargs['N'] if 'N' in kwargs else args[0]

        def sqrt_as_fraction(n: int):
            root_n = sqrt(n)

            ai_2, bi_2, ci_2 = 0, 1, n
            ai_1, bi_1, ci_1 = 1, 0, 1
            q0, qi = floor(root_n), None

            while True:
                k = sqrt(n-ci_2*ci_1)
                qi = floor(k+root_n)//ci_1
                if qi == 2*q0 and ai*ai-n*bi*bi == 1:
                    return (ai, bi)

                ai = int(qi*ai_1 + ai_2)
                bi = int(qi*bi_1 + bi_2)
                ci = int(2*qi*k + ci_2 - qi*qi*ci_1)

                ai_2, bi_2, ci_2 = ai_1, bi_1, ci_1
                ai_1, bi_1, ci_1 = ai, bi, ci

        x, D, y = 3, 2, 2
        for i in range(2, N+1):
            root_i = sqrt(i)
            if root_i != floor(root_i):
                xi, yi = sqrt_as_fraction(i)
                if xi > x:
                    x = xi
                    y = yi
                    D = i
                    if DEBUG: Logger.info(f'(x, D, y): ({x}, {D}, {y})')

        print(x, D, y)
        return D


if __name__ == '__main__':
    pe = ProjectEuler66()
    pe.solve(N=1000)
