n = int(input())
gauss = n * (n + 1) // 2
amount = sum(map(int, input().split()))
print(gauss - amount + 1)
