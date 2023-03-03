#!/usr/bin/python3
""" Script to calculate the perimeter of an island """


def island_perimeter(grid):
    """ function to calculate the perimeter of the grid
    """
    vector = set() 
    """To keep track of paths checked"""

    def dfs(i, j):
        """applying depth first search
        """
        if i >= len(grid) or j >= len(grid[0]) or \
        i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in vector:
            return 0

        vector.add((i, j))

        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)

        return perim


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
               return dfs(i, j)
    return 0
