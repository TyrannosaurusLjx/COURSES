#include <iostream>
#include "BinarySearchTree.h"
using namespace std;

    // Test program
int main( )
{
    BinarySearchTree<int> t;
    int NUMS = 20;
    const int GAP  =   3711;
    int i;

    cout << "Checking... (no more output means success)" << endl;

    for( i = GAP; i != 0; i = ( i + GAP ) % NUMS )
        t.insert( i );

    for( i = 1; i < NUMS; i+= 2 )
        t.remove( i );

    if( NUMS < 40 )
        t.printTree( );
    if( t.findMin( ) != 2 || t.findMax( ) != std::max(NUMS - 2, GAP) )
        cout << "FindMin or FindMax error!" << endl;
    /// 这里原书有一个 bug. 

    for( i = 2; i < NUMS; i+=2 )
        if( !t.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t.contains( i ) )
            cout << "Find error2!" << endl;
    }

    BinarySearchTree<int> t2;
    t2 = t;

    for( i = 2; i < NUMS; i+=2 )
        if( !t2.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t2.contains( i ) )
            cout << "Find error2!" << endl;
    }

    BinarySearchTree<int> t3(t);
    /// 复制构造函数的测试．结束之后, t3 是一个新的类实体.

    for( i = 2; i < NUMS; i+=2 )
        if( !t3.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t3.contains( i ) )
            cout << "Find error2!" << endl;
    }

    BinarySearchTree<int> t4(std::move(t));
    /// 移动构造函数, 结束之后, t 的实质内容转移给 t4. t 已经没有实质
    /// 内容. 这里 move 的作用是把一个左值变成一个右值.
    for( i = 2; i < NUMS; i+=2 )
        if( !t4.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t4.contains( i ) )
            cout << "Find error2!" << endl;
    }

    t = t4;
    /// 这是一次复制赋值.
    for( i = 2; i < NUMS; i+=2 )
        if( !t.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t.contains( i ) )
            cout << "Find error2!" << endl;
    }
    
    t = std::move(t4);
    /// 这是一次移动赋值.
    for( i = 2; i < NUMS; i+=2 )
        if( !t.contains( i ) )
            cout << "Find error1!" << endl;

    for( i = 1; i < NUMS; i+=2 )
    {
        if( t.contains( i ) )
            cout << "Find error2!" << endl;
    }

    t.remove(std::move(i));
    t.remove(0 + 1);

    /// 问题: 这时 t4 还有意义么? 
    cout << "Finished testing" << endl;

    

    return 0;
}
