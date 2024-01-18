#include <iostream>
#include <vector>
#include "BinarySearchTree.h"
using namespace std;

    // Test program
int main( )
{
    BinarySearchTree<int> t;

    vector<int> input {3, 1, 7, 2, 5, 9, 4};

    cout << "Before:\t";
    for (vector<int>::iterator it = input.begin();
	 it != input.end();
	 it++)
    {
	cout << *it << '\t';
	t.insert(*it);
    }
    cout << endl;
    cout << "After:\t";
    t.printTree();
    return 0;
}
