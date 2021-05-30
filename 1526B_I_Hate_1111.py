from bisect import bisect_left

def solve(n, divisor):

  if divisor <= 1 or n < 11 or len(str(n)) == 2 and n % 11 != 0:
    return False

  if n % int('1'*divisor) == 0:
    return True

  if divisor == 2 :
    return n % 11 == 0

  return solve(n - int('1'*divisor), divisor) or solve(n, divisor-1) 


soln = [i for i in range(1, 1100) if solve(i, len(str(i))) == False]

for _ in range(int(input())):
  n = int(input())

  if n >= 1100:
    print('YES')
  else:
    i = bisect_left(soln, n)
    if i < len(soln):
      if soln[i] == n:
        print('NO')
      else:
        print('YES')
    else:
      print('YES')
