#include <algorithm>
#include <ios>
#include <iostream>
#include <stdexcept>
#include <strings.h>
#include <system_error>
// 带头结点的单链表，头借点存储链表的长度
template<typename Comparable>
class SingleList{
  public:
    
    struct Node{
        Comparable value;
        Node *next;

        Node(Comparable item): value( item ), next( NULL ) {};
    };
    Node *head;

    // construct function
    SingleList(): head( new Node(0) )  {};

    // isempty?
    bool Empty(){
        return head->value == 0 ;
    }

    // get length
    int Length(){
        return head->value;
    }

    //get value of position 'index'
    Comparable GetValue(int index){
        if( Empty() ){ throw std::runtime_error("the list is empty!"); }
        else if( index < 0 || index >= head->value ){
            throw std::out_of_range("index out of range!");
        }else{
            Node* temp = GetElem( index );
            return temp->value;
        }
    }      

    //get index of value == "value"
    int GetIndex(Comparable value){
        Node* temp = head;
        if( Empty() ){ throw std::runtime_error("the list is empty"); }else{
            for(int i = 0; i < head->value; i++){
                temp = temp->next;
                if( temp->value == value ){
                    return i;
                }
            }
            return -1;
        }
    }

    // insert method
    void Insert(int index, Comparable value){
        if(index < 0 || index > head->value){// index == head->value equals indert at the last 
            throw std::out_of_range("index out of range!");
        }else{
            Node* temp = head;
            Node* new_node =new Node(value);
            for(int i = 0; i < index; i++){
                temp = temp->next;
            } 
            new_node->next = temp->next;
            temp->next = new_node;
            head->value++;
        }
    }
    
    //remove method
    void Remove(int index){
        if(index < 0 || index >= head->value){
            throw std::out_of_range("index out of range!");
        }else{
            IRemove(index);
        }
    }    

    // print list
    void Print(){
        if( head->value == 0 ){
            std::cout<<"empty single list"<<std::endl;
        }else{
            Node* temp = head;
            for(int i=0; i < head->value; i++){
                temp = temp->next;
                std::cout<<temp->value<<std::endl;
            }
        }
    }

    //push 
    void Push(Comparable item){
        Insert(head->value, item);
    }



  private:
    // get the pointer of index 'index'
    Node* GetElem(int index){
        Node* temp = head;
        for(int i = 0; i <= index; i++){
            temp = temp->next;
        }
        return temp;
    }

    // get the pointer of value == "value"
    Node* LocateElem(Comparable value){
        Node* temp = head;
        for(int i = 0; i < head->value; i++){
            temp = temp->next;
            if( temp->value == value ){
                return temp;
            }
        }
        return nullptr;
    }          

    //remove
    void IRemove(int index){
        Node* temp = head;
        for(int i = 0; i<index; i++){
            temp = temp->next;
        }
        Node* p = temp->next;
        temp->next = p->next;
        delete p;
        head->value--;
    }
};



