import random  
  
# 生成十万个随机数  
random_numbers = [random.random() for _ in range(100000)]  
  
# 将随机数转换为8位二进制形式  
binary_numbers = [format(int(num * 255), '08b') for num in random_numbers]  
  
# 将二进制数写入文件  
with open('random_numbers', 'wb') as file:  
    for binary_num in binary_numbers:  
        byte = int(binary_num, 2).to_bytes(1, 'big')  
        file.write(byte)  
        