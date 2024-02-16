#include "finalBST.h"

template <typename Comparable>
class AvlTree: public BinarySearchTree<Comparable>
{
public:
    using BinarySearchTree<Comparable>::makeEmpty;
    using BinarySearchTree<Comparable>::isEmpty;
    using BinarySearchTree<Comparable>::printTree;
    using typename BinarySearchTree<Comparable>::BinaryNode;


    AvlTree( ) { root= nullptr ;}

    
        ~AvlTree( )
    {
        makeEmpty( );
    }


    // //重写printTree
    // /**
    //  * Print the tree contents in sorted order.
    //  */
    // void printTree( ) const
    // {
    //     if( isEmpty( ) )
    //         std::cout << "Empty tree" << std::endl;
    //     else
    //         printTree( root );
    // }



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
    struct AvlNode : public BinaryNode
    {
        int height;
        AvlNode *left;
        AvlNode *right;
        AvlNode( const Comparable & ele, AvlNode *lt, AvlNode *rt, int h = 0 )
            : BinaryNode{ ele, lt, rt }, height{ h } { }
        AvlNode( Comparable && ele, AvlNode *lt, AvlNode *rt, int h = 0 )
            : BinaryNode{ std::move( ele ), lt, rt }, height{ h } { }
    };

    AvlNode *root;

    /**
     * Return the height of node t or -1 if nullptr.
     */
    int height( AvlNode *t ) const
    {
        return t == nullptr ? -1 : t->height;
    }

    int max( int lhs, int rhs ) const
    {
        return lhs > rhs ? lhs : rhs;
    }



    /**
     * Internal method to insert into a subtree.
     * x is the item to insert.
     * t is the node that roots the subtree.
     * Set the new root of the subtree.
     */
    void insert( const Comparable & x, AvlNode * & t )
    {
        if( t == nullptr )
            t = new AvlNode{ x, nullptr, nullptr };
        else if( x < t->element )
            insert( x, t->left );
        else if( t->element < x )
            insert( x, t->right );
        
        balance( t );
    }

    /**
     * Internal method to insert into a subtree.
     * x is the item to insert.
     * t is the node that roots the subtree.
     * Set the new root of the subtree.
     */
    void insert( Comparable && x, AvlNode * & t )
    {
        if( t == nullptr )
            t = new AvlNode{ std::move( x ), nullptr, nullptr };
        else if( x < t->element )
            insert( std::move( x ), t->left );
        else if( t->element < x )
            insert( std::move( x ), t->right );
        
        balance( t );
    }

  
    static const int ALLOWED_IMBALANCE = 1;

    // Assume t is balanced or within one of being balanced
    void balance( AvlNode * & t )
    {
        if( t == nullptr )
            return;
        
        if( height( t->left ) - height( t->right ) > ALLOWED_IMBALANCE )
            if( height( t->left->left ) >= height( t->left->right ) )
                rotateWithLeftChild( t );
            else{
                doubleWithLeftChild( t );
            }
        else if( height( t->right ) - height( t->left ) > ALLOWED_IMBALANCE )
            if( height( t->right->right ) >= height( t->right->left ) )
                rotateWithRightChild( t );
            else{
                doubleWithRightChild( t );
            } 
        t->height = max( height( t->left ), height( t->right ) ) + 1;
    }
    


    /**
     * Rotate binary tree node with left child.
     * For AVL trees, this is a single rotation for case 1.
     * Update heights, then set new root.
     */
    void rotateWithLeftChild( AvlNode * & k2 )
    {
        AvlNode *k1 = k2->left;
        k2->left = k1->right;
        k1->right = k2;
        k2->height = max( height( k2->left ), height( k2->right ) ) + 1;
        k1->height = max( height( k1->left ), k2->height ) + 1;
        k2 = k1;
    }

    /**
     * Rotate binary tree node with right child.
     * For AVL trees, this is a single rotation for case 4.
     * Update heights, then set new root.
     */
    void rotateWithRightChild( AvlNode * & k1 )
    {
        AvlNode *k2 = k1->right;
        k1->right = k2->left;
        k2->left = k1;
        k1->height = max( height( k1->left ), height( k1->right ) ) + 1;
        k2->height = max( height( k2->right ), k1->height ) + 1;
        k1 = k2;
    }

    /**
     * Double rotate binary tree node: first left child.
     * with its right child; then node k3 with new left child.
     * For AVL trees, this is a double rotation for case 2.
     * Update heights, then set new root.
     */
    void doubleWithLeftChild( AvlNode * & k3 )
    {
        rotateWithRightChild( k3->left );
        rotateWithLeftChild( k3 );
    }

    /**
     * Double rotate binary tree node: first right child.
     * with its left child; then node k1 with new right child.
     * For AVL trees, this is a double rotation for case 3.
     * Update heights, then set new root.
     */
    void doubleWithRightChild( AvlNode * & k1 )
    {
        rotateWithLeftChild( k1->right );
        rotateWithRightChild( k1 );
    }








    // /**
    //  * Internal method to print a subtree rooted at t in sorted order.
    //  */
    // void printTree( AvlNode *t ) const
    // {
    //     if( t != nullptr )
    //     {
    //         printTree( t->left );
    //         std::cout << t->element << std::endl;
    //         printTree( t->right );
    //     }
    // }









};