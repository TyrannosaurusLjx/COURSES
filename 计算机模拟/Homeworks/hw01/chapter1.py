import random
import math


def batteryprint(time, num, surplus):
    print("现在有{}个电池，已经工作了{}h，下一个电池充满还有{}".format(num, time, surplus))

def battery(time=0, num=2, surplus=0):
    if time >= 1000:
        print("it has worked for 1000h")
        return time
    batteryprint(time, num, surplus)
    if num == 0:
        return time
    if num == 2:
        cost = random.randint(1, 6)
        time += cost
        num -= 1
        return battery(time, num, surplus=random.choice([1,3]))
    if num == 1:
        cost = random.randint(1, 6)
        time += cost
        num -= 1
        if surplus <= cost:
            num += 1
            surplus = 0
        return battery(time, num, surplus = random.choice([1,3]))

#print(battery())


# chapter1 T5
def dice(mapping):
    dice1 = random.choice(range(1,7))
    dice2 = random.choice(range(1,7))
    needs = mapping[(dice1, dice2)]
    print("dice1 = {}, dice2 = {}, we need {} books".format(dice1, dice2, needs))
    return needs

def earns(books, needs):
    money = 0
    if needs >= books:
        money = books*5
    else:
        money = -5*books + 10*needs
    print("earn {}".format(money))
    return money

def chapter1_5(nums):
    # (1,1)-(1,3) = 12  (1,4)-(3,3) = 13  (3,4)-(5,2) = 14 (5,3)-(6,3) = 15 (6,4)-(6,6) = 16
    map12 = [(1,i) for i in range(1,4)]
    map13 = [(1,i) for i in range(4,7)] + [(2,i) for i in range(1,7)] + [(3,i) for i in range(1,4)]
    map14 = [(3,i) for i in range(4,7)] + [(4,i) for i in range(1,7)] + [(5,i) for i in range(1,3)]
    map15 = [(5,i) for i in range(3,7)] + [(6,i) for i in range(1,4)]
    map16 = [(6,i) for i in range(4,7)]
    #mapping = {map12:12, map13:13, map14:14, map15:15, map16:16}
    mapping = {}
    for key in map12:
        mapping[key] = 12
    for key in map13:
        mapping[key] = 13
    for key in map14:
        mapping[key] = 14
    for key in map15:
        mapping[key] = 15
    for key in map16:
        mapping[key] = 16

    max_profit = 0
    suit_books  = 0

    for book in range(12,17):
        ave_profit = 0
        for simulation in range(nums):
            print("have:",book)
            need = dice(mapping)
            earn = earns(book,need)
            ave_profit += earn
        ave_profit /= nums
        if ave_profit > max_profit:
            suit_books = book
            max_profit = ave_profit
    print("max profit {}, buy {} books".format(max_profit, suit_books))

#chapter1_5(int(input("模拟次数")))

# pi
def pi_needle(n):
    # 构建一个整数坐标的格，设置针的长度为1，那么N/M=2/pi
    M = 0

    def circle_choice():
        x, y = random.uniform(0,10), random.uniform(0,10)
        theta = random.uniform(1,2*math.pi)
        x_ = x + math.cos(theta)
        y_ = y + math.sin(theta)
        print(x,y,x_,y_)
        return x, y, x_,y_

    def intersect(x,y,x_,y_):
        if math.floor(y) != math.floor(y_):
            return True
        return False

    for i in range(n):
        x, y, x_, y_ = circle_choice()

        if intersect(x,y,x_,y_):
            M += 1
            print("intersect！")
        else:
            print("no")

    if M == 0:
        print("Fail")
        return 0
    else:
        return 2*n/M

print(pi_needle(int(input("how many times you wanna simulate"))))

def pi_throws(n):
    m = 0
    def in_circle(x,y):
        dis = (x-0.5)**2 + (y-0.5)**2
        if dis < 1/4:
            return True
        else:
            return False

    for i in range(n):
        x, y = random.uniform(0,1), random.uniform(0,1)
        if in_circle(x,y):
            m += 1
    pi = 4*m/n
    print("pi = {}".format(pi))
    return pi

pi_throws(int(input("n")))







