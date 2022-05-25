#lstrip
str="    ram"
print(str.lstrip())

str="##ram"
print(str.lstrip('#'))

#rstrip
str ="ram    "
print(str.rstrip())

str="ram###"
print(str.rstrip('#'))

#replace
str="this is  a python class and is running"
print (str.replace("is","was"))
print (str.replace("is","was", 2))

#split
str ="this is string example......wow!!!"
print (str.split())
print (str.split('i',1))
print (str.split('w'))

#splitlines
str= "this is \nstring example"
print(str.splitlines())

#strip
str="##Nepal##"
print(str.strip('#'))
