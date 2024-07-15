# Given n non negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it 
# is able to trap after raining.

def elevate(arr):
  maxi, water = arr[0], 0
  for i in range(1,len(arr)):
    if arr[i]>maxi:
      maxi = arr[i]
    else:
      water = water + (maxi - arr[i])
      print(arr[i],"->",water)
  if arr.index(maxi)!=len(arr)-1:
    for i in range(len(arr)-1, arr.index(maxi)+1n):
      water = water - (maxi - arr[i])
      print(i,"->",water)
  return water

arr = list(map(int,input().split()))
print(elevate(arr))
