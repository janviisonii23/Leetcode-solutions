# Fibonacci Sequence

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. The sequence begins as follows:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

In this sequence, each number represents the addition of the two numbers before it.

### Formula

The Fibonacci sequence follows this formula:

- (F(n) = F(n-1) + F(n-2))

* Where (F(0) = 0) and ( F(1) = 1)[base cases]

### Methods to Calculate Fibonacci Numbers

1. **Recursive Approach**

   - This method calculates each Fibonacci number by calling a function that repeatedly breaks down the problem into smaller parts until it reaches the base cases (0 or 1).
   - It has very simple code but becomes inefficient as \( n \) grows larger because it performs repeated calculations, leading to a time complexity that increases exponentially.

2. **Iterative Approach**
   - This approach uses a simple loop to calculate the Fibonacci sequence up to the desired number.
   - Instead of breaking down the problem recursively, it starts from the base cases and iteratively calculates each Fibonacci number by adding the previous two numbers.
   - It is the most efficient approach in terms of both time and memory, as it runs in linear time and only requires constant space.
