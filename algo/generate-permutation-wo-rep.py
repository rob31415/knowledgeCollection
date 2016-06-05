#! /usr/bin/python3

# generate n-permutation without repetition

def permuteRecursively(a, b):
  if(not b):
    print(a)
  else:
    for i, element in enumerate(b):
      ithElementRemoved = b[:i] + b[i+1:]
      permuteRecursively(a + b[i], ithElementRemoved)

permuteRecursively("", "1234")

print("")

from collections import namedtuple
Element = namedtuple("Element", ["a", "b"])

def permuteIteratively(a, b):
  storage = [Element(a, b)]

  while(storage):
    el = storage.pop(0)
    if(el.b):
      for i, element in enumerate(el.b):
        ithElementRemoved = el.b[:i] + el.b[i+1:]
        storage.append(Element(el.a + el.b[i], ithElementRemoved))
    else:
      print(el.a)

permuteIteratively("", "1234")

