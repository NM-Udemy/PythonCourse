import gzip

data = 'こんにちは\nさようなら'

# with gzip.open('text.txt.gz', mode='wb') as f:
#     f.write(data.encode('utf-8'))

# with gzip.open('text.txt.gz', mode='rt', encoding='utf-8') as f:
#     while (line := f.readline()):
#         print(line)

with gzip.open('text.txt.gz', mode='ab') as f:
    f.write('さようなら\nお疲れ様です。'.encode('utf-8'))

with gzip.open('text.txt.gz', mode='rt', encoding='utf-8') as f:
    while (line := f.readline()):
        print(line)
