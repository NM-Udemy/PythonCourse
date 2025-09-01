def calculate_tax(price: int, rate: float) -> int:
    return int(price * (1 + rate))

print(calculate_tax(1000, 0.1)) # 1100.0
# print(calculate_tax("1000", 0.1)) # 1100.0

value: int = calculate_tax(1000, 0.1)
