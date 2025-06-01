try:
    # 获取用户输入并转换为整数列表
    user_input = input("请输入数字序列（用空格分隔）: ")
    numbers = list(map(int, user_input.split()))

    if not numbers:
        print("错误：至少需要输入一个数字！")
    else:
        print("\n原始序列:", numbers)
        print("升序排列:", sorted(numbers))
        print("降序排列:", sorted(numbers, reverse=True))

except ValueError:
    print("错误：请确保所有输入都是有效数字！")
except Exception as e:
    print(f"发生未知错误: {str(e)}")