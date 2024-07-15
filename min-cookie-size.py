# Assume you area an awesome parent and want to give your child some cookies.
# But you should give each child at most one cookie.Each child i has agreed 
# factor g[i], which is the minimum size of a cookie that the child will be 
# content with and each cookie j has a size s[j]>=g[i], we can assign the cookie 
# j to the child i, and the child i will be content. Your goal is to maximize 
# the number of content and output the maximum number.

# Alt 1
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

#IDEAL SOLUTION 
# Least time complexity code of 2.
# Logic: if the smallest kid cant be satisfies with the smallest cookie available, 
# there is no use checking if the bigger kids following the smallest kid when both 
# greed factor list and cookie size list are ordered in ascending order are satisfied 
# or not.
def cookie(s,g):
  n,m,i,j = len(s),len(g),0,0
  s.sort()
  g.sort()
  while(i<n and j<m):
    if s[i]>=g[j]:
      j+=1
    i+=1
  return j

s = list(map(int,input().split()))
g = list(map(int,input().split()))
print(cookie(s,g))
