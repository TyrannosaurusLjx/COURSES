#include <iostream>

template<typename T>
class fatherclass{
    public:
        fatherclass(){
            root = new node;
            root->left = 0;
            root->right = 11;
        };
        ~fatherclass(){
            delete root;
        };

        void print(){
            print(root);
        }

protected:
        struct node{
            T left;
            T right;
        };
        node *root;
        void print(node *root){
            std::cout<<root->left<<std::endl;
            std::cout<<root->right<<std::endl;
        }

};

template<typename T>  
class sonclass : public fatherclass<T> {  
public:  
    using fatherclass<T>::print;  
    using typename fatherclass<T>::node;  
  
    sonclass() {  
        this->root = new node; // 通过 this 指针访问基类的 root  
        this->root->left = 1;  
        this->root->right = 2;  
    }  
  
    ~sonclass() {  
        // 不需要手动删除 root，基类的析构函数会处理  
    }  
  
    void reprint() {  
        this->root->left = 10;  
        this->root->right = 20;  
        print(); // 调用基类的 print 函数  
    }  
};  



