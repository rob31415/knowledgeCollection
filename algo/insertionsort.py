#! /usr/bin/python3


a = [8,5,3,7,2,9]


print(a)

for i in range(1,len(a)):
  j = i
  while(j>0 and a[j]<a[j-1]):
    tmp = a[j]
    a[j] = a[j-1]
    a[j-1] = tmp
    print(a)
    j -= 1
    
print(a)

