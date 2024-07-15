# Given an array arr[] containing N integers. In one step, any element of the array
# can either be increased or decreased by one. Find minimum steps required such
# that the product of the array elements becomes 1.

# Input:

# -2 4 0 0 0

# 5

# Output:

# 7

def minStep(arr,N):
  zero,product,steps = 0,1,0

  for i in arr:
    if i<0:
      steps+=(abs(i)-1)
      product *= -1

    elif i == 0:
      zero += 1

    else:
      steps+=(i-1)
      product *= 1

  if product==1 or (product==-1 and zero>0):
    steps += zero

  elif product == -1:
    steps += 2

  return steps

arr = list(map(int,input().split()))
N = int(input())
print(minStep(arr,N))
