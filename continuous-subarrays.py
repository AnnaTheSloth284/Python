# Given an unsorted array of integers, find the number of continuous 
# subarrays having sum exactly equal to the given number.

def sum_of_subarray(arr,k):
  occ = dict()
  sum_ = 0
  res = 0
  for i in arr:
    sum_ += i
    if sum_ == k:
      res += 1

    if sum_ in occ:
      occ[sum_] += 1

    else:
      occ[sum_] = 1

    if (sum_ - k) in occ:
      res += occ[sum_ - k]
    print(res,occ)

    return res
