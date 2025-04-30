import crayon
while True:
    num = int(input())
    num_32 = num & 0xFFFFFFFF  # 确保处理32位范围内的值
    binary_str = bin(num_32)[2:].zfill(32)  # 转换为二进制并补零到32位
    groups = [binary_str[i:i+4] for i in range(0, 32, 4)]
    print(' '.join(groups))