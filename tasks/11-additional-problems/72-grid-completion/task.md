# Grid Completion 

Your task is to create an ```n \times n``` grid whose each row and column has exactly one A and B. Some of the characters have already been placed. In how many ways can you complete the grid?
## Input
- The first input line has an integer ```n```: the size of the grid.
After this, there are ```n``` lines that describe the grid. Each line has ```n``` characters: . means an empty square, and A and B show the characters already placed.
You can assume that every row and column has at most one A and B.
## Output
- Print one integer: the number of ways modulo ```10^9+7```.
## Constraints

- ```2 \le n \le 500```

## Example
Input:
```
5
.....
..AB.
.....
B....
...A.
```

Output:
```
16
```
