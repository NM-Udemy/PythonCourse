# Queue

from queue import Queue
q = Queue(maxsize=3) # キューの初期化

print(q.qsize())
print(q.queue) # 中身表示
print(q.empty()) # 空True
print(q.full())
q.put('A')
q.put('B')
q.put('C')
q.put_nowait('D')
print(q.qsize()) # サイズ表示
print(q.queue) # 中身表示
print(q.empty()) # 空True
print(q.full())
# var = q.get()
# print(var)
# print(q.queue)
# print(q.get())
# print(q.get())
# # print(q.get())
# print('処理終了')