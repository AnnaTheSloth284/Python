# Given three coordinate points A,B and C, find the missing point D
# such that ABCD can be a parallelogram. If there are multiple such 
# points, find the lexicographically smallest coordinate

# Input:

# 3 2

# 3 4

# 2 2

# Output:

# 2 0

def lexismall(A,B,C):
  x1 = A[0] + B[0] - C[0]
  x2 = C[0] + A[0] - B[0]
  x3 = B[0] + C[0] - A[0]

  y1 = A[1] + B[1] - C[1]
  y2 = C[1] + A[1] - B[1]
  y3 = B[1] + C[1] - A[1]
  return min((x1,y1),(x2,y2),(x3,y3))

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
print(lexismall(A,B,C))
