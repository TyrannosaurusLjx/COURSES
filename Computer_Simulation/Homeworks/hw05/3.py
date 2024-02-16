import random as rd
import numpy as np
import matplotlib.pyplot as plt
def time_cost(patient_num):
    def serve():
        return rd.choices([24, 27, 30, 33, 36, 39],[0.1, 0.2, 0.4, 0.15, 0.10, 0.05])[0]
    def arrive(index):
        return 30*(index+1) + rd.choices([-15, -5, 0, 10, 15], [0.10, 0.25, 0.50, 0.10, 0.05])[0]
    
    ## 初始化信息矩阵
    guests = np.array([[0 for _ in range(patient_num)] for _ in range(5)])
    #["arrive", "serve", "stay", "leave", "option"]
    for index in range(patient_num):
        arrive_time, serve_time = arrive(index), serve()
        if index == 0:
            guests[:,index] = [arrive_time, serve_time, serve_time, arrive_time + serve_time , 0]
        else:
            last_leave = guests[3, index-1]
            if arrive_time >= last_leave:
                guests[:,index] = [arrive_time, serve_time, serve_time, arrive_time + serve_time, 0]
            else:
                wait = guests[3,index-1] - arrive_time
                stay = wait + serve_time
                guests[:,index] = [arrive_time, serve_time, stay, arrive_time + stay, 1]
    return guests
    
def plot_guests(guests):
    patientNum = len(guests[0])
    plt.plot(list(range(1,patientNum+1)), guests[0,:], label = "arrive")
    plt.plot(list(range(1,patientNum+1)), guests[3,:], label = "leave")
    plt.title("Arrival and Departure Times After 9:00")  
    plt.xlabel("Patient Index")  
    plt.ylabel("Time") 
    plt.legend() 
    plt.show()
    return 0

plot_guests(time_cost(16))
    
