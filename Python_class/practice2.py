list=[8,1,9,2,3,4,5,6,6,2,1,7,8,9]
list.append('numbers')
print(list)
list.insert(2,'hello')
print(list)
x = list.index(2,4,-1)
list.remove(x)
print(len(list))
print(list.count(4))
last = list.pop(x)
print(list,last)
print(id(x))
print(id(last))
print(list[::-1])
print(list[::])
