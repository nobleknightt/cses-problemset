# Bit Substrings 

You are given a bit string of length ```n```. Your task is to calculate for each ```k``` between ```0  \ldots n``` the number of non-empty substrings that contain exactly ```k``` ones.
For example, if the string is 101, there are:

- 1 substring that contains 0 ones: 0
- 4 substrings that contain 1 one: 01, 1, 1, 10
- 1 substring that contains 2 ones: 101
- 0 substrings that contain 3 ones

## Input
- The only input line contains a binary string of length ```n```.
## Output
- Print ```n+1``` values as specified above.
## Constraints

- ```1 \le n \le 2 \cdot 10^5```

## Example
Input:
```
101
```

Output:
```
1 4 1 0
```
