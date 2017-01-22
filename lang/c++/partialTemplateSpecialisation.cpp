// g++ partialTemplateSpecialisation.cpp

#include <iostream>

// execute different operations, depending on type

template <typename T>
struct A
{
  void op() {std::cout << "any other type" << std::endl;}
};

template <>
struct A<bool>
{
  void op() {std::cout << "bool" << std::endl;}
};

int main()
{
  A<int> b;
  b.op();	// exec op for any other type than bool

  A<bool> a;
  a.op();	// exec op, specialised for bool  
}

// btw: the only diff between struct and class is:
// stuct default accessibility is public, class is private
