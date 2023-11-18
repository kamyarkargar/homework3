#tree decision 
import random
list=[]
for i in range(1,11):
  x=(random.randint(1,100))
  print(x)
  list.append(x)
print(list)
def rec_rec(n):
  if n==[]:
    return 0
  else:
    return 1 +rec_rec(n[1:])

def quicksort(array):
  if len(array)<10:
    return array
  else:
    pivot=array[0]
    smaller,bigger=[],[]
    for ele in array[0:]:
      if ele <= pivot:
        smaller.append(ele)
      else:
        bigger.append(ele)
    return quicksort(smaller)+[pivot]+quicksort(bigger)
print(quicksort(list))
print(rec_rec(list))
#از چب به راست درخت را مي خواند
