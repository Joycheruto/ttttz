xxx = str(input("Enter your name: "))
with open("names.txt","w") as f:
     f.write("name saved !")
with open("names.txt","r") as f:
    content = f.read()
    print(content)
   


# try:
#     with open("ex.txt","r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("file does not exist")
# finally:
#     f.closed()
#     print("file closed")











