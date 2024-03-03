#include<iostream>
#include <stdexcept>
#include <strings.h>
template<typename Comparable>
class DoubleList{
  public: 

    DoubleList(): head( new Node(0) ){};
    
    ~DoubleList(){};

    //Empty method
    bool Empty(){
        return head->value == 0;
    }
    
    // indert item to position index
    // 不允许在末尾 insert
    void Insert(int index, Comparable item){
        if(index < 0 || index >= head->value){
            throw std::out_of_range("index out of range!");
        }else {
            Node* temp = head;
            for(int i = 0; i < index; i++){
                temp = temp->next;
            }
            Node* new_node = new Node(item);
            new_node->next = temp->next;
            temp->next->prior = new_node;
            temp->next = new_node;
            new_node->prior = temp;
            head->value ++;
        }
    }

    int GetIndex(Comparable item){
        Node *temp = head->next;
        int index = 0;
        while(temp != nullptr){
            if(temp->value != item){
                temp = temp->next;
                index++;
            }else{
                return index;
            }
        }
        return -1;
    }

    void Print(){
        if(Empty()){
            std::cout<<"the list is empty!"<<std::endl;
        }else{
            Node* temp = head->next;
            while(temp->next != nullptr){
                std::cout<<temp->value<<std::endl;
                temp = temp->next;
            }
            std::cout<<temp->value<<std::endl;//容易写成temp->next
        }
    }

   void Push(Comparable item){
        Node *temp = head;
        while(temp->next != nullptr){
            temp = temp->next;
        }
        Node* new_node = new Node(item);
        temp->next = new_node;
        new_node->prior = temp;
        head->value++;
    } 

    void Remove(int index){
        if(index < 0 || index >= head->value){
            throw std::out_of_range("index out of range");
        }else{
            Node* temp = head;
            for(int i = 0; i <= index; i++){
                temp = temp->next;
            }
            temp->prior->next = temp->next;
            temp->next->prior = temp->prior;
            delete temp;
            head->value--;
        }
    }

  private:
    struct Node{
        Comparable value;
        Node* prior,* next;

        Node(Comparable item): value( item ), prior( nullptr ), next( nullptr ){};
    };

    Node* head;




};
