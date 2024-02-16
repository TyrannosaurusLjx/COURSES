#include "AvlTree.h"

int main(){

    int a,b,c,d;
    a=1; b=2; c=3; d=4;
    AvlTree<int> tree;
    tree.insert(a);
    tree.isEmpty();
    tree.insert(2);
    tree.printTree();

}