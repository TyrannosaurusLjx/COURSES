#include"finalavltree.h"

#include <iostream>

int main(){

    int a,b,c,d;
    a = 1;
    b = 2;
    c = 3;
    d = 4;
    std::cout<<"测试bst树"<<std::endl;
    BinarySearchTree<int>bst;
    bst.printTree();
    std::cout<<"bool = "<<bst.isEmpty()<<std::endl;
    bst.insert(a);
    bst.insert(b);
    std::cout<<"bool = "<<bst.isEmpty()<<std::endl;
    bst.printTree();


    std::cout<<"测试avl树"<<std::endl;
    AvlTree<int>avl;
    avl.printTree();
    std::cout<<"bool = "<<avl.isEmpty()<<std::endl;
    avl.insert(a);
    avl.insert(b);
    std::cout<<"bool = "<<avl.isEmpty()<<std::endl;
    // avl.remove(2);
    avl.printTree();
    std::cout<<"max min"<<avl.findMax()<<avl.findMin()<<"contains"<<avl.contains(1)<<std::endl;
    avl.makeEmpty();
    avl.printTree();
    return 0;

}