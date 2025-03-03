import random
from copy import deepcopy

#myList = [1, "Hi", True, 7.5]
#myList2 = list((4, 6, 87))

#print(myList[2:6:2])


#concatenation:

myList1 = [1, 2, 3, 5]
myList2 = [[3, 4], [5, 6], 7]
myListCopy = deepcopy(myList2)


#print(["Test", 3]*4)
#myList1[1:3] = ["Changed", "Changed"]
#myList1.append("New item")
#print(myList1)
#myList1.insert(-1, "new item")
#print(myList1)
#myList1.extend(myList2)
#print(myList1)
#myList.remove("Hi")
#print(myList)
#myVar=myList.pop(2)
#print(myVar)
#del myList
#myList.clear()
#print(myList)


#create a list with 10 random int numbers:
#myList=[]
#for i in range(0, 10):
#    myList.append(random.randint(-10, 10))
#print(myList)

#myList = random.sample(range(-10, 11), 20)
#print(myList)

myList = [random.randint(-10, 10) for i in range(0, 10)]
#print(myList)

oddList = []
for item in myList:
    if item % 2 != 0:
        oddList.append(item)
print(myList)
print(oddList)