_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new = []

for x in _tuple:
    if x not in _new:
        _new.append(x)

_new_tuple = tuple(_new)

print(_new_tuple)