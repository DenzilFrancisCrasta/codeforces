for _ in range(int(input())):
  
  n, m = map(int, input().split())
  s = input()

  left = [m+1]*n
  right = [m+1]*n

  current = -1 * (m + n + 2)
  for i in range(n):
    if s[i] == '0':
      left[i] = min(left[i], i - current) 
    else:
      current = i


  current = m+ n + 2
  for i in reversed(range(n)):
    if s[i] == '0':
      right[i] = min(right[i], current-i) 
    else:
      current = i

  output = list(s)

  for i in range(n):
    if s[i] == '0' and 
        (left[i] <=m or right[i] <= m) 
        and left[i] != right[i]:
      output[i] = '1' 

  print(*output,sep='')
