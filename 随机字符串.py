import random
import os

# ==================== 硬编码配置区域 ====================
CHARSET = [  # 可自由修改的字符池
    'a', 'b', 'c', 'd'  # 小写字母
]
STRING_LENGTH = 10 # 生成的字符串长度
OUTPUT_PATH = "D:\\bobi2\\development\\work spaces\\OI-code\\input.txt"  # 输出文件路径


# ==================== 配置结束 ====================

def generate_new_string():
    """生成全新随机字符串并立即写入文件"""
    # 使用系统随机源增强随机性
    secure_random = random.SystemRandom()
    new_string = ''.join([secure_random.choice(CHARSET) for _ in range(STRING_LENGTH)])

    # 原子化写入操作
    temp_file = OUTPUT_PATH + ".tmp"
    with open(temp_file, 'w') as f:
        f.write(new_string)
        f.flush()
        os.fsync(f.fileno())

    # 替换旧文件
    os.replace(temp_file, OUTPUT_PATH)
    return new_string


if __name__ == '__main__':
    # 生成并保存
    result = generate_new_string()

    # 终端输出验证
    print(f"[全新生成] 长度：{STRING_LENGTH}  文件：{os.path.abspath(OUTPUT_PATH)}")
    print(f"生成内容：{result[:4]}...{result[-4:]}")  # 只显示首尾各4位
    print("完整内容已安全写入目标文件")