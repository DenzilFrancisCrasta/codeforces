import re

def dec2alpha(n):

    alpha = []    
    BASE = 26

    while n > BASE:

      rem = n % BASE
      n = n // BASE

      # adjust the alphabet digits because 0 is not part of the alphabet
      if rem == 0:
        rem = BASE
        n -= 1

      alpha.append(rem)
    alpha.append(n)
    
    # convert the char offsets to alphabet chars
    return ''.join([chr(ord('A') + c - 1 ) for c in reversed(alpha)])

for _ in range(int(input())):
  s = input()
  
  number_re = re.compile(r'R(\d+)C(\d+)')
  alpha_re = re.compile(r'([A-Z]+)(\d+)')

  match = number_re.fullmatch(s)
  
  if match:
    row = match.group(1)
    col = int(match.group(2))
    alpha = dec2alpha(col)
    print(alpha+row) 
  else:
    match = alpha_re.fullmatch(s)
    alpha = match.group(1)
    row = match.group(2)

    col = 0

    for i, c in enumerate(reversed(alpha)):
      col += (ord(c) - ord('A') + 1) * (26**i)

    print('R{}C{}'.format(row, col))



