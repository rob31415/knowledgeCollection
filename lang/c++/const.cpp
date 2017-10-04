// g++ const.cpp

#include <iostream>

class A
{
public:
	A() : data(0) {}
	// compiler error, return value must be "int const*"
	//int* getData2() const {return &data;}
	int const* getData() {return &data;}
private:
	int data;
};

int main()
{
	A a;
	std::cout << *a.getData();
	// compiler error
	//*a.getData() = 1;
}
