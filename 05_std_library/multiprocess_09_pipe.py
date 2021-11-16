# multiprocess_09_pipe.py


from multiprocessing import Process, Pipe

def sender(conn, msgs): #値を入れる
    for msg in msgs:
        conn.send(msg)
        print('Sent message: {}'.format(msg))
    conn.close()

def receiver(conn): # 値を取り出す
    while 1:
        msg = conn.recv()
        if msg == 'END':
            break
        print('received message: {}'.format(msg))


if __name__ == '__main__':
    msgs = ['hello', 'hey', 'goodbye', 'END']
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(parent_conn, msgs))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()