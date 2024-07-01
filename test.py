# 示例data列表
data = [1, 2, 3, 4, 2, 3, 4, 4, 5, 1, 10, 10, 10]

# 创建一个只有键1到10的字典，初始值为0
count_dict = {key: 0 for key in range(1, 11)}

# 遍历data列表，统计每个数字出现的次数
for number in data:
    if number in count_dict:
        count_dict[number] += 1

print(count_dict)
