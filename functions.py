# def say_hello():
#     print("hi there")
# say hello()


# def greet(name):
#     print(f"hello,{name}!")
# greet("Joy")


# def greets(name,age):
#     print("hello",name,"my age is", age)
# greets("joy",19)
# class_mean =20
# def square(x):#a and b are parammeters
#     print(x*x)
# square(227.737)
# square(class_mean)

# def is_even(n):
#     if n %2==1: 
#         print("it is odd")
#     else:
#         print("it is even")

# is_even(22)

# def product_numbers(*b):
#     a= 1
#     for i in b:
#         a = a * i
#     return a
# print(product_numbers(4,11,22,44))


# def times_numbers(x,y):
#     return x*y
    
# #times_numbers(13,17)
# print(times_numbers(13,17))


# score =eval(input("enter the score:"))
# def grade_student(score):
#     if score>70:
#         return "A"
#     elif score >60:
#         return "B"
#     elif score >50:
#         return "C"
#     elif score >40:
#         return "D"
#     else:
#         return "supp"
# print(grade_student(62))

# age = eval(input("enter the age"))
# def age_person(age):
#     if age<10:
#         return "this is a child"
#     elif age <20:
#         return "this is a teen"
#     elif age <70:
#         return "this is an adult"
#     else:
#         return "you are old"
    
# print(age_person(20))




# def name(first,last):
#     print(first,last)

# name ("JOY","lijood")
# name()

# def sum (a,b):
#     return a+b
# print(sum ("hello ","world"))
# print(sum (2,5))

# def square(x):
#     return x * x
# answer =square (131)
# print(answer)



#  score =eval(input("enter the score:"))
#name ="joy"
# def assign_score(name,grade):
#     if grade >70:
#         grade =  "A"
#     elif grade >60:
#         grade =  "B"
#     elif grade >50:
#         grade =  "C"
#     elif grade >40:
#         grade =  "D"
#     else:
#         return "supp"
#     return name + grade
    
# mark = assign_score("joy  ",66)
# print(mark)
# print(assign_score("Joy",55))

def assign_score(name,grade):
    if grade >70:
        return  "A"
    elif grade >60:
        return  "B"
    elif grade >50:
        return  "C"
    elif grade >40:
        return  "D"
    else:
        return "supp"
    
name =str(input("enter name "))
grade = eval(input("enter grade "))
    
print( assign_score(name,grade))
