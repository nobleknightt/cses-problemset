# Dynamic Range Sum Queries 

Given an array of ```n``` integers, your task is to process ```q``` queries of the following types:

- update the value at position ```k``` to ```u```
- what is the sum of values in range ```[a,b]```?

## Input
- The first input line has two integers ```n``` and ```q```: the number of values and queries.
The second line has ```n``` integers ```x_1,x_2,\dots,x_n```: the array values.
Finally, there are ```q``` lines describing the queries. Each line has three integers: either "```1``` ```k``` ```u```" or "```2``` ```a``` ```b```".
## Output
- Print the result of each query of type 2.
## Constraints

- ```1 \le n,q \le 2 \cdot 10^5```
- ```1 \le x_i, u \le 10^9```
- ```1 \le k \le n```
- ```1 \le a \le b \le n```

## Example
Input:
```
8 4
3 2 4 5 1 1 5 3
2 1 4
2 5 6
1 3 1
2 1 4
```

Output:
```
14
2
11
```
