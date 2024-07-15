# Given an array nums of size n, return the majority element. The majority 
# element is the element that appears more than [n/2] times. You may assume 
# that the majority element always exists in the arrays.

# Input:

# 3 2 3

# Output:

# 3

def majority(arr):
  for i in set(arr):
    if arr.count(i)> (len(arr)//2):
      return i

arr = list(map(int,input().split()))
print(majority(arr))
