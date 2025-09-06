from functools import partial, lru_cache
import time


def calculate_price_with_tax(price, tax_rate):
    return int(price * (1 + tax_rate))

japan_price = partial(
    calculate_price_with_tax, tax_rate=0.1
)

print(japan_price(1000)) # 1100
print(japan_price(2500)) # 2750

@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

start_time = time.time()
result = fibonacci_cached(30)
end_time = time.time()
print(f'duraction: {end_time - start_time:.7f}')
# cacheなし: 0.0983732
# cacheあり: 0.0000362