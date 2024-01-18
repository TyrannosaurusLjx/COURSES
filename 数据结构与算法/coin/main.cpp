#include <iostream>
#include"coin.h"


int main(){
    // 测试用例
    std::vector<int>testTarget={30, 45, 100, 11, 1,311};
    std::vector<std::vector<int>>testAmounts={{10, 2, 1, 4}, {1, 1, 1, 1}, {10, 10, 10, 10}, {5, 0, 0, 0}, {1, 0, 0, 0}, {7, 8, 9, 7}};
    std::vector<int>answer={2, -1, 4, -1, 1, 30};

    for(int i = 0; i<testTarget.size(); i++){
        int target = testTarget[i];
        std::vector<int>amounts = testAmounts[i];
        int result = coin(target, amounts);
        std::cout<<"目标值:"<<target<<";";
        std::cout<<"期望值:"<<answer[i]<<";";
        std::cout<<"运行结果:"<<result<<std::endl;
    }
    return 0;
}
