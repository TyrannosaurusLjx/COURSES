#include <iostream>
void toprint(int x);
bool isprime(int x);
int main() {
    for (int i = 2;i <= 28; i++){
        if(isprime(i) == true){
            toprint(i);
        }
    }

    return 0;
}
