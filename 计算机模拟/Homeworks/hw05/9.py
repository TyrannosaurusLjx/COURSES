import random as rd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
import math

def bank(clientNum):
    client = [[0 for _ in range(clientNum + 1)] for _ in range(7)]
    # lineName = ["arrive_time", "serving_num", "isquit", "wait_time", "serve_time", "stay_time", "leave_time"]
    
    # 判断是否要放弃服务
    def isQuit(number):
        quit = True
        if number < 6:
            quit = False
        elif number <= 8:
            quit = rd.choices([True, False],[0.2, 0.8])[0]
        elif number <= 10:
            quit = rd.choices([True, False],[0.4, 0.6])[0]
        elif number <= 14:
            quit = rd.choices([True, False],[0.6, 0.4])[0]
        else:
            quit = rd.choices([True, False],[0.8, 0.2])[0]
        return quit
    
    # 获取当前有多少人在服务 (包括队列中的和排队中的)
    def get_serving(index0,arrive_time):
        stay_client_leave_time = [leave_time for leave_time in client[6][index0:] if leave_time > arrive_time]
        serving_num = len(stay_client_leave_time)
        if serving_num == 0:
            return (1, 0, stay_client_leave_time)
        else:
            index0 = client[6][index0:].index(stay_client_leave_time[0])
            return (index0, serving_num, stay_client_leave_time)
     
    
    # 获取服务时间
    
    def serve():
        rv = expon(scale = 3)
        return rv.rvs()
    
    
    # 一次性生成所有人的arrive-time
    def arrive(client_num):
        lambda_val = 1 # 一分钟平均到达一个
        rv = expon(scale = 1/lambda_val)
        time_gap = rv.rvs(size=client_num)
        arrive_time = [time_gap[0]]
        for i in range(1,len(time_gap)):
            arrive_time.append(arrive_time[i-1] + time_gap[i])
        return arrive_time
        
    
    # 主循环
    client[0][1:] = arrive(client_num=clientNum) # 生成到达时间
    index0 = 1 # 缩短查询时间
    for index in range(1,clientNum + 1):
        arrive_time = client[0][index]
        result = get_serving(index0,arrive_time=arrive_time)
        index0,serving_num,stay_client_leave_time = result[0],result[1],result[2]
        
        if serving_num < 4:
            isquit = False
            wait_time = 0
            serve_time = serve()
            stay_time = serve_time
            leave_time = arrive_time + stay_time
        else:
            isquit = isQuit(serving_num)
            if isquit:
                isquit = True
                wait_time = 0
                serve_time = 0
                stay_time = 0
                leave_time = arrive_time
            else:
                isquit = False
                wait_time = min(stay_client_leave_time) - arrive_time
                serve_time = serve()
                stay_time = wait_time + serve_time
                leave_time = arrive_time + stay_time
                
        colInfo = [arrive_time, serving_num, isquit, wait_time, serve_time, stay_time, leave_time]
        for i in range(7):
            client[i][index] = colInfo[i]
    return client
    
result = bank(200)

# 绘制折线图
def bankPlot(client):
    x = list(range(len(client[0])))
    plt.plot(x,client[0], label = "arrive")
    plt.plot(x,client[4], label ="serve_time")
    plt.plot(x,client[5], label ="stay_time")
    plt.plot(x,client[6], label ="leave_time")
    plt.xlabel("clients")
    plt.ylabel("time")
    plt.legend()
    plt.show()
    
bankPlot(result)

print("预计等待时间:{}".format(np.mean(result[3])))
print("出纳员忙概率:{}".format(1-sum([4-i for i in result[1] if i < 4]) / (4*len(result[1]))))

