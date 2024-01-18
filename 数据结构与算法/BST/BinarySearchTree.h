#ifndef BINARY_SEARCH_TREE_H
#define BINARY_SEARCH_TREE_H

#include <iostream>
#include "dsexceptions.h"
#include <algorithm>
using namespace std;       

/// BinarySearchTree class
///
/// CONSTRUCTION: zero parameter
///
/// ******************PUBLIC OPERATIONS*********************
/// void insert( x )       --> Insert x
/// void remove( x )       --> Remove x
/// bool contains( x )     --> Return true if x is present
/// Comparable findMin( )  --> Return smallest item
/// Comparable findMax( )  --> Return largest item
/// boolean isEmpty( )     --> Return true if empty; else false
/// void makeEmpty( )      --> Remove all items
/// void printTree( )      --> Print tree in sorted order
/// ******************ERRORS********************************
/// Throws UnderflowException as warranted
template <typename Comparable>
class BinarySearchTree
{
public:
    /** 
     * Default constructor. 
     * 
     */
    BinarySearchTree( ) : root{ nullptr } 
	{
	    /// C++ 11 以后的标准推崇用 {} 来初始化数据.  
	}

    /**
     * Copy constructor
     */   
    BinarySearchTree( const BinarySearchTree & rhs ) : root{ nullptr }
	{
	    /// 初始化时的 root{ nullptr } 似乎毫无意义?
	    root = clone( rhs.root );
	    /// 这里用 clone 完成指针指向的内容复制, 而不是仅仅复制了指针.
	}
    
    /**
     * Move constructor
     */
    BinarySearchTree( BinarySearchTree && rhs ) : root{ rhs.root }
	{
	    /// 比较和 copy 的区别, 这里外部参数传入 rhs 时, 如果外部参数
	    /// 是一个右值, 那么按照旧 C++ 规范, 复制不可避免. 现在提供了
	    /// 右值引用, 在参数传入时, 避免了复制. 而这里通过对 rhs.root
	    /// 的指针复制, 避免了整棵树的复制. 
	    rhs.root = nullptr;     
 	    /// 必须释放 rhs.root 的管理权限. 提问: 为何这里不需要先delete
	    /// ? this->root 接管了原本 rhs.root 的内存, 没有指向内容的复
	    /// 制. 数据仍然存放在原地址, 因此不可以 delete, 否则
	    /// this->root 下的树也会被删除.  而 rhs 在调用发生之后, 作为
	    /// 一个右值量, 从概念上, 只用一次, 不会再使用, 因此可以赋为
	    /// nullptr, 避免同一段内存出现两个入口.
	}
    
    /**
     * Destructor for the tree
     */
    ~BinarySearchTree( )
	{
	    makeEmpty( );
	}

    /**
     * Copy assignment
     */
    BinarySearchTree & operator=( const BinarySearchTree & rhs )
	{
	    BinarySearchTree copy = rhs;  
	    /// 正在声明时用 = 不是赋值, 而是自动调用 copy constructor.
	    /// 等价于 BinarySearchTree copy{ rhs };
	    /// 这里发生了数据复制.
	    std::swap( *this, copy );   
	    /// 指针交换, 这样 this 指向的是新产生的实例, 而 copy
	    /// 接管了原实例.
	    return *this;
	    /// 因为返回是一个引用, 因此这里没有发生数据复制. 随着函数结束,临
	    /// 时变量 copy 会销毁, 从而启动析构函数.  此时它指向的是赋值
	    /// 运算左边的老对象的内容, 在析构时, 这个内存会被释放. 再体会
	    /// 一下上面的 swap 的作用. 一个正常的函数, 除了参数调用时可能
	    /// 发生隐含的复制, 返回时也可能. 这些都可以通过合理的指针或引
	    /// 用避免, 但指针会使代码可读性下降, 接口变的臃肿. 而引用可以
	    /// 合理的避开这一点.
	}
        
    /**
     * Move assignment
     */
    BinarySearchTree & operator=( BinarySearchTree && rhs )
    	{
    	    std::swap( root, rhs.root );
    	    /// 通过交换, this->root 接管了原 rhs.root 指向的内存.
    	    return *this;
    	}
    
   
    /**
     * Find the smallest item in the tree.
     * Throw UnderflowException if empty.
     */
    const Comparable & findMin( ) const
	{
	    if( isEmpty( ) )
		throw UnderflowException{ };
	    return findMin( root )->element;
	}

    /**
     * Find the largest item in the tree.
     * Throw UnderflowException if empty.
     */
    const Comparable & findMax( ) const
	{
	    if( isEmpty( ) )
		throw UnderflowException{ };
	    return findMax( root )->element;
	}

    /**
     * Returns true if x is found in the tree.
     */
    bool contains( const Comparable & x ) const
	{
	    return contains( x, root );
	    /// 这不是递归, 和上面两个函数一样, 是调用内部的 private 函数
	    /// 来确保接口统一.
	}

    /**
     * Test if the tree is logically empty.
     * Return true if empty, false otherwise.
     */
    bool isEmpty( ) const
	{
	    return root == nullptr;
	    /// 短小精悍.
	}

    /**
     * Print the tree contents in sorted order.
     */
    void printTree( ostream & out = cout ) const
	{
	    /// 默认为标准输出, 也可以改.
	    if( isEmpty( ) )
		out << "Empty tree" << endl;
	    else
		printTree( root, out );
	    /// 仍然调用内部函数.
	}

    /**
     * Make the tree logically empty.
     */
    void makeEmpty( )
	{
	    makeEmpty( root );
	}

    /**
     * Insert x into the tree; duplicates are ignored.
     */
    void insert( const Comparable & x )
	{
	    insert( x, root );
	}
     
    /**
     * Insert x into the tree; duplicates are ignored.
     */
    void insert( Comparable && x )
	{
	    insert( std::move( x ), root );
	}
    
    /**
     * Remove x from the tree. Nothing is done if x is not found.
     */
    void remove( const Comparable & x )
	{
	    remove( x, root );
	}


private:
    struct BinaryNode
    {
        Comparable element;
        BinaryNode *left;
        BinaryNode *right;

        BinaryNode( const Comparable & theElement, BinaryNode *lt, BinaryNode *rt )
	    : element{ theElement }, left{ lt }, right{ rt } { }
        
        BinaryNode( Comparable && theElement, BinaryNode *lt, BinaryNode *rt )
	    : element{ std::move( theElement ) }, left{ lt }, right{ rt } { }
	/// 参考前面的注释, 自己理解一下上面两个构造的不同. 
    };

    BinaryNode *root;


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
	    /// 这里可以这么做的原因是 t 是一个指针引用参数. 也就是说, t
	    /// 是一个指针变量的引用. 这个分支被触发, 要么 t 就是 root, 而
	    /// root 是 nullptr, 也就是说这是一棵空树. 于是直接给它分配一
	    /// 个新结点；另一种情况是递归的终点. 也就是 t 是作为一个指针
	    /// 引用参数, 对之前某结点的左子树或右子树的根的引用. 比如, 实
	    /// 际发生的调用是 insert( x, t->left ), 这样进入调用后, 发现
	    /// t 是 nullptr, 于是把 t 赋成一个新结点. 这时对 t 的改动, 相
	    /// 当于对上一层 t->left 的一个别名的改动 (引用的原始定义), 于
	    /// 是相当于直接把上一层的 t->left 从 nullptr 改成了新结点. 因
	    /// 此合法且高效. 用这种技巧我们就不需要保留上一层的缓存了. 
	    else if( x < t->element )
		insert( x, t->left ); 	       
	    else if( t->element < x )
		insert( x, t->right );
	    else
		;  // Duplicate; do nothing
	    /// 书上这个 BST 约定元素无重复, 因此有重复就什么也不做. 
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
	    /// 和之前唯一的区别就是这里调用了不同的构造函数. 这里结点数据
	    /// 没有发生复制. 考虑一下这个 insert 的实际应用场合是什么?
	    else if( x < t->element )
		insert( std::move( x ), t->left );
	    else if( t->element < x )
		insert( std::move( x ), t->right );
	    else
		;  // Duplicate; do nothing
	}

    /**
     * Internal method to remove from a subtree.
     * x is the item to remove.
     * t is the node that roots the subtree.
     * Set the new root of the subtree.
     *
     * remove 只提供了一个接口的版本, 这个接口是常量左值引用, 它可以同
     * 时接受左右值引用, 但不能对被引用的内容作出修改. 
     */
    void remove( const Comparable & x, BinaryNode * & t )
	{
	    /// remove 是比较复杂的操作, 因为我们需要保持 BST 性质. 节后我
	    /// 们再讨论这个.

	    /// 这里为何不先 find 再 remove ?
	    if( t == nullptr )
		return;   // Item not found; do nothing
	    if( x < t->element )
		remove( x, t->left );
	    else if( t->element < x )
		remove( x, t->right );
	    else if( t->left != nullptr && t->right != nullptr ) // Two children
	    {
		t->element = findMin( t->right )->element;
		/// 这个元素必然是排在 x 下一位的元素, 且必存在.
		remove( t->element, t->right );
		/// 将右子树中的 t->element 删除.
	    }
	    else   /// 一个孩子, 孩子替代. 没有孩子, 等价于删除. 
	    {
		BinaryNode *oldNode = t;
		t = ( t->left != nullptr ) ? t->left : t->right;
		delete oldNode;
	    }
	}

    /**
     * Internal method to find the smallest item in a subtree t.
     * Return node containing the smallest item.
     */
    BinaryNode * findMin( BinaryNode *t ) const
	{
	    /// 这个函数用了递归.
	    if( t == nullptr )
		return nullptr;
	    if( t->left == nullptr )
		return t;
	    return findMin( t->left );
	}

    /**
     * Internal method to find the largest item in a subtree t.
     * Return node containing the largest item.
     */
    BinaryNode * findMax( BinaryNode *t ) const
	{
	    /// 而这个函数没有用递归. 
	    if( t != nullptr )
		while( t->right != nullptr )
		    t = t->right;
	    return t;
	}


    /**
     * Internal method to test if an item is in a subtree.
     * x is item to search for.
     * t is the node that roots the subtree.
     */
    bool contains( const Comparable & x, BinaryNode *t ) const
	{
	    /// contains 不如依附于 find ?
	    if( t == nullptr )
		return false;
	    else if( x < t->element )
		return contains( x, t->left );
	    else if( t->element < x )
		return contains( x, t->right );
	    else
		return true;    // Match
	}
/****** NONRECURSIVE VERSION*************************
	bool contains( const Comparable & x, BinaryNode *t ) const
	{
        while( t != nullptr )
	if( x < t->element )
	t = t->left;
	else if( t->element < x )
	t = t->right;
	else
	return true;    // Match

        return false;   // No match
	}
*****************************************************/

    /**
     * Internal method to make subtree empty.
     */
    void makeEmpty( BinaryNode * & t )
	{
	    if( t != nullptr )
	    {
		/// 为何这里是后续遍历?
		makeEmpty( t->left );
		makeEmpty( t->right );
		delete t;
	    }
	    t = nullptr;
	}

    /**
     * Internal method to print a subtree rooted at t in sorted order.
     *
     * 修改了输出的换行模式.
     */
    void printTree( BinaryNode *t, ostream & out ) const
	{
	    /// 为何这里是中序遍历? 
	    if( t != nullptr )
	    {
		printTree( t->left, out );
		out << t->element << "\t";
		printTree( t->right, out );
	    }
	    if (t == root)
		std::cout << std::endl;
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

#endif
