# Permutation Inversions 

Your task is to count the number of permutations of ```1,2,\dots,n``` that have exactly ```k``` inversions (i.e., pairs of elements in the wrong order).
For example, when ```n=4``` and ```k=3```, there are ```6``` such permutations:

- ```[1,4,3,2]```
- ```[2,3,4,1]```
- ```[2,4,1,3]```
- ```[3,1,4,2]```
- ```[3,2,1,4]```
- ```[4,1,2,3]```

## Input
- The only input line has two integers ```n``` and ```k```.
## Output
- Print the answer modulo ```10^9+7```.
## Constraints

- ```1 \le n \le 500```
- ```0 \le k \le \frac{n(n-1)}{2}```

## Example
Input:
```
4 3
```

Output:
```
6
```
