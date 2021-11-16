import re

msg = 'Phone number: "Taro": "090-1111-2222", "Jiro": "080-3333-4444"'
match = re.findall(r'"([a-z,A-Z]+)": "(\d{2,4}-\d{2,4}-\d{2,4})"', msg)
print(match)
print(type(match))

# sub

txt = 'My    name is  Taro. I like     Baseball'
print(re.sub(r'\s+', ' ', txt))

msg = 'Apple: 100yen, Orange: 300yen, Grape: 200yen'
print(re.sub(r':\s(\d+)yen', r': \1dollar', msg, 2))

# split
txt = 'The rain in 1spain mainly falls on the plain'
print(re.split(r'\d', txt))
