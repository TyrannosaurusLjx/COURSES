from test_for_realnumber_coding import *
 
# plot(target_function)
def run_with_popnum(num):
    times = 10
    pc = 0.8
    pm = 0.05
    pop_size = num
    dimension = 2
    head_size = np.array([2, 2])
    tail_size = np.array([2, 2])
    ga = GA(pc, pm, pop_size, dimension, head_size, tail_size, target_function)
    result = []
    for i in range(times):
        ga.run(200)
        X = ga.get_best()
        # print(f'Optimal solution: {X}')
        # print(f'Optimal value: {target_function(X)}')
        result.append(target_function(X))
    result = np.array(result)
    count = np.count_nonzero(result[result > 4])
    ratio = count / times
    return count, ratio
    
def main():
    num_lst = list(range(200,4000,50))
    ratio_lst = []
    count_lst = []
    for num in num_lst:
        print(num)
        count, ratio = run_with_popnum(num)
        count_lst.append(count)
        ratio_lst.append(ratio)
    ## 分别画出 count 和 ratio 的折线图(以 num 为横坐标)
    fig, axs = plt.subplots(2, 1, figsize=(8, 10))  # 2 行 1 列，调整 figsize 控制图片大小
    axs[0].plot(num_lst, count_lst, color='blue')
    axs[0].set_xlabel('Population')
    axs[0].set_ylabel('Count')
    axs[0].set_title('Count with Population')
    axs[1].plot(num_lst, ratio_lst, color='green')
    axs[1].set_xlabel('Population')
    axs[1].set_ylabel('Ratio')
    axs[1].set_title('Ratio with Population')
    plt.tight_layout()
    ## 保存图片
    plt.savefig('count_ratio_with_population.png')

    plt.show() 
main()
