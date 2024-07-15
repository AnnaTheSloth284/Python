def check(inp):
  stack = []
  for i in inp:
    if i in ('(','{','['):
      stack.append(i)

    else:
      if i==')' and stack.pop()!='(':
        return False
      elif i=='}' and stack.pop()!='{':
        return False
      elif i==']' and stack.pop()!='[':
        return False
  if stack==[]:
    return True
  else:
    return False

inp = input()
print(check(inp))
