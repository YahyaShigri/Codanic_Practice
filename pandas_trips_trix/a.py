import re
name = "ali ahmed zakir"
user = input("what is your name: ")
result =re.search(user, name)
# print(result)
if result:
    print("yes")
else:
    print("no")