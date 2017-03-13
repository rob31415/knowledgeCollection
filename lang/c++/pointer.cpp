// g++ pointer.cpp -std=c++11

#include <iostream>
#include <memory>

using namespace std;

class X {};


void uniquePtrExample()
{
	std::unique_ptr<X> a_unique_pt(new X());	// non-assignable and non-copyable (but moveable). gets auto-deleted when leaving scope.
	//unique_ptr<X> another_unique_pt = a_unique_pt;		// compile error
	cout << ((a_unique_pt == nullptr) ? "true" : "false");		// false, of course
	unique_ptr<X> another_unique_pt = move(a_unique_pt);		// transfer ownership
	cout << ((a_unique_pt == nullptr) ? "true" : "false");		// true
	// "delete a_unique_pt;" not neccessary here, is auto deleted when exiting function
}


weak_ptr<X> sharedAndWeakPtrExample()
{
	shared_ptr<X> a_shared_pt(new X());		// is deleted when all (non-weak) references are out of scope
	cout << a_shared_pt.use_count();	// 1
	shared_ptr<X> another_shared_pt = a_shared_pt;	// refcount +1
	cout << a_shared_pt.use_count();	// 2
	shared_ptr<X> a_third_shared_pt = a_shared_pt; // refcount +1
	cout << a_shared_pt.use_count();	// 3

	weak_ptr<X> a_weak_pt = a_shared_pt;	// refcount +0
	cout << a_shared_pt.use_count();	// 3
	cout << a_weak_pt.use_count();	// 3
	return a_weak_pt;
}


int main()
{
	uniquePtrExample();

	weak_ptr<X> a_empty_weak_pt = sharedAndWeakPtrExample();
	cout << a_empty_weak_pt.use_count();		// 0

	return 0;
}
