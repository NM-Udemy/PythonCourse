from pathlib import Path
script_dir = Path(__file__).parent
ouput_txt = script_dir / 'data' / 'output.txt'
with open(ouput_txt, 'w', encoding='utf-8') as f:
    f.write('Hello World!')
    f.write('\nこんにちは世界')
    
    lines = ['りんご\n', 'ばなな\n', 'ぐれーぷ\n']
    f.writelines(lines)

with open(ouput_txt, 'a', encoding='utf-8') as f:
    f.write('私の名前は田中です。')
    
    lines = ['りんご\n', 'ばなな\n', 'ぐれーぷ\n']
    f.writelines(lines)

