# random_sample

import random

# randint, random, shuffle

# print(random.randint(0, 5)) # 0以上、5以下

# print(random.random()) # 0~1少数

list_a = list(range(5))
random.shuffle(list_a)
# print(list_a)

# choice
list_a = tuple(range(5))
a = random.choice(list_a)
# print(a)

# choices 重複あり
list_b = list(range(100))
list_c = random.choices(list_b, k=100)
# print(list_c)

# sample 重複無
# list_c = random.sample(list_b, k=101)
# print(list_c)

# gauss(ガウス分布), normalvariate(正規分布)
# print(random.gauss(0, 2)) # 平均0, 標準偏差2のgauss
# print(random.normalvariate(0, 2))

# random.seed
random.seed(1) # システム時間
for x in range(10):
    print(random.random())