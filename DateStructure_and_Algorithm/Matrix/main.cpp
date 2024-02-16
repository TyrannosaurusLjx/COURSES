#include <iostream>
#include <vector>
#include "Matrix.h"
int main(){
    std::vector<std::vector<int>> Data1,Data2;
    Data1 = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    Data2 = {
        {2,4,5},
        {5,2,1},
        {5,3,1}
    };

    Matrix m1(3,3,Data1);
    Matrix m2(3,3,Data2);
    Matrix m3(3,3,{});
    m1.Print();
    m2.Print();
    m3.Print();
    Matrix m4 = m1.rightMul(m2);
    m4.Print();
    m4 = m4.kMul(8);
    m4.Print();





}