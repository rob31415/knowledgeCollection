// g++ partialApplication.cpp -std=c++11


/*
a fct X takes a callback C and calls it.
C itself takes a callback D and calls that.
Caveat: D isn't supposed to be given to C via X.

*/

#include <iostream>
#include <functional>

using namespace std;

typedef function<void ()> D;
typedef function<bool (int, D)> C;


void d()
{
	cout << "D" << endl;
}


bool c(int a, D d)
{
	d();
	return a<5;
}


void X(function<bool (int)> callback, int a)
{
	if(callback(a))
	{
		cout << "X yes" << endl;
	}
	else
	{
		cout << "X no" << endl;
	}
}


int main()
{
	function<bool (int)> p = std::bind(c, placeholders::_1, d);
	X(p, 1);
	X(p, 10);
	return 0;
}
