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

    /**
     * Copy constructor
     */
    BinaryTree( const BinaryTree & rhs ) : root{ nullptr }
    {
        root = clone( rhs.root );
    }

    /**
     * Move constructor
     */
    BinaryTree( BinaryTree && rhs ) : root{ rhs.root }
    {
        rhs.root = nullptr;
    }
    

    /**
     * Copy assignment
     */
    BinaryTree & operator=( const BinaryTree & rhs )
    {
        BinaryTree copy = rhs;
        std::swap( *this, copy );
        return *this;
    }
        
    /**
     * Move assignment
     */
    BinaryTree & operator=( BinaryTree && rhs )
    {
        std::swap( root, rhs.root );       
        return *this;
    }
    
    /**
     * Test if the tree is logically empty.
     * Return true if empty, false otherwise.
     */
    virtual bool isEmpty( ) const
    {
        return root == nullptr;
    }

    /**
     * Print the tree contents in sorted order.
     */
    virtual void printTree(  ) const
    {
        if( isEmpty( ) )
            std::cout << "Empty tree" << std::endl;
        else
            printTree( root );
    }

    /**
     * Make the tree logically empty.
     */
    virtual void makeEmpty( )
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