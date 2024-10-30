# Move Zeros to End

This function moves all zeros in an array to the end while maintaining the order of non-zero elements. The approach involves two main steps:

1. **Identify First Zero**: 
   - The function locates the position `j` of the first zero in the array. 
   - If no zero is found, the function returns the array as is.

2. **Swap Non-Zero Elements**: 
   - Starting from the position after `j`, the function iterates through the array.
   - For each non-zero element, it swaps the element with the position at `j`, then increments `j` to maintain order.

### Result
The modified array has all non-zero elements at the beginning, followed by zeros at the end. This two-pass approach ensures efficiency by minimizing unnecessary swaps.
