# Sorting Methods 

Here are some possible methods using which we can sort the elements of an array in increasing order:

- At each step, choose two adjacent elements and swap them.
- At each step, choose any two elements and swap them.
- At each step, choose any element and move it to another position.
- At each step, choose any element and move it to the front of the array.

Given a permutation of numbers ```1,2,\ldots,n```, calculate the minimum number of steps to sort the array using the above methods.
## Input
- The first input line contains an integer ```n```.
The second line contains ```n``` integers describing the permutation.
## Output
- Print four numbers: the minimum number of steps using each method.
## Constraints

- ```1 \le n \le 2 \cdot 10^5```

## Example
Input:
```
8
7 8 2 6 5 1 3 4
```

Output:
```
20 6 5 6
```
