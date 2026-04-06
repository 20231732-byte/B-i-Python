
_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new = []

new = []

for x in _list:
    if _list.count(x) == 1:
        _new.append(x)
        
for x in _list:
    if x not in new:
        new.append(x)

print(_new)
print(new)