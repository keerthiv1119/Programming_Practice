import textwrap
k = input()
w = int(input())
a = textwrap.wrap(k,w)
print('\n'.join(a),end=" ")
