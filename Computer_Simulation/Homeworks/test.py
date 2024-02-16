
import random
import math

def pi_needle(n):
    # 构建一个整数坐标的格，设置针的长度为1，那么 N/M = 2/π
    M = 0

    def circle_choice(x, y):
        theta = random.uniform(0, 2 * math.pi)
        x_ = x + math.cos(theta)
        y_ = y + math.sin(theta)
        return x, y, x_, y_

    def intersect(x, y, x_, y_):
        if math.floor(y) != math.floor(y_):
            return True
        return False

    for i in range(n):
        x = random.uniform(0, 10)  # 修正范围，确保在 [0, 10] 内
        y = random.uniform(0, 10)  # 修正范围，确保在 [0, 10] 内
        x, y, x_, y_ = circle_choice(x, y)

        if intersect(x, y, x_, y_):
            M += 1

    if M == 0:
        print("Fail")
        return 0
    else:
        return 2 * n / M

n = int(input("how many times you wanna simulate: "))
result = pi_needle(n)
print(f"Estimated value of pi: {result}")
