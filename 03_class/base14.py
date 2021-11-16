# ファイル出力、追記


file_path = 'resources/output.csv'

f = open(file_path, mode='w', encoding='utf-8', newline='\n')
f.write('あああ\nいいい')
f.close()
with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ', 'い', 'う']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))
    # f.writelines(list_a[0])
