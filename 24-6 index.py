'''#print name
print ("my name is darshan ")

#add two number

a=20
b=30
sum=a+b
print("the sum is :",sum)

#ask user name
name =input ("what is your name" )
print(name)

'''
#simpal calculator

'''
a=int(input("enter the number"))
b=int(input("enter the second number"))
print("addition:",a+b)
print("subtraction:",a-b)
print("mulitiplication:",a*b)
print("division:",a/b)

'''

#print  formating using sepand end:
'''
print("apple","banana","cherry",sep="|",end="<---end of list\n")
'''

#formating message from user input
'''
name=input("enter youar name :")
age=int (input("enter your age :"))
hobby = input ("enter your favorite hobby:")




print(f"heloo,{name}, at {age} enjoing,{hobby} sounfd fun!!! ")
'''

#declar variable of datatype and show their types
'''
a=10
b=3.14
c="python"
d=True

print(a,"type:",type(a))
print(b,"type:",type(b))
print(c,"type:",type(c))
print(d,"type:",type(d))
'''

#PYTHON PROGRAM
subject1=input("enter 1st subject name :")
marks1=int(input("enter the marks "))

subject2=input("enter 2nd subject name :")
marks2=int(input("enter the marks "))

subject3=input("enter 3rd subject name :")
marks3=int(input("enter the marks "))



total=marks1+marks2+marks3
average =total/3
if average >=90:
     grade="A"
elif average>=75:
    grad="B"
elif average>=60:
    grad="C"
elif average>=40:
    grad="D"
else:
    grade="fail"
print("\n-------result----------")
print(f"{subject1}:{marks1}")
print(f"{subject2}:{marks2}")
print(f"{subject3}:{marks3}")

print(f"total marks:{total}")
print(f"average marks:{average}")

     
