# threading_05_gil2.py

import concurrent.futures
import time

number = 10000000
write_data = ''.join([str(x) for x in range(number)])

def write_file(file_name):
    with open(file_name, mode='w') as fh:
        fh.write(write_data)

start_time = time.time()

# write_file('tmp1.txt')
# write_file('tmp2.txt')
# write_file('tmp3.txt')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(write_file, ['tmp1.txt', 'tmp2.txt', 'tmp3.txt'])

end_time = time.time()
print(end_time - start_time)