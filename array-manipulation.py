# Starting with a 1-indexed array of zeros and a list of operations for 
# each operation add a value to each of the array element between two 
# given indices inclusive. Once all operations have been performed, return 
# the maximum value in the array

def arrManipulation(n,queries):
  arr = [0]*(n+1)
  for i in queries:
    a,b,k = i
    arr[a]+=k
    arr[b+1]-=k
    curr = 0
    maxVal = 0
    for i in arr:
      curr+=i
      maxVal = max(maxVal,curr)
  return maxVal

n=10
queries = [[1,5,3],[4,8,7],[6,9,1]]
print(arrManipulation(n,queries))
