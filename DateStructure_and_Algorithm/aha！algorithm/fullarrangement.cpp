#include <iostream>
#include <vector>
using namespace std;

void dfs(int step, int n, vector<int>& book, vector<int>& a) {
    if (step == n + 1) {
        for (int index = 1; index <= n; index++) {
            cout << a[index] << " ";
        }
        cout << endl;
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (book[i] == 0) {
            a[step] = i;
            book[i] = 1;
            dfs(step + 1, n, book, a);
            book[i] = 0;
        }
    }
}

int main(void) {
    int n;
    cin >> n;
    vector<int> book(n + 1, 0);
    vector<int> a(n + 1, 0);
    dfs(1, n, book, a);
    return 0;
}
