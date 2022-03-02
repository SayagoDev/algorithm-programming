# CSES Problem Set <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [Introductory Problems](#introductory-problems)
  - [Weird Algorithm](#weird-algorithm)
  - [Missing Number](#missing-number)

## Introductory Problems

### Weird Algorithm

Consider an algorithm that takes as input a positive integer $`n`$. If $`n`$ is even, the algorithm divides it by two, and if $`n`$ is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until $`n`$ is one. For example, the sequence for $`n=3`$ is as follows:

```math
3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1
```

Your task is to simulate the execution of the algorithm for a given value of $n$.

**Input**

The only input line contains an integer $`n`$.

**Output**

Print a line that contains all values of $`n`$ during the algorithm.

**Constraints**

- $`1 \leq n \leq 10^6`$

**Example**

```text
Input:
3

Output:
3 10 5 16 8 4 2 1
```

**Code**

```python
n = int(input())
while n > 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n*3)+1
print(1)
```

**Complexity Analysis**

- **Time Complexity:** $`O(n).`$
- **Space Complexity:** $`O(1).`$

### Missing Number

You are given all numbers between $`1,2,…,n`$ except one. Your task is to find the missing number.

**Input**

The first input line contains an integer $`n`$.

The second line contains $`n−1`$ numbers. Each number is distinct and between $`1`$ and $`n`$ (inclusive).

**Output**

Print the missing number.

**Constraints**

- $`2 \leq n \leq 2 \cdot 10^5`$

**Example**

```text
Input:
5
2 3 1 5

Output:
4
```

**Code**

```python
n = int(input())
gauss = n * (n + 1) // 2
amount = sum(map(int, input().split()))
print(gauss - amount + 1)
```

**Complexity Analysis**

- **Time Complexity:**
- **Space Complexity:**
