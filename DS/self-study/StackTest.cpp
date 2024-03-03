#include<iostream>
#include"Stack.h"

int main(){
    Stack<int> S;

    std::cout<<"is empty? "<<S.Empty()<<std::endl;
    std::cout<<"-------"<<std::endl;
    for(int i = 1; i<=5; i++){
        S.Push(i);
    }
    std::cout<<"is empty ?"<<S.Empty()<<std::endl;
    S.Print();
    for(int i = 1 ;i <= 5 ;i++){
        std::cout<<S.Top()<<"  "<<S.Pop()<<std::endl;
    }
    S.MakeEmpty();
    std::cout<<"is empty?"<<S.Empty()<<std::endl;
    return 0;
}
