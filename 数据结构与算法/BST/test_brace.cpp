#include <iostream>
#include <string>
#include <algorithm>

struct Student
{
	std::string name;
	int age;
};

class Chicken
{
public:
	int age;
	std::string name;
///	Chicken() {};
/// 如果增加这个缺省构造接口, 那么默认的构造就会失效;
///	Chicken (int _a, std::string _n) : age {_a}, name {_n} {};
/// 而这个可以看作是显式的大花括号初始化.
};

int main(int argc, char* argv[])
{
	int i {-1};
	std::string name {"Zhang San"};

	Student cai {"Kunkun", 24};
///	Student cai {24, "Kunkun"};
///     必须和声明一致对齐，反过来就是个语法错误. 	
	Chicken zhiyin {3, "Black Feet"};
	/// 实际上这样的初始化意义不大， 也不推荐. 接口应该严格掌握在设计者手里
	
	std::cout << "i = " << i << std::endl;
	std::cout << "name = " << name << std::endl;
	std::cout << "cai:"
			  << "name = " << cai.name
			  << "\tage = " << cai.age << std::endl;
	std::cout << "zhiyin:"
			  << "name = " << zhiyin.name
			  << "\tage = " << zhiyin.age << std::endl;
	return 0;
};
