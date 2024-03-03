#include <cwchar>
#include<iostream>
#include <iterator>
#include <stdexcept>
template<typename Comparable>
//链式存储实现,带头节点,头节点存储队列长度
class Queue{
  public:
    Queue(){
        front = new Node(0);
        rear = front;
    }
    ~Queue(){
        while(front->next != rear){
            Node* temp = front;
            front = front->next;
            delete temp;
        }
    }



    // is empty
    bool Empty(){
        return rear == front;
    }

    void Print(){
        Node* temp = front->next;
        while(temp != nullptr){
            std::cout<<temp->value<<std::endl;
            temp = temp->next;
        }
    }

    void EnQueue(Comparable item){
        Node* new_node = new Node(item);
        rear->next = new_node;
        rear = new_node;
        front->value++;
    }

    Comparable DeQueue(){
        if(Empty()){
            throw std::out_of_range("the quque is empty!");
        }else if( front->value == 1 ){
            Node* temp = rear;
            rear = nullptr;
            front->next = rear;
            front->value --;
            return temp->value;
        }else{
            Node* temp = front->next;
            front->next = temp->next;
            front->value--;
            return temp->value;
        }
    }

    Comparable Front(){
        if(Empty()){
            throw std::out_of_range("index out of range!");
        }else{
            return front->next->value;
        }
    }

  private:
    struct Node{
        Comparable value;
        Node* next;

        Node(Comparable item): value(item), next(nullptr){};
        ~Node(){};
    };
    Node* front,* rear;
};
