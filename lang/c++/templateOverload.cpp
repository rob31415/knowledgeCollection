//g++ templateOverload.cpp

#include <iostream>

template<typename T>
int f(T) { return 1;}
// becomes f(int*)

template<typename T>
int f(T*) { return 2;}
// becomes f(int*)

int main()
{
  std::cout << f<int>((int*)0) << std::endl;

  // chooses 1st templ., because would for the second 
  // want to cast to <int**> which is not possible
  std::cout << f<int*>((int*)0) << std::endl;
}
