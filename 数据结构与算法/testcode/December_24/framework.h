template <typename Comparable>
class BinaryTree
{  

};

template <typename Comparable>
class BinarySearchTree: public BinaryTree<Comparable>
{

};

template <typename Comparable>
class AvlTree: public BinarySearchTree<Comparable>
{

};

template <typename Comparable>
class RedBlackTree: public BinarySearchTree<Comparable>
{

};

template <typename Comparable>
class SplayTree: public BinarySearchTree<Comparable>
{

};


