a = int(input('Enter number: '))

if a>0:
    print('positive')
elif a<0:
    print('negative')
else:
    print('zero')

#if you want to ignore one case just use pass:

if a>0:
    print('positive')
elif a<0:
    print('negative')
elif a % 1 == a:
    pass
else:
    print('zero')


if "Py" in "Python":
    print('ok')

#for loops

for i in range(10):
    print(i)

for i in 'Python':
    print(i)


for i in range(2, 20, 4):
    print(i)

#swap:

x = int(input('number 1: ' ))
y = int(input('number 2: ' ))

temp = x
x = y
y = temp

print(x)
print(y)


#while loop:

i=0

while i < 10:
    print(i)
    i+=1

