# include<vector>
int coin(int target, std::vector<int>amounts){
    std::vector<int>coins={1,5,10,25};
    std::vector<int>dp(target+1, INT16_MAX);
    dp[0]=0;
    for(int j = 0; j < coins.size(); j++){
        for(int k = 1; k<= amounts[j]; k++){
            for(int i = target; i >= coins[j]; i--){
                dp[i] = std::min(dp[i], dp[i-coins[j]] + 1);
            }
        }
    }
    if(dp[target] != INT16_MAX){
        return dp[target];
    }else{
        return -1;
    }
}

