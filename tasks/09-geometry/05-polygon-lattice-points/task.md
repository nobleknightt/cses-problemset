# Polygon Lattice Points 

Given a polygon, your task is to calculate the number of lattice points inside the polygon and on its boundary. A lattice point is a point whose coordinates are integers.
The polygon consists of ```n``` vertices ```(x_1,y_1),(x_2,y_2),\dots,(x_n,y_n)```. The vertices ```(x_i,y_i)``` and ```(x_{i+1},y_{i+1})``` are adjacent for ```i=1,2,\dots,n-1```, and the vertices ```(x_1,y_1)``` and ```(x_n,y_n)``` are also adjacent.
## Input
- The first input line has an integer ```n```: the number of vertices.
After this, there are ```n``` lines that describe the vertices. The ```i```th such line has two integers ```x_i``` and ```y_i```.
You may assume that the polygon is simple, i.e., it does not intersect itself.
## Output
- Print two integers: the number of lattice points inside the polygon and on its boundary.
## Constraints

- ```3 \le n \le 10^5```
- ```-10^9 \le x_i, y_i \le 10^9```

## Example
Input:
```
4
1 1
5 3
3 5
1 4
```

Output:
```
6 8
```
