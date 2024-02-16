import random

def batteryprint(time, num, surplus):
    print("现在有{}个电池，已经工作了{}h，下一个电池充满还有{}".format(num, time, surplus))

def battery(time=0, num=2, surplus=0):
    if time >= 1000:
        print("机器爆炸了")
        return time
    batteryprint(time, num, surplus)
    if num == 0:
        return time
    if num == 2:
        cost = random.randint(1, 6)
        time += cost
        num -= 1
        return battery(time, num, surplus=2.5)
    if num == 1:
        cost = random.randint(1, 6)
        time += cost
        num -= 1
        if surplus <= cost:
            num += 1
            surplus = 0
        return battery(time, num, surplus = 2.5)


print(battery())

