#include <iostream>
#include <stack>
#include <queue>
#include <string>
#include <cctype>
#include "stringPreproce.h"
#include "calculator.h"

/**
 * @brief 操作符优先级判断函数
 *
 * 根据操作符的最后一个字符，判断操作符的优先级。
 *
 * @param op 要判断优先级的操作符
 * @return 操作符的优先级，+和-返回1，*和/返回2，括号返回3，其他返回0
 */
int op_Priority(std::string op){
    op = op[op.length()-1];
    if(op == "+" || op == "-"){
        return 1;
    }else if(op == "*" || op == "/"){
        return 2;
    }else if(op == "(" || op == ")"){
        return 3;
    }else{
        return 0;
    }
}

/**
 * @brief 统计字符串中小数点的个数
 *
 * 统计字符串中小数点的个数。
 *
 * @param str 输入的字符串
 * @return 字符串中小数点的个数
 */
int countDots(const std::string& str) {  
    int count = 0;  
    for (char c : str) {  
        if (c == '.') {  
            count++;  
        }  
    }  
    return count;  
}

int main(int argc, char* argv[]){
    double value = 0; // 表达式的值
    std::queue<std::string> Postfix; // 后缀表达式队列
    std::queue<std::string> infixQueue; // 中缀表达式队列
    std::stack<std::string> opStack;
    infixQueue = strToQueue(strPreproce(argv[1]));

    std::string item;
    while (!infixQueue.empty()){
        item = infixQueue.front();
        if(countDots(item) > 1){
            err_exp();
        }
        if(isnum(item)){
            Postfix.push(item);
        }else if(item == "("){
            opStack.push(item);
        }else if(item == ")"){
            while (opStack.top() != "("){
                Postfix.push(opStack.top());
                opStack.pop();
            }
            // pop (
            opStack.pop();
        }else{
            while(!opStack.empty() && (op_Priority(opStack.top()) >= op_Priority(item)) && opStack.top() != "("){
                Postfix.push(opStack.top());
                opStack.pop();
            }
            opStack.push(item);
        }
        // next
        infixQueue.pop();
        continue;
    }
    while (!opStack.empty()){
        Postfix.push(opStack.top());
        opStack.pop(); 
    }

    double result = evalPostfix(Postfix);
    std::cout <<"result=" <<result;

    // 输出后缀表达式
    std::cout<<"  the Postfix is: ";
    while(!Postfix.empty()){
        std::cout << Postfix.front() << " ";
        Postfix.pop();
    }
    std::cout << " " << std::endl;
    
    return 0;
}
