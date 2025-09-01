import math

print(math.ceil(1.7)) # 小数点以下切り上げ->int
print(math.sqrt(3))

import sys
print(sys.path)  # importする対象のフォルダ
# ['/Users/matsumotonaoki/Documents/140_新Udemy_source/PythonCourse/05_package',
# '/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python313.zip', 
# '/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13',
# '/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload',
# '/Users/matsumotonaoki/Documents/140_新Udemy_source/PythonCourse/.venv/lib/python3.13/site-packages']
import numpy

print(sys.modules) # importしたライブラリ一覧

import math_utils # math_utilsが実行される
print(math_utils.add(10, 20)) # 30
print(math_utils.multiply(5, 5)) # 25
