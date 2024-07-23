import pandas as pd
import random
import string



# 定义数据生成函数
def generate_data(num_rows):
    data = []
    teams = ['重点客户', '普通客户', '非优先客户']



    classifications = ['初次接触', '正在跟进','准备购买','准备付款','已经购买']
    sources = ['行业活动', '搜索引擎', '客户转介绍', '展会','朋友介绍']
    phone_numbers = [f'13{random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}' for _ in
                 range(num_rows)]

    for i in range(num_rows):

        team = random.choice(teams)

        classification = random.choice(classifications)
        source_group_name = random.choice(sources)

        phone_number = phone_numbers[i]
        name =f'客户{i + 1}'

        data.append([team, classification, source_group_name, phone_number, name])

    return data

# 生成数据
data = generate_data(50)

# 创建DataFrame
df = pd.DataFrame(data, columns=['客户所属', '客户状态', '客户来源', '手机号', '客户姓名'])

# 保存到Excel
df.to_excel('客户数据2.xlsx', index=False)