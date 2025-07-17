x = 12
print(x)

#operators
#1.arithmetc operators
#2.relational operators
#3.logical operators


#DATA TYPES
#1.NUMERICS
#integers and floats and booleans 

temp = 22.5
temp_as_int = int(temp)
print(temp_as_int)

#age = 24
#age_as_float= float(age)
#print(age_as_float)

raining = int(True)
print(raining)
sunny = int(False)
print(sunny)

#sequences
#strings

name ="Emmanuel "
name_2 =" Esther"
school = "Chi code lab"

print(name + name_2)#concantenation

value = 15
value_as_a_string = str(value)
print(value_as_a_string)

#string manipulation

name_3 = "Raynelle"

print(name_3[5])
print(name_3[-5])
#string slicing
print(name_3[2:])
print(name_3[2:5])
print(name_3[:-3])

#string inbuilt methods

#lenght of string

department = "electrical"
print(len(department))
print("p" in department )
print(department.capitalize())#it should capitalize everything
print(department.strip("e"))#you strip at the ends only
print(department.index("t"))
print(department.find("t"))

#string formatting
nomenclature = "Elizabeth"
age = 22
print(f"my name is {nomenclature} and am {age} years old")

years = 56
txt = "my name is John and am {}"
print(txt.format(years))

degree = (1,2,34,4)
print(degree[0])