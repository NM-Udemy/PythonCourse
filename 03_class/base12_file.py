from pathlib import Path
script_dir = Path(__file__).parent

with open(script_dir / 'data' / 'sample.txt', 'r', encoding='utf-8') as f:
    print(type(f))
    content = f.read() # メモリに全内容をロード
    print(content, type(content))
    f.seek(0) # 最初に戻す
    lines = f.readlines() # リスト形式でメモリにロード
    print(lines, type(lines))
    f.seek(0)
    # while True:
    #     line = f.readline()
    while line := f.readline():
        print(line)
