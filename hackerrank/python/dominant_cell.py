#
# Problem description:
# Find the count of dominant cells
#
# Example:
# Input:
# 9 1 1
# 8 1 9
# 1 1 1
# Visualisation:
# 9 . .
# . . 9
# . . .
# Output:
# 2
def numCells(grid: list[list[int]]) -> int:
    dominant_cells = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            neighbors = []
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:
                    neighbors.append(grid[ni][nj])

            if neighbors and grid[i][j] > max(neighbors):
                dominant_cells += 1

    return dominant_cells


if __name__ == "__main__":
    assert numCells([[9, 1, 1], [8, 1, 9], [1, 1, 1]]) == 2
