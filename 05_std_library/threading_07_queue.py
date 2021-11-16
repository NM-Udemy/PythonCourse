# threading_07_queue.py

from queue import Queue, Empty
from urllib.request import urlretrieve
from PIL import Image
from threading import Thread
import logging
import time

def download_image(url):
    # 画像をダウンロードする関数
    logging.info('downloading = {}'.format(url))
    download_path = url.split('/')[-1]
    # ダウンロードした画像の配置先(url http://www./hogehoge.jpg => hogehoge.jpg)
    urlretrieve(url, download_path)
    return download_path

def process_image(file_path):
    # 画像を加工する
    logging.info('processing = {}'.format(file_path))
    save_file_path = file_path.split('.')[0] + '_gray.' + file_path.split('.')[1]
    # hogehoge.jpg => hogehoge_gray.jpg
    img = Image.open(file_path)
    gray_img = img.convert('L')
    gray_img.save(save_file_path)
    return save_file_path

def upload_image(file_path):
    # アップロードする処理
    logging.info('アップロード完了 {}'.format(file_path))
    return 'http://upload_{}'.format(file_path)

class Worker(Thread):

    def __init__(self, func, in_queue, out_queue, max_size):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.max_size = max_size
    
    def run(self):
        work_count = 0
        while work_count < self.max_size:
            try:
                item = self.in_queue.get_nowait()
                if item != 'error':
                    result = self.func(item)
                else:
                    result = 'error'
                work_count += 1
            except Empty as e:
                time.sleep(0.5)
            except Exception as e:
                logging.info(e)
                self.out_queue.put('error')
                work_count += 1
            else:
                self.out_queue.put(result)
                time.sleep(0.1)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
download_queue = Queue()
process_queue = Queue()
upload_queue = Queue()
done_queue = Queue()

urls=[
'https://www.nblog09.com/w/wp-content/uploads/2018/12/desk-2158142__480.jpg',
'https://www.nblog09.com/w/wp-content/uploads/2019/01/mill-1620440__480-640x360.jpg',
'https://www.nblog09.com/w/wp-content/uploads/2019/05/nature-213364__480-640x360.jpg',
'https://www.nblog09.com/w/wp-content/uploads/2019/05/Mac-640x360.jpg',
'https://www.nblog09.com/w/wp-content/uploads/2019/01/christmas-1911637__480-640x360.jpg'
]
download_worker = Worker(
    download_image, download_queue, process_queue, len(urls)
)
process_worker = Worker(
    process_image, process_queue, upload_queue, len(urls)
)
upload_worker = Worker(
    upload_image, upload_queue, done_queue, len(urls)
)
download_worker.start()
process_worker.start()
upload_worker.start()

for url in urls:
    download_queue.put(url)
    time.sleep(0.1)

download_worker.join()
process_worker.join()
upload_worker.join()

logging.info('処理終了 = {}'.format(done_queue.queue))