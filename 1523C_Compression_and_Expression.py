for _ in range(int(input())):
  stack = []
  n = int(input())
  a = [int(input()) for _ in range(n)]

  stack.append(a[0])
  print(stack[-1])

  for x in a[1:]:
    if x == stack[-1]:
      if x == 1:
        stack.append(1)
        print(*stack, sep='.')
      else:
        while len(stack) > 0 :
          if stack.pop() == x-1:
            stack.append(x)
            print(*stack, sep='.')
            break

    elif x > stack[-1]:
      if x == stack[-1] + 1:
        stack[-1] = x
        print(*stack, sep='.')
      else:
        while len(stack) > 0 :
          if stack.pop() == x-1:
            stack.append(x)
            print(*stack, sep='.')
            break
    else:
      if x == 1:
        stack.append(1)
        print(*stack, sep='.')
      else:
        while len(stack) > 0 :
          if stack.pop() == x-1:
            stack.append(x)
            print(*stack, sep='.')
            break
