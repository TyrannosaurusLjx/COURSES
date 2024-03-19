class Nim():
    def __init__(self) -> None:
        self.coins = []
        self.n = 0

    # 检查当前状态是不是安全的    
    def is_safe(self):
        bit_sum = self.coins[0]
        for coin in self.coins[1:]:
            bit_sum ^= coin
        
        return bit_sum == 0

    # 如果安全就调用这个函数计算最佳处理(实际上不唯一)
    def get_best(self):
        bit_sum = self.coins[0]
        for coin in self.coins[1:]:
            bit_sum ^= coin
        index = len(bin(bit_sum))-2 # 这里index 从 1 开始
        turn = 0
        need_change_index = -1
        need_change = self.coins[0]
        for i in range(self.n):
            coin = self.coins[i]
            if coin>>(index - 1) & 1 == True:
                need_change_index = i
                need_change = coin
                break
        bin_change = bin(need_change)[2:].zfill(self.n)
        
        bin_bit_sum = bin(bit_sum)[2:].zfill(self.n)
        
        for i in range(1,index+1):
            if bin_bit_sum[-i] == '0':
                turn += int(bin_change[-i])*2**(i-1)
            else:
                turn += ( int(bin_change[-i]) ^ 1 )*2**(i-1)
        need_delete = need_change - turn
        return need_change_index +1 , need_delete


    # 初始化函数
    def set_coins(self, lst):  
        if any(x <= 0 for x in lst):  
            raise ValueError("列表中存在小于等于 0 的元素，请重新输入。")  
        else:  
            self.coins = lst  
            self.n = len(lst)  
    
    # 打印当前状态
    def show_info(self):
        print("当前情况:",self.coins)
    
    # 接收需要删除的部分
    def get_delete(self):
        while True:
            try:
                index, num = map(int,input("输入你想取的堆号和堆数,以空格分割,按回车确定:").split())
                if index <= 0 or index > self.n:
                    print("堆号越界")
                    continue
                if num<=0 or num > self.coins[index-1]:
                    print("数量不合法")
                    continue
            except ValueError:
                print("输入不合法,重试")
            else:
                break

        return index-1, num
    
    # 判断游戏时候结束
    def success(self):
        return sum(self.coins) == 0

    # 主循环
    def main(self):
        # 初始化
        flag = -1
        self.set_coins(list(map(int,input("输入硬币堆的数目,以空格分割,按回车确定:").split())))
        
        while True:
            self.show_info()
            
            if self.is_safe():
                print("not safe")
            else:
                print("best change:",self.get_best())
            flag += 1
            index, value = self.get_delete()
            self.coins[index] -= value
            
            if self.success():
                print("玩家{}赢了".format(flag%2+1))
                break
            else:
                continue


if __name__ == "__main__":
    nim = Nim()
    nim.main()
