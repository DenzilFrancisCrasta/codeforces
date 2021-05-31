def operations(i, j):
  print(1, i, j)
  print(2, i, j)
  print(2, i, j)
  print(1, i, j)
  print(2, i, j)
  print(2, i, j)

for _ in range(int(input())):
  n = int(input())
  a = input()

  print(n//2 * 6)

  for i in range(1,n,2):
    j = i+1
    for _ in range(2):
      print(1, i, j)
      print(2, i, j)
      print(2, i, j)

