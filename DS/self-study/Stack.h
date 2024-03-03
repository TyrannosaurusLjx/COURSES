#include <cwchar>
#include <iterator>
#include <stdexcept>
#include<iostream>
#include <valarray>
template<typename Comparable>
// 使用链式结构实现
class Stack{
    
  public:
    Stack(){
        tail = new Node(0);
        top = tail;
    };
    ~Stack(){
        while(top!=tail){
            Node* temp = top;
            top = top->next;
            delete temp;
        }        
    };

    bool Empty(){
        return tail->value == 0;
    }

    void MakeEmpty(){
        while( !Empty() ){
            Node* temp = top;
            top = top->next;
            tail->value--;
            delete temp;
        }
    }

    void Push(Comparable item){
        Node* new_node = new Node(item);
        new_node->next = top;
        top = new_node;
        tail->value++;
    }

    Comparable Pop(){
        if(Empty()){
            throw std::out_of_range("index out of range!");
        }else{
            Node* temp = top;
            top = top->next;
            tail->value--;
            return temp->value;
        }
    }


    void Print(){
        Node* temp = top;
        while(temp != tail){
            std::cout<<temp->value<<std::endl;
            temp = temp->next;
        }
    }

    Comparable Top(){
        if( !Empty() ){
            return top->value;
        }else{
            throw std::out_of_range("the stack is empty!");
        }
    }

  private:
    struct Node{
        Comparable value;
        Node *next;

        Node(Comparable item): value(item), next( nullptr ){};
    };
    Node* top;
    Node* tail;
};
