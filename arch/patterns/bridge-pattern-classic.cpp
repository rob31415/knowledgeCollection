// g++ -std=c++14 classic.cpp && ./a.out

#include <iostream>

using namespace std;

struct Impl
{
  virtual void opA() = 0;
  virtual void opB() = 0;
  virtual void opC() = 0;
};


struct ImplA : public Impl
{
  void opA()
  {
    cout << "ImplA opA" << endl;
  }
  
  void opB()
  {
    cout << "ImplA opB" << endl;
  }
  
  void opC()
  {
    cout << "ImplA opC" << endl;
  }
};


struct ImplB : public Impl
{
  void opA()
  {
    cout << "ImplB opA" << endl;
  }
  
  void opB()
  {
    cout << "ImplB opB" << endl;
  }
  
  void opC()
  {
    cout << "ImplB opC" << endl;
  }
};


struct I
{
  Impl *body;
  
  I() : body(new ImplB()) {  }
  
  ~I()
  {
    delete body;
  }

  void opY()
  {
    body->opA();
  }

  void opZ()
  {
    body->opB();
    body->opC();
  }
};


int main()
{
  I i = I();
  
  i.opZ();  
  
	return 0;
}
