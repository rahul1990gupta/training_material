"""
Given an array, rotate the array 90 degrees clockwise.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated matrix = [
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]
"""

def rotate_counter_clockwise(arr):
    n = len(arr)

    narr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            narr[n-1-j][i] = arr[i][j]
    return narr        
