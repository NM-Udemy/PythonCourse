import re

txt = "I like tenis"
x = re.search(r'\bt\w+', txt)
print(type(x))
print(x.group()) # group: 中身表示

pattern = r'^a...s$'
test_string = 'abyss'
result = re.search(pattern, test_string)
if result:
    print(result.group())
else:
    print('Not exists')

msg = 'Im 30 years old'
match = re.search(r'(\d{2}) years', msg)
print(match.group()) # 検出した値
print(match.start()) # 最初のインデックス
print(match.end()) # 最後のインデックス
print(match.span()) #(最初、最後)
print(match.re) # 検索値
print(match.string) # 対象文字列


msg = 'Im 40 years, name is Jiro.'
match = re.search(r'Im (\d{1,3}) years, name is (.*?)\.', msg)
print(match.groups()) # ()の値
print(match.group(1)) # 40
print(match.group(2)) # Jiro
