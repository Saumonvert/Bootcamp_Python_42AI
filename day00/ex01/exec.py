import sys

args = sys.argv
res = ' '.join(args[1:])[::-1]

print(res.swapcase())