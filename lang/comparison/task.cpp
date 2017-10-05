// g++ task.cpp -std=c++1y

#include <map>
#include <list>
#include <tuple>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

typedef tuple<float,string> Tuple;
typedef map<string, list<Tuple>> Input;

Input createDatastructure()
{
	Input retVal;

	auto l1 = list<Tuple>();
	l1.push_back(Tuple(2.3f, "f"));
	l1.push_back(Tuple(0.01f, "g"));
	l1.push_back(Tuple(0.3f, "h"));

	auto l2 = list<Tuple>();
	l2.push_back(Tuple(0.3001f, "i"));
	l2.push_back(Tuple(0.01f, "j"));
	l2.push_back(Tuple(9.3f, "kx"));

	auto l3 = list<Tuple>();
	l2.push_back(Tuple(1000.7f, "l"));
	l2.push_back(Tuple(9.3f, "m"));
	l2.push_back(Tuple(9.2999f, "n"));

	retVal["A"] = l1;
	retVal["B"] = l2;
	retVal["C"] = l3;

	return retVal;
}

typedef set<Tuple> Output;

int main()
{
	auto input = createDatastructure();
	Output output;

	transform(input.begin(), input.end(), std::inserter(output, output.begin()),
		[](const pair<string, list<Tuple>>&) {return Tuple(1.0f, "a");} );

	for(auto const &e : output) {
		cout << get<0>(e);
	}

	return 0;
}
