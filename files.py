file = open("exampley.txt","r")
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)

file.close()

file = open("practice.txt","w")
file.write("hello world!\n")
file.write("another line\n.")
file.close()

file = open("practice.txt","a")
file.write("this gets added to the end.\n")

file.close()

file = open("practice.txt","r")



file.close()
