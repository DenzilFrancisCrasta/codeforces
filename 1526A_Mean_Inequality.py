for _ in range(int(input())):
  n = int(input())

  a = list(map(int, input().split()))

  a = sorted(a)

  for i in range(1, 2*n-1, 2):
    a[i], a[i+1] = a[i+1], a[i] 

  print(*a)

