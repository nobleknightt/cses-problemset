# Substring Order II 

You are given a string of length ```n```. If all of its substrings (not necessarily distinct) are ordered lexicographically, what is the ```k```th smallest of them?
## Input
- The first input line has a string of length ```n``` that consists of characters a–z.
The second input line has an integer ```k```.
## Output
- Print the ```k```th smallest substring in lexicographical order.
## Constraints

- ```1 \le n \le 10^5```
- ```1 \le k \le \frac{n(n+1)}{2}```

## Example
Input:
```
baabaa
10
```

Output:
```
ab
```

Explanation: The 10 smallest substrings in order are a, a, a, a, aa, aa, aab, aaba, aabaa, and ab.
