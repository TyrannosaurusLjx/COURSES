#include <iostream>
using namespace std;

int power(int x, int n)
{
    if(n == 0){
        return 1;
    }
    if(n == 1){
        return x;
    }

    int m = n/2;
    int half = power(x,m);

    if(n&1 == 1){
        return half*half*x;
    }else{
        return half*half;
    }
}

int main(){
    int x, n,  result;
    cout<<"input 'x' and its power 'n'"<<endl;
    cin>> x >> n;
    result = power(x,n);
    cout<<"power"<<"("<<x<<","<<n<<")"<<"="<<result<<endl;
    return 0;
}


