#include <iostream>
#include "BinaryTree.h"


    // Test program


// BinarySearchTree Test
void BinarySearchTreeTest()
{
    BinarySearchTree<int> t;
    int NUMS = 400000;
    const int GAP  =   3711;
    int i;


    for( i = GAP; i != 0; i = ( i + GAP ) % NUMS )
        t.insert( i );

    for( i = 1; i < NUMS; i+= 2 )
        t.remove( i );

    if( NUMS < 40 )
        t.printTree( );
    if( t.findMin( ) != 2 || t.findMax( ) != NUMS - 2 )
        std::cout << "FindMin or FindMax error!" << std::endl;

    for( i = 2; i < NUMS; i+=2 )
        if( !t.contains( i ) )
            std::cout << "Find error1.1 ! BinarySearchTree" << std::endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t.contains( i ) )
            std::cout << "Find error2.1! BinarySearchTree" << std::endl;
    }

    BinarySearchTree<int> t2;
    t2 = t;

    for( i = 2; i < NUMS; i+=2 )
        if( !t2.contains( i ) )
            std::cout << "Find error1.2 ! BinarySearchTree" << std::endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t2.contains( i ) )
            std::cout << "Find error2.2! BinarySearchTree" << std::endl;
    }
    std::cout << "test for BinarySearchTree finished" << std::endl;
    return;
};

// AvlTree Test
void AvlTreeTest()
{
    AvlTree<int> t;
    int NUMS = 200;//xiao yu 2000000
    const int GAP  =   37;
    int i;

    for( i = GAP; i != 0; i = ( i + GAP ) % NUMS )
        t.insert( i );
    t.remove( 0 );
    for( i = 1; i < NUMS; i += 2 )
        t.remove( i );

    if( NUMS < 40 )
        t.printTree( );
    if( t.findMin( ) != 2 || t.findMax( ) != NUMS - 2 )
        std::cout << "FindMin or FindMax error!" << std::endl;

    for( i = 2; i < NUMS; i += 2 )
        if( !t.contains( i ) )
            std::cout << "Find error1.1! AvlTree" << std::endl;

    for( i = 1; i < NUMS; i += 2 )
    {
        if( t.contains( i )  )
            std::cout << "Find error2.1! AvlTree" << std::endl;
    }

    std::cout << "test for AvlTree finished" << std::endl;
    return;
};

// RedBlackTree Test
void RedBlackTreeTest()
{
    const int NEG_INF = -9999;
    RedBlackTree<int> t{ NEG_INF };
    int NUMS = 400000;
    const int GAP  =   37;
    int i;

    for( i = GAP; i != 0; i = ( i + GAP ) % NUMS )
        t.insert( i );

    if( NUMS < 40 )
        t.printTree( );
    if( t.findMin( ) != 1 || t.findMax( ) != NUMS - 1 )
        std::cout << "FindMin or FindMax error!" << std::endl;

    for( i = 1; i < NUMS; ++i )
        if( !t.contains( i ) )
            std::cout << "Find error1.1! RedBlackTree" << std::endl;
    if( t.contains( 0 ) )
        std::cout << "Oops!" << std::endl;

    
    RedBlackTree<int> t2{ NEG_INF };
    t2 = t;

    for( i = 1; i < NUMS; ++i )
        if( !t2.contains( i ) )
            std::cout << "Find error1.2! RedBlackTree" << std::endl;
    if( t2.contains( 0 ) )
        std::cout << "Oops!" << std::endl;

    std::cout << "test for RedBlackTree finished" << std::endl;
    return;
};


// SplayTree Test
void SplayTreeTest()
{
    SplayTree<int> t;
    int NUMS = 30000;
    const int GAP  =   37;
    int i;

    for( i = GAP; i != 0; i = ( i + GAP ) % NUMS )
        t.insert( i );

    for( i = 1; i < NUMS; i+= 2 )
        t.remove( i );

    if( NUMS < 40 )
        t.printTree( );
    if( t.findMin( ) != 2 || t.findMax( ) != NUMS - 2 )
        std::cout << "FindMin or FindMax error!" << std::endl;

    for( i = 2; i < NUMS; i+=2 )
        if( !t.contains( i ) )
            std::cout << "Find error1.1! SplayTree" << std::endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t.contains( i ) )
            std::cout << "Find error2.2! SplayTree" << std::endl;
    }

    SplayTree<int> t2;
    t2 = t;

    for( i = 2; i < NUMS; i+=2 )
        if( !t2.contains( i ) )
            std::cout << "Find error1.2! SplayTree" << std::endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t2.contains( i ) )
            std::cout << "Find error2.2! SplayTree" << std::endl;
    }

    std::cout << "test for Splay finished" << std::endl;
    return;
};


// test program
int main()
{
    std::cout << "Checking... (no more output means success)" << std::endl;
    BinarySearchTreeTest();
    AvlTreeTest();
    RedBlackTreeTest();
    SplayTreeTest();
    std::cout << "All tests passed" << std::endl;
    return 0;
}

