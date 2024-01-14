# #验证自然数正负倒数和等于ln2
# n = int(input('输入一个整数'))
# list_1 = [1/i if i%2 == 1 else -1/i for i in range(1,n+1,1)]
# print(sum(list_1))
# import math
# print(math.log(2,math.e))
# print(math.log(2,math.e) - sum(list_1))

# #例2-10
# n = int(input('输入一个整数'))
# list_1 = [1/i if i%4 == 1 else -1/i for i in range(n+1) if i%2 == 1]
# print(sum(list_1))

#实部和虚部都是浮点数

# #49第十题
# x = float(input('键入x的值'))
# import math
# f_x = math.sin((7/36)*math.pi) + (math.e**x-15*x)/math.sqrt(x**4+1)
# print(f_x)

#编程题
# #1
# n = int(input('键入一个正整数'))
# list = [i for i in range(n+1)]
# print(sum(list))

# #2 分段函数
# x = float(input("输入x的值"))
# if x == 0 :
#     result = 0
# else:
#     result = 1/x
# print("f({0:.1f}) = {1:.1f}".format(x,result))

# #3阶梯电价
# x = float(input("your cost"))
# if 0 < x < 50:
#     yc = 0.53*x
#     print(yc)
# elif 50 < x :
#     yc = 0.53*50 + (x-50)*0.58
#     print(yc)
# else:
#     print('Invalid Value')

# #数列求和
# a = input('a')
# n = int(input('n'))
# list_1 = [int(a*i) for i in range(1,n+1)]
# print(sum(list_1))

# #求奇数和  没写出来
# list_1 = list(input().split())
# list_2 = [int(i) for i in list_1]
# list_3 = [i for i in list_2 if i>0 and i%2 == 1]
# print(sum(list_3))

# #6
# n = int(input())
# list_1 = list( i/(2*i-1) if i%2 == 1 else -i/(2*i-1) for i in range(1,n+1) )
# print('{:.3f}'.format(sum(list_1)))

# #第2章-12	输出三角形面积和周长
# list_1 = list(map(int,input().split()))
# list_1.sort()
# if list_1[0] + list_1[1] > list_1[2]:
#     perimeter = sum(list_1)
#     s = perimeter/2
#     import math
#     area = math.sqrt(s*(s-list_1[0])*(s-list_1[1])*(s-list_1[2]))
#     print('area = {0:.2f}; perimeter = {1:.2f}'.format(area,perimeter))
# else:
#     print('These sides do not correspond to a valid triangle')

#
#	第2章-13	分段计算居民水费
# x = int(input())
# if x <= 15:
#     y = 4*x/3
# else:
#     y = 2.5*x-17.5
# print('{:.2f}'.format(y))

# #第2章-14	求整数段和
# A,B = map(int(),input().split())
# h = 0
# s = 0
# for i in range(A,B+1,1) :
#     print('{:>5}'.format(i),end = '')
#     s += i
#     h += 1
#     if h == 5:
#         print("\n",end='')
#         h = 0
#     elif(i==B):
#         print("\n",end="")
# print('sum = {}'.format(s))



