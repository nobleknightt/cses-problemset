# Fixed-Length Paths I 

Given a tree of ```n``` nodes, your task is to count the number of distinct paths that consist of exactly ```k``` edges.
## Input
- The first input line contains two integers ```n``` and ```k```: the number of nodes and the path length. The nodes are numbered ```1,2,\ldots,n```.
Then there are ```n-1``` lines describing the edges. Each line contains two integers ```a``` and ```b```: there is an edge between nodes ```a``` and ```b```.
## Output
- Print one integer: the number of paths.
## Constraints

- ```1 \le k \le n \le 2 \cdot 10^5```
- ```1 \le a,b \le n```

## Example
Input:
```
5 2
1 2
2 3
3 4
3 5
```

Output:
```
4
```
