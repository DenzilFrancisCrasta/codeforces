# group elements 

'''
Given array
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Group identity
[0, 1, 2, 3, 0, 1, 2, 3, 0]

With x % GROUP_SIZE (=3)
1 -> 1,  2 -> 2, 3 -> 0

with adjustment ((x % GROUP_SIZE) - 1) % GROUP_SIZE
'''

[((x % GROUP_SIZE) -1 ) % GROUP_SIZE for x in a]

