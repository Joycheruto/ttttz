try:
    file = open("prac.txt","r")
    content = file.read()
except FileNotFoundError:
    print("file not found ")
else:
    print("file read successfully...")
finally:
    print("This runs always ,even if there is an error")

    #catching multiple exceptions



try:
    v = {1:"john",7:"faith"}
    
except ValueError:
    print("this is a value error ")
except TypeError:
    print("this is a type error..")
finally:
    print("sssss")