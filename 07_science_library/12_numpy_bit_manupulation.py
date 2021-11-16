# 12_numpy_bit_manupulation.py


import numpy as np


x = np.array([0,1,0,1])
y = np.array([0,0,1,1]) #1 => 000000001 -> 11111110

print(np.bitwise_and(x, y)) # xとyの論理積
print(np.bitwise_or(x, y)) # xとyの論理和
print(np.bitwise_xor(x, y)) # xとyの排他的論理和
print(np.bitwise_not(x)) # xとyの否定(0 -> 1, 1->0)

print(x & y) # 論理積
print(x | y) # 論理和
print(x ^ y) # 排他的論理和
print(~ x) # 否定
