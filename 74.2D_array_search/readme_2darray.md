# Matrix Search Algorithm

## Problem Statement

Given an `m x n` integer matrix `matrix` with the following properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

The task is to check if a given integer `target` is present in the matrix, with a solution that achieves `O(log(m * n))` time complexity.

## Approach

We approach this problem by treating the matrix as a 1D sorted array, allowing us to apply binary search efficiently.

### Steps

1. **Flatten the 2D Matrix to a 1D View**:  
   - Imagine all elements of the `m x n` matrix laid out in a single row of length `m * n`.
   - Use `mid / n` to get the row index and `mid % n` to get the column index, where `n` is the number of columns.

2. **Binary Search**:  
   - Set initial search boundaries with `left = 0` and `right = m * n - 1`.
   - Calculate `mid` as the average of `left` and `right`.
   - If `matrix[mid / n][mid % n]` equals `target`, return `true`.
   - If it’s less than `target`, shift `left` to `mid + 1`.
   - Otherwise, shift `right` to `mid - 1`.
   - If the loop completes without finding the target, return `false`.

### Complexity

- **Time Complexity**: `O(log(m * n))` due to binary search.
- **Space Complexity**: `O(1)` as no extra space is used.

## Example

```cpp
vector<vector<int>> matrix = {
    {1, 3, 5, 7},
    {10, 11, 16, 20},
    {23, 30, 34, 60}
};
int target = 3;

Solution solution;
bool result = solution.searchMatrix(matrix, target);  // returns true
