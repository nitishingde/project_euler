'''
https://projecteuler.net/problem=18

@dp
'''

from lib import (
    Logger,
    max,
    namedtuple,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler18(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        pyramid = args[0]

        def logic1():
            '''
            Algorithm:
            - Create directed graph (adjacency list) with Position(row, column) for node
            - Adjacent nodes for Positon(row=r, column=c): [Position(row=r+1, column), Postion(row=r+1, column+1)]
            - Do DFS traversal to calculate sum for each route
            - T.C : O(2**(N-1)) where N = no of rows in pyramid
            '''
            graph, routes = {}, 0
            Position = namedtuple('Position', ['row', 'column'])
            for r, row in enumerate(pyramid[:-1]):
                for c, column in enumerate(row):
                    graph[Position(row=r, column=c)] = [Position(row=r+1, column=c), Position(row=r+1, column=c+1)]

            def dfs(node: Position):
                nonlocal routes
                if node not in graph: # leaf node
                    if DEBUG: routes += 1
                    return pyramid[node.row][node.column]

                return max([dfs(next_node) for next_node in graph[node]])+pyramid[node.row][node.column]
                # return max(dfs(graph[node][0], graph[node][1]))+pyramid[node.row][node.column]

            mx = dfs(Position(0,0))
            print(mx)
            if DEBUG: Logger.info(f'routes : {routes}')
            return mx

        def logic2():
            '''
            Algorithm:
            - Dynamic programming for memoization
            - Instead of finding max sum overall, find max sum for each postion in a row, going from top to bottom of pyramid
            '''
            dp = [[0]*len(row) for row in pyramid]
            dp[0][0] = pyramid[0][0] # base case

            for dp_previous_row, dp_current_row, pyramid_current_row in zip(dp, dp[1:], pyramid[1:]):
                dp_current_row[0] = pyramid_current_row[0] + dp_previous_row[0] # only 1 adjacent node above
                dp_current_row[-1] = pyramid_current_row[-1] + dp_previous_row[-1] # only 1 adjacent node above
                for column in range(1, len(dp_current_row)-1):
                    dp_current_row[column] = pyramid_current_row[column] + max(dp_previous_row[column-1:column+1])

            mx = max(dp[-1])
            print(mx)
            return mx

        ans = logic2()

        return ans

if __name__ == '__main__':
    pe = ProjectEuler18()

    pyramid = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    pe.solve(pyramid)

    pyramid = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]
    pe.solve(pyramid)
