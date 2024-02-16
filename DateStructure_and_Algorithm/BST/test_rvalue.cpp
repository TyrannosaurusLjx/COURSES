#include <iostream>
#include <string>

class Animal
{
private:
    double weight;
    std::string name;
public:
    /// 这里用了常量左值引用, 它也可以接受右值. 但接受后不能修改右值引
    /// 用内的值. 如果没有必要修改右值参数, 那么可以用常量左值引用统一
    /// 左右值引用. 实际上作为构造函数, 这么做是偷懒, 应该提供两种版本
    /// 的接口.
    Animal (const std::string &_s) : name {_s} {};
    /// 第二个 const 表示这个函数是静态的. 这样从逻辑上, 就不得返回有
    /// 修改可能的引用, 比如左值引用或者指针. 因此第一个 const 修饰是
    /// 必须的, 它表示返回的左值引用是一个常量引用.
    const std::string &getName () const
    {
	return name;
    }
};

class Student
{
private:
    int age;
    Animal pet;
public:
    Student (const int &_a, const Animal &_p) : age {_a}, pet {_p} {};
    void sing();
    void jump();
    void rap();
    void play();
};

void Student::sing()
{
    std::cout << pet.getName() << " you are beatiful!" << std::endl;
};

void Student::rap()
{
    std::cout << "This year, I'm 24 years old. I'm a student." << std::endl;
};

int main(int argc, char* argv[])
{
    Animal chicken {"Zhiyin"};
    Student kunkun {24, chicken};
    kunkun.rap();
    kunkun.sing();
    return 0;
};
