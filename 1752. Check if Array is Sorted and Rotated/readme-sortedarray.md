# Check if Array is Sorted and Rotated

This C++ code is designed to determine if an array is sorted in non-decreasing order, possibly after a single rotation. A rotation means shifting elements from the beginning to the end or vice-versa, like `[3,4,5,1,2]`, which is a rotated version of `[1,2,3,4,5]`.

## Approach

1. **Count the Inversions**:

   - We count instances where the current element is greater than the next one (inversions), indicating a potential rotation point.
   - If there is more than one inversion, we conclude that the array cannot be sorted with a single rotation and return `false`.

2. **Handle Two Cases**:
   - **No Inversions**: The array is already sorted in non-decreasing order, so we return `true`.
   - **One Inversion**: We check two subarrays — one from the start of the array to the inversion point and another from the inversion point to the end. Both should be sorted individually. Additionally, the first element should be greater than or equal to the last element to complete a valid rotation.

## Complexity

The time complexity is **O(n)**, where `n` is the size of `nums`, as we make a single pass over the array for each check.

This approach ensures we handle different configurations of rotations and determine if the array meets the required conditions.
