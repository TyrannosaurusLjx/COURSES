#include <algorithm>
#include<iostream>
#include"Queue.h"

int main(){
    Queue<int> Q;
    std::cout<<"is empty? "<<Q.Empty()<<std::endl;
    std::cout<<"-------------"<<std::endl;
    for(int i = 1;i <=9; i++){
        Q.EnQueue(i);
    }
    Q.Print();

    std::cout<<"-------------"<<std::endl;
    for(int j = 0; j<= 3; j++){
        std::cout<<Q.DeQueue()<<std::endl;
    }
    std::cout<<"now front is "<<Q.Front()<<std::endl; 
    return 0;
}
