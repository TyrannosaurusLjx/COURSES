#include <iostream>
#include <stack>
#include <string>
#include <cstdlib>

bool isValid(const std::string& s);

bool isValid(const std::string& s){
    std::stack<char> mystack;
    for(int i = 0; i< s.size();i++){
        if (s[i] == '(' || s[i] == '{' || s[i] == '['){
            mystack.push(s[i]);
        }else if (s[i] == ')' || s[i] == '}' || s[i] == ']'){
            if(s[i] == ')' && mystack.top() != '('){
            return false;
            }else if(s[i] == ']' && mystack.top() != '['){
            return false;
            }else if(s[i] == '}' && mystack.top() != '{'){
            return false;
            }else if (mystack.empty()){
            return false;
            }
            mystack.pop();
        }

    }
    return mystack.empty();
}

int main(){
    std::char s1 = "{}}{[[))";
    std::char s2 = "{{[()]}}";
    std::cout<<isValid(s1)<<isValid(s2)<<std::endl;
    return 0;
}
