# osモジュール
import os

print(os.name)
# os_name = os.name
# if os_name == 'nt':
#     print('WIndows')
# elif os_name == 'posix':
#     print('MAc/linux')

# 環境変数
print(os.environ.get('LANG'))
print(os.getenv('LANG'))
# environ = os.getenv('environ')
# if environ=='dev':
#     # 開発環境の処理、設定(DB, LOG)を読み込む
# elif environ == 'production':
#     # 本番環境

# getcwd, chdir, listdir,getpid,getppid

# print(os.getcwd())
# print(os.getpid())
# print(os.getppid())
# print(os.listdir())
# os.chdir('std_library')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())

os.system('dir') # mac ls

# フォルダ作成(mkdir)、フォルダ削除(rmdir)、フォルダ名、ファイル名変更(rename)
# os.mkdir('sample')
os.rename('sample', 'sample2')