# Assume you area an awesome parent and want to give your child some cookies.
# But you should give each child at most one cookie.Each child i has agreed 
# factor g[i], which is the minimum size of a cookie that the child will be 
# content with and each cookie j has a size s[j]>=g[i], we can assign the cookie 
# j to the child i, and the child i will be content. Your goal is to maximize 
# the number of content and output the maximum number.

def cookie(gkids,ckies):
  stack = []
  for i in ckies:
    stack.append(i)
  count=0

  for i in gkids:
    if i in stack:
      count+=1
      stack.remove(i)
   #for j in stack:
   #   if j>=i:
   #     count+=1
   #     stack.remove(j)

  return count

gkids = list(map(int,input().split()))
ckies = list(map(int,input().split()))
print(cookie(gkids,ckies))
