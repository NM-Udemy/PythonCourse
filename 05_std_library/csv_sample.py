# csv

import csv

# 読込み
# with open('std_library/input.csv') as fh:
#     csv_reader = csv.reader(fh, delimiter=',', quotechar='|')
#     print(csv_reader.line_num)
#     for row in csv_reader:
#         print(row[0])
#         print(csv_reader.line_num)

# DictReader
# with open('std_library/input.csv') as fh:
#     csv_reader = csv.DictReader(fh, delimiter=',', quotechar='|', fieldnames=['name', 'age'])
#     csv_header = csv_reader.fieldnames
#     print(type(csv_header))
#     print(dir(csv_reader))
#     for row in csv_reader:
#         print(type(row))
#         print(row['name'])

# # # writer
with open('std_library/output.csv', mode='w', newline='') as fh:
    csv_writer = csv.writer(fh, delimiter='\t', quoting=csv.QUOTE_NONE)
    csv_writer.writerows([['a','b','c'],[1,2,3]])


# # DictWriter
# with open('std_library/output.csv', mode='w', newline='') as fh:
#     fieldnames = ['name', 'age']
#     csv_writer = csv.DictWriter(fh, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerow({'age': 19, 'name': 'Taro'})
#     csv_writer.writerows([{'name': 'Hanako', 'age': 30}, {'name': 'Jiro', 'age': 40}])