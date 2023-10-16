def minCostPath(matrix, i, j):
    # Base case: reached the bottom-right corner
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[i][j]
    
    # If we are at the last row, can only move right
    if i == len(matrix) - 1:
        return matrix[i][j] + minCostPath(matrix, i, j + 1)
    
    # If we are at the last column, can only move down
    if j == len(matrix[0]) - 1:
        return matrix[i][j] + minCostPath(matrix, i + 1, j)
    
    # Move either right or down, choose the minimum cost
    right_cost = matrix[i][j] + minCostPath(matrix, i, j + 1)
    down_cost = matrix[i][j] + minCostPath(matrix, i + 1, j)
    
    return min(right_cost, down_cost)

# Example usage:
matrix = [
    [5, 9, 6],
    [11, 5, 2]
]

result = minCostPath(matrix, 0, 0)
print("Minimum Cost Path:", result)
