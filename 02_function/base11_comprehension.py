# リスト内包表記

numbers = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in numbers] 
print(squares) # [1, 4, 9, 16, 25, 36]

result = [x if x > 0 else 0 for x in range(-2, 3)]
print(result) # [0, 0, 0, 1, 2]


# 辞書内包表記
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print('単語の長さ:', word_lengths)
# 単語の長さ: {'apple': 5, 'banana': 6, 'cherry': 6}

scores = {"Alice": 85, "Bob": 72, "Charlie": 90}
passed = {
    name: score
    for name, score in scores.items() 
}
print(passed)

# 集合内包表記
import math
sqrt_set = {math.sqrt(x) for x in range(10)}
print(sqrt_set, type(sqrt_set))

text = "Hello world programming"
vowels = {char.lower()
          for char in text if char.lower() in 'aiueo'
          }
print(vowels)

# ジェネレータ内包表記
large_numbers = (
    x**2
    for x in range(1000000) if x % 1000 == 0)

for _ in range(5):
    print(next(large_numbers))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = (
    x for x in range(1, 100) if is_prime(x)
)
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))

# セイウチ演算子
numbers = range(1, 11)
expensive_calc = [
    (n, result)
    for n in numbers
    if(result := n**2 + n*3) > 20
]
print(expensive_calc)

texts = ['apple', 'banana', 'cherry', 'pine']
long_words = {word: length
              for word in texts
              if (length := len(word)) > 4}
print(long_words)

sales_data = [
    {"product": "A", "price": 100, "quantity": 5},
    {"product": "B", "price": 200, "quantity": 3},
    {"product": "C", "price": 300, "quantity": 6},
]

high_revenue = {
    item["product"]: revenue
    for item in sales_data
    if(revenue := item["price"] * item["quantity"]) > 500
}
print(high_revenue)