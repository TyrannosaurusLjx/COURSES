#include <iostream>
#include <queue>
#include <string>
#include <list>
#include <stack>

/**
 * @brief 判断字符串是否为数字
 *
 * 判断字符串的最后一个字符是否为数字，用于确定是否是数字。
 *
 * @param str 要检查的字符串
 * @return 如果字符串最后一个字符是数字，则返回 true，否则返回 false
 */
bool isnum(std::string str){
    if(isdigit(str[str.size()-1])){
        return true;
    }else{
        return false;
    }
}

/**
 * @brief 执行后缀表达式计算
 *
 * 给定一个后缀表达式队列，计算其结果并返回。
 *
 * @param Postfix 后缀表达式队列
 * @return 计算结果
 */
double evalPostfix(std::queue<std::string>& Postfix);

/**
 * @brief 执行二元运算
 *
 * 根据操作符执行二元运算，如加法、减法、乘法和除法。
 *
 * @param s1 第一个操作数
 * @param s2 第二个操作数
 * @param op 操作符（+、-、*、/）
 * @return 计算结果
 */
double eval(double s1, double s2, std::string op){
    double result = 0;
    if(op == "+"){
        result = s1 + s2;
    }else if(op == "-"){
        result = s1 - s2;
    }else if(op == "*"){
        result = s1 * s2;
    }else{
        result = s1 / s2;
    }
    return result;
}

double evalPostfix(std::queue<std::string>& Postfix){
    std::queue<std::string> cpPostfix(Postfix);
    std::stack<double> result;

    double item, s1, s2;
    std::string op;
    while(!cpPostfix.empty()){
        op = cpPostfix.front();
        cpPostfix.pop();
        if(isnum(op)){
            result.push(std::stod(op));
        }else{
            s2 = result.top();
            result.pop();
            s1 = result.top();
            result.pop();
            item = eval(s1, s2, op);
            result.push(item);
        }
    }
    return result.top();
}
