# f =open("exam.txt","w")  #this creates a new file
# f.write("python is quite fun ") #this  write on the file
# # f.close()

# f=open("exam.txt","r")#this brings it on the terminal
# content = f.read()
# print(content)
# f.close()

#second method of opening files
# with open("exam2.txt","w") as f:
#     f.write("python is python\n")
#     f.write("he loves it ")

# try:
#     with open("ex.txt","r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("file does not exist")
# finally:
#     f.closed()
#     print("file closed")

options = str(input("choose one option(read or write:)"))

if (options == "write"):
    entry = str(input("enter the entry: "))
    file = open("diary.txt","w")
    file.write(entry)
elif(options == "read"):
    try:
        with open ("diary.txt","r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("file not found")
else:
    print(f"the option '{options}' entered is invalid")




    print("woring on git hub!!!!")

