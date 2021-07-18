def flatten(list1):
    if len(list1)== 0:
      return list1
    if isinstance(list1[0],list):
      return flatten(list1[0]) + flatten(list1[1:])
    return list1[:1] + flatten(list1[1:])  

def reverse2(liste):
  rlist = []
  for x in liste:
    x.reverse()
    rlist.append(x)
  rlist.reverse()
  return rlist
  

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
print(reverse2([[1, 2], [3, 4], [5, 6, 7]]))




