import os
import sys
from pathlib import Path

# 3.13.1 (main, Dec  3 2024, 17:59:52) [Clang 16.0.0 (clang-1600.0.26.4)]
python_version = sys.version
print(python_version.split()[0], type(python_version))

print(sys.platform) #darwin, win32
print(sys.executable)
# /Users/matsumotonaoki/Documents/140_新Udemy_source/PythonCourse/.venv/bin/python
# print(sys.argv[1])

# /Users/matsumotonaoki/Documents/140_新Udemy_source/PythonCourse/06_stdlibrary
# /Users/matsumotonaoki/Documents/140_新Udemy_source/PythonCourse
print(os.getcwd())
# os.mkdir('test') # ディレクトリ作成

print(os.getenv('USER')) # win: USERNAME
print(os.getenv('MY_KEY')) # None

current_dir = Path.cwd()
print(current_dir)

file_dir = Path(__file__).parent # ファイルの入っているフォルダ
data_dir = file_dir / 'data'
data_dir.mkdir(exist_ok=True)
# フォルダがあってもエラーにならない
