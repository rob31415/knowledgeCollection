#! /usr/bin/python3


a = [8,5,3,7,2,9]


print(a)

for i in range(0,len(a)):
  minIdx = i
  for j in range(i+1,len(a)):
    if(a[j] < a[minIdx]):
      minIdx = j
  if(minIdx != i):
    tmp = a[i]
    a[i] = a[minIdx]
    a[minIdx] = tmp
    print(a)


print(a)

