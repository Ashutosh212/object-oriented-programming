# import sys

# if len(sys.argv) == 1:
#     print("Ashutosh")
# elif len(sys.argv) == 3 and sys.argv[1] == '-n':
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meows")
# else:
#     print("usage: cheer function")

# Note : doing abpve thing using argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, help="Number of times of meow", type=int)
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")