# 要复制一个序列可以用切片的方法 直接赋值的话会导致将同一个序列给了两个变量
# 对其中一个做改变的时候另外的一个变量也会改变
# 列表中间放列表就构造了一个矩阵  matrix[i][j]用来访问第i－1行第j－1列的元素
# del是个删除语句

# #1
# list_1 = list(map(int,input('身高').split()))
# ave = 1/len(list_1)*(sum(list_1))
# list_2 = []
# for i in list_1:
#     if i >= ave:
#         list_2.append(i)
# for j in list_2:
#     print(j,end=' ')

# #2
# list_1 = input('输入你的身份证号')
# list_2 = []
# for i in list_1:
#     list_2.append(int(i))
# M1 = list_2[-1]
# sum_list_2 = 0.07*list_2[0]+0.09*list_2[1]+0.10*list_2[2]+0.05*list_2[3]+0.08*list_2[4]+0.04*list_2[5]+0.02*list_2[6]+0.01*list_2[7]+0.06*list_2[8] \
#              +0.03*list_2[9]+0.07*list_2[10]+0.09*list_2[11]+0.10*list_2[12]+0.05*list_2[13]+0.08*list_2[14]+0.04*list_2[15]+0.02*list_2[16]
# Z = int(100*sum_list_2%11)
# S_M2 = [1,0,'X',9,8,7,6,5,4,3,2]
# M2 = S_M2[Z]
# if M2 == M1:
#     print("合法号码")
# else:
#     print('你的身份证号不合法！')


m , n = map(int,input().split())
m , n = min(m,n) , max(m,n)
s = 0
for i in range(m,n+1,1):
    s += (i**2+1/i)
print('sum = {:.6f}'.format(s))


