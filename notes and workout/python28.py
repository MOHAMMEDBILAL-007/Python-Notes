#f string
letter ="hey my name is {} and iam from {}"
name="joe"
country='america'
print(letter.format(name,country))
print(letter.format(country,name))#python doesent care which variable belongs to where


letter ="hey my name is {1} and iam from{0}"#specifying which index variable belongs to which place
print(letter.format(country,name))
# this method takes a lot of space and need a lot of code so we use

print(f"my name is {name} and iam from {country}")
#or
print("hey my name is {} and iam from {}".format(name,country))

# we can even specify the number of digits we can print
value = 3.1454345332
print(f"value = {value:.2f}")
# if i want the out put same as written in the string not replaced by values we use {{}}
print(f"my name is {{name}} and iam from {{country}}")
