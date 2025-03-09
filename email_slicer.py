#email slicing

email = input("Enter your email: ")
#aijanamanova22@gmail.com
index = email.index("@")
username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")

#name slicing

name = input("Please type your full name: ")
index = name.index(" ")
firstName = name[:index]
lastName = name[index+1:]
print(f"first name is {firstName}")
print(f"last name is {lastName}")

#remove the first and last characters:

word = input("write a word:")
removed = word[1:-1]
print(f"first and last char is removed: {removed}")

#extract a certain word python:

sentence = 'i love programming in python'
pythonIndex = sentence.index('python')
print(f"extracted word: {sentence[pythonIndex]}")