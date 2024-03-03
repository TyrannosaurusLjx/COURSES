#include<iostream>

int main(){
    int array1[5];//测试 数组是可以不连续存储的
    array1[1] = 2;
    array1[4] = 5;
    for(int i = 0; i<5; i++){
        std::cout<<"array index "<<i<<" is "<<array1[i]<<std::endl;
    }
    return 0;
}
