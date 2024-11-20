# Range Queries and Copies 

Your task is to maintain a list of arrays which initially has a single array. You have to process the following types of queries:

- Set the value ```a``` in array ```k``` to ```x```.
- Calculate the sum of values in range ```[a,b]``` in array ```k```.
- Create a copy of array ```k``` and add it to the end of the list.

## Input
- The first input line has two integers ```n``` and ```q```: the array size and the number of queries.
The next line has ```n``` integers ```t_1,t_2,\ldots,t_n```: the initial contents of the array.
Finally, there are ```q``` lines describing the queries. The format of each line is one of the following: "1 ```k``` ```a``` ```x```", "2 ```k``` ```a``` ```b```" or "3 ```k```".
## Output
- Print the answer to each sum query.
## Constraints

- ```1 \le n, q \le 2 \cdot 10^5```
- ```1 \le t_i, x \le 10^9```
- ```1 \le a \le b \le n```

## Example
Input:
```
5 6
2 3 1 2 5
3 1
2 1 1 5
2 2 1 5
1 2 2 5
2 1 1 5
2 2 1 5
```

Output:
```
13
13
13
15
```
