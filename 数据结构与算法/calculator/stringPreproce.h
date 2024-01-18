#include <iostream>
#include <stack>
#include <string>
#include <cctype>

/**
 * @brief 错误提示函数
 *
 * 当遇到非法表达式时，输出错误信息并退出程序。
 */
void err_exp(){
    std::cout << "\nError!" << std::endl;
    exit(-1);
}

/**
 * @brief 判断字符是否是操作符
 * @param op 要检查的字符
 * @return 如果字符是操作符，则返回 true，否则返回 false
 */
bool isop(char op){
    if(op == '+' || op == '-' || op == '*' || op == '/' || op == '(' || op == ')'){
        return true;
    }else{
        return false;
    }
}

/**
 * @brief 判断字符是否是四则运算符
 * @param ch 要检查的字符
 * @return 如果字符是四则运算符但不是括号，则返回 true，否则返回 false
 */
bool isFourOp(char ch){
    if(isop(ch) && ch != '(' && ch != ')'){
        return true;
    }else{
        return false;
    }
}

/**
 * @brief 判断字符是否是小数点
 * @param op 要检查的字符
 * @return 如果字符是小数点，则返回 true，否则返回 false
 */
bool ispoint(char op){
    if(op == '.'){
        return true;
    }else{
        return false;
    }
}

/**
 * @brief 括号处理函数
 * @param str 要检查的字符串
 * @return 如果括号合法，返回 true，否则返回 false
 */
bool bracketCheck(std::string str){
    int lcount = 0,rcount = 0;
    bool result = true;
    char ch=' ',leftch = ' ',rightch=' ';
    // 括号栈
    std::stack<char> bracketStack;
    for(int i=0; i < str.length(); i++){
        ch = str[i];
        if(ch == '('){
            lcount += 1;
        }
        if(ch == ')'){
            rcount += 1;
        }

        // 两端分别判断
        if(i == 0){
            rightch = str[i+1];
            if(ch == ')' || ispoint(ch) || ch == '*' || ch == '/' ||  (ch == '(') && (rightch == ')' || rightch == '.' || rightch == '*' || rightch == '/') || (ch == '+' || ch == '-') && !(isdigit(rightch))  ){
                result = false;
                break;
            }
        }else if(i == str.length()-1){
            leftch = str[i-1];
            if(ch == '(' || (ch == ')' && !(isdigit(leftch) || leftch == ')') )){
                result = false;
                break;
            }
        }
        
        // 中间
        leftch = str[i-1];
        rightch = str[i+1];
        // 括号左右不合法处理
        if(ch == '('){
            if(isdigit(leftch) || ispoint(leftch) || leftch == ')' || rightch == '*' || rightch == '/' || ispoint(rightch) || rightch == ')'){
                result = false;
                break;
            }else{
                bracketStack.push(ch);
            }
        }else if(ch == ')'){
            if(!(isdigit(leftch) || leftch == ')') || rightch == '(' || isdigit(rightch) || ispoint(rightch)){
                result = false;
                break;
            }else{
                if( !bracketStack.empty() && bracketStack.top() == '('){
                    bracketStack.pop();
                }else{
                    result = false;
                    break;
                }
            }
        }
    }
    if(lcount != rcount){
        result = false;
    }
    return result;
}



/**
 * @brief 操作符处理函数
 * @param str 输入的字符串
 * @return 如果操作符合法，返回 true，否则返回 false
 */
bool opCheck(std::string& str){
    bool result = true;
    char ch;
    for(int i = 0; i < str.length(); i++){
        ch = str[i];
        if(isFourOp(ch)){
            if(isFourOp(str[i+1])){
                result = false;
                break;
            }
        }
    }
    if(isFourOp(str[str.length()-1])){
        result = false;
    }
    return result;
}

/**
 * @brief 总判断函数
 * @param infix 输入的中缀表达式
 * @return 经过预处理的表达式
 */
std::string strPreproce(std::string infix){
    std::string preInfix;
    char ch;
    // 处理除了操作符、小数点和数字以外的字符
    for(int i=0; i < infix.length(); i++){
        ch = infix[i];
        if(isdigit(ch) || ispoint(ch) || isop(ch)){
            preInfix += ch;
        }else if(isalpha(ch)){
            continue;
        }
    }

    // 检查括号合法性
    if(bracketCheck(preInfix) != true){
        err_exp();
    }
    // 检查运算合法性
    if(opCheck(preInfix) != true){
        err_exp();
    }

    infix = preInfix;
    return infix;
}

/**
 * @brief 将字符串转换为队列
 *
 * 此函数将输入的中缀表达式字符串转化为队列，以便后续处理。
 *
 * @param infix 输入的中缀表达式字符串
 * @return 转化后的队列
 */
std::queue<std::string> strToQueue(std::string infix){
    std::queue<std::string> result, fixedResult;
    std::string item;
    bool atNum = true;
    char ch;
    for(int i = 0; i < infix.length(); i++){
        ch = infix[i];
        if(isop(ch)){
            atNum = false;
        }else{
            atNum = true;
        }
        if(atNum){
            item += ch;
        }else{
            if(item != ""){
                result.push(item);
            }
            item = "";
            result.push(std::string(1, ch));
        }
    }
    // 处理最后一个字母
    if(atNum){
        result.push(std::string(1, ch));
    }
    // 处理负数
    std::string s1, s2, s3;
    if(result.front() == "-"){
        s1 = result.front();
        result.pop();
        if(result.empty()){
            err_exp();
        }else{
            s2 = result.front();
            result.pop();
        }
        fixedResult.push(s1 + s2);
    }

    while(!result.empty()){
        s1 = result.front();
        result.pop();
        fixedResult.push(s1);

        if(s1 == "(" && !result.empty()){
            s2 = result.front();
            if(s2 == "-"){
                result.pop();
                s3 = result.front();
                result.pop();
                fixedResult.push(s2 + s3);
            }
        }else{
            continue;
        }
    }
    while (!result.empty())
    {
        std::cout<<result.front();
        result.pop();
    }
    std::cout<<" "<<std::endl;


    
    return fixedResult;
}
