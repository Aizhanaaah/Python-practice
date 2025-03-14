import copy
import random

#exercise one
number = [1, 2, 3, 45, 6, 7, 8, 9, 10]
random.shuffle(number)
print(number)
shuffle1 = copy.deepcopy(number)
print(id(number))
print(shuffle1)
print(id(shuffle1))
shuffle2 = random.sample(number, len(number))
print(shuffle2)
print(id(shuffle2))

#exercise two
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
randomStudent = random.choice(students)
print(randomStudent)
random2Students = random.sample(students, 2)
print(random2Students)


#exercise 3

colors = ['red', 'blue', 'green', 'yellow', 'purple']
shuffled = []
temp = copy.deepcopy(colors)
for i in range(len(colors)):
    current = random.randint(0, len(temp)-1)
    shuffled.append(temp[current])
    temp.pop(current)
print(shuffled)


#exercise 4
sentence = "Python is fun to learn"
list1 = sentence.split()
print(list1)
random.shuffle(list1)
print(list1)

#exercise 5
list2 = []
for j in range(6):
    current1 = random.randint(1, 49)
    list2.append(current1)
print(list2)


#exercise 6
groups = [['Alice', 'Bob'], ['Charlie', 'David'], ['Eve', 'Frank']]
random.shuffle(groups)
shuffle = copy.deepcopy(groups)
for i in range(len(groups)):
    for j in range(len(groups[i])):
        random.shuffle(shuffle[i])
print(shuffle)
