# if 1行 lambda

y = 10
x = 0 if (y-20) > 0 else 1 # y>0 => 0 else 1
# print(x)

lambda_a = lambda x: x * x # 引数x 返り値x*x

print(lambda_a(10))
lambda_b = lambda x, y, z=5: x * y * z
print(lambda_b(2,3)) # x=2, y=3, z=5 => 30
print(lambda_b(2,3,4)) # x=2, y=3, z=4 => 24

# 条件式付きlambda
lambda_c = lambda x, y: y if x < y else x # if(x<y) => y, else x
print(lambda_c(6, 4))
