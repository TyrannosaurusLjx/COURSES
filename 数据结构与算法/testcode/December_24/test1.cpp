#include <algorithm>
#include<iostream>

#include"../dsexceptions.h"

template <typename Comparable>
class BinaryTree
{

  public:
    BinaryTree( ) : root{ nullptr }
    {
    }

    bool isEmpty( ) const
    {
        return root == nullptr;
    }

    /**
     * Print the tree contents in sorted order.
     */
    void printTree(  ) const
    {
        if( isEmpty( ) )
            std::cout << "Empty tree" << std::endl;
        else
            printTree( root );
    }

    /**
     * Make the tree logically empty.
     */
    void makeEmpty( )
    {

        makeEmpty( root );
    }

    /**
     * Destructor for the tree
     */
    ~BinaryTree( )
    {
        makeEmpty( );
    }


  protected:

    struct BinaryNode
    { 
        Comparable element;
        BinaryNode *left;
        BinaryNode *right;

        BinaryNode( const Comparable & theElement, BinaryNode *lt, BinaryNode *rt )
          : element{ theElement }, left{ lt }, right{ rt } { }
        
        BinaryNode( Comparable && theElement, BinaryNode *lt, BinaryNode *rt )
          : element{ std::move( theElement ) }, left{ lt }, right{ rt } { }
    };
    
    BinaryNode *root;   

    
   void makeEmpty( BinaryNode * & t )
    {
        if( t != nullptr )
        {
            makeEmpty( t->left );
            makeEmpty( t->right );
            delete t;
        }
        t = nullptr;
    }

    /**
     * Internal method to print a subtree rooted at t in sorted order.
     */
    void printTree( BinaryNode *t ) const
    {
        if( t != nullptr )
        {
            printTree( t->left );
            std::cout << t->element << std::endl;
            printTree( t->right );
        }
    }

    /**
     * Internal method to clone subtree.
     */
    BinaryNode * clone( BinaryNode *t ) const
    {
        if( t == nullptr )
            return nullptr;
        else
            return new BinaryNode{ t->element, clone( t->left ), clone( t->right ) };
    }
};

template <typename Comparable>
class BinarySearchTree: public BinaryTree<Comparable>
{

  public:
    using BinaryTree<Comparable>::makeEmpty;
    using BinaryTree<Comparable>::isEmpty;
    using BinaryTree<Comparable>::printTree;
    using typename BinaryTree<Comparable>::BinaryNode;


    BinarySearchTree( ) {this->root= nullptr ;}

    
        ~BinarySearchTree( )
    {
        makeEmpty( );
    }


    /**
     * Insert x into the tree; duplicates are ignored.
     */
    void insert( const Comparable & x )
    {
        insert( x, this->root );
    }
     
    /**
     * Insert x into the tree; duplicates are ignored.
     */
    void insert( Comparable && x )
    {
        insert( std::move( x ), this->root );
    }

protected:


    /**
     * Internal method to insert into a subtree.
     * x is the item to insert.
     * t is the node that roots the subtree.
     * Set the new root of the subtree.
     */
    void insert( const Comparable & x, BinaryNode * & t )
    {
        if( t == nullptr )
            t = new BinaryNode{ x, nullptr, nullptr };
        else if( x < t->element )
            insert( x, t->left );
        else if( t->element < x )
            insert( x, t->right );
        else
            ;  // Duplicate; do nothing
    }
    
    /**
     * Internal method to insert into a subtree.
     * x is the item to insert.
     * t is the node that roots the subtree.
     * Set the new root of the subtree.
     */
    void insert( Comparable && x, BinaryNode * & t )
    {
        if( t == nullptr )
            t = new BinaryNode{ std::move( x ), nullptr, nullptr };
        else if( x < t->element )
            insert( std::move( x ), t->left );
        else if( t->element < x )
            insert( std::move( x ), t->right );
        else
            ;  // Duplicate; do nothing
    }


};



int main(){
    BinarySearchTree<int> bst;
    bst.insert(2);
    bst.printTree();
    int a = 1;
    bst.insert(a);
    bst.printTree();
    return 0;

}