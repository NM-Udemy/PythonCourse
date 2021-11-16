# decimal

from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP

float_num = 1.01
float_sum = 0.0
for _ in range(100):
    float_sum += float_num
print(float_sum)

decimal_val = Decimal(str(float_num))
decimal_sum = Decimal(0.0)
for _ in range(100):
    decimal_sum += decimal_val
print(decimal_sum)
print(decimal_val / Decimal('2'))

decimal_val = Decimal('87.325')

print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_DOWN)) # 87.32
print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_UP)) # 87.33
print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)) # 87.33
