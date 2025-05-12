try:
    # 获取用户输入并转换为整数列表
    user_input = input("请输入数字序列（用空格分隔）: ")
    numbers = list(map(float, user_input.split()))

    if not numbers:
        print("错误：至少需要输入一个数字！")
    else:
        # 升序排序
        asc_sorted = sorted(numbers)
        # 降序排序
        desc_sorted = sorted(numbers, reverse=True)

        print("\n原始序列:", numbers)
        print("升序排列:", asc_sorted)
        print("降序排列:", desc_sorted)

except ValueError:
    print("错误：请确保所有输入都是有效数字！")
except Exception as e:
    print(f"发生未知错误: {str(e)}")