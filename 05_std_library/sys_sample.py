import sys

# version, path
# print(sys.version)
# print(sys.path)
# print(sys.argv)
# if len(sys.argv) >= 2:
#     for x in sys.argv[1:]:
#         print(x)

# stdout

# with open('tmp.txt', mode='w') as fh:
#     sys.stdout = fh
#     print('AA')


# getsizeof

list_a = [x for x in range(10000)]
print(sys.getsizeof(list_a))
# exit
prit('AAAA')