#include <algorithm>
#include<iostream>
#include"SinleList.h"
#include"DoubleList.h"

int main(){
    DoubleList<int> lst;
    std::cout<<lst.Empty()<<std::endl;
    for(int i = 0; i<=10; i++){
        lst.Push(i);
    }


    std::cout<<"is empty"<<lst.Empty()<<std::endl;
    lst.Print();
    
    std::cout<<"--------------"<<std::endl;

    for(int i = 0; i<=2; i++){
        lst.Remove(i);
    }
    lst.Print();
    
    std::cout<<lst.GetIndex(0)<<" "<<lst.GetIndex(10)<<" "<<lst.GetIndex(12)<<std::endl;

    return 0;
}

