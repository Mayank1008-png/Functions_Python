#create function
def my_function():
    print("kya hall hai ladle")
#calling
my_function()

#function to add two number and print result
def  number(a,b):
    result =a+b
    print("my result is",result)
#calling
number(8,9)
number(3,5)

#RETURN=THE RETURN STATEMENT IS USED IN A FUNCTION TO SEND A RESULT BACK TO THE PLACE WHERE FUNCTION WAS CALLED. WHEN REturn IS EXCEUTED,THE FUNCTION STOP RUNNING AND IMMEDIATELY RETURN THE SPECIFIED VALUE.
#IN FUNCTION WE CAN USE ONLY ONE RETURN STATEMENT
#Example
def add(a,b):
    return a+b
result1=add(6,7)
print(result1)

#EXAMPLE 2
def celcius_to_farenite(celcius):
    farenite=(celcius*9/5 + 32)
    return farenite
temp1=celcius_to_farenite(0)
print("TEMP IN FERENTITE=",temp1)
print("with return=",type(temp1))

#Example 3
def celciustoferenite(celcius):
    farenite=(celcius*9/5+32)
    print(farenite)
temp2=celciustoferenite(50)
print("without return=",type(temp2)) #nonetype because when we find type of print statement its nonetype we can't use its again

#THE PASS STATEMENT= THE PASS STATEMENT IS A PLACEHOLDER IN A FUNCTION OR A LOOP . IT DOES NOTHING AND IS USED TO WRITE A CODE THAT WILL BE ADDED LATER OR TO DEFINE A EMPTY FUNCTION.
def my():
    pass

#Calculator
#STEP 1= CREATE FUNCTION
#function to add two number
def add(a,b):
    return a+b
#function to multiply two number
def mul(a,b):
    return a*b
#function to divide two number
def div(a,b):
    return a/b
def sub(a,b):
    return a-b
#for average``
def avg(a,b):
    return (a+b)/2
print("please choose an option:\n"\
      "1.ADDITION\n" \
      "2.SUBTRATION\n"\
      "3.Multiply\n"\
      "4.Divide\n"\
      "5.AVERAGE")
select=int(input("select 1,2,3,4,5="))
a=int(input("enter 1st number="))
b=int(input("enter 2nd number=" ))
if select==1:
    print("sum of two number is=",add(a,b))
elif select==2:
    print("subtration of two number is=",sub(a,b))
elif select==3:
    print("multiplication of two number is=",mul(a,b))
elif select==4:
    print("division of two number is=",div(a,b))
elif select==5:
    print("average of two number is=",avg(a,b))
else:
    print("invalid operation please select again")

#ARGUMENTS
def greeting(name):     #name is the parameter
    print("Congrats,"+ name + "!" )
greeting("Mayank")      #Mayank is the argument

# 4 type of arguments
#1. Required Arguments (single/multiple arguments)
def course(couse_name,instrator_name):
    print("My Course name is "+ couse_name + " and the instructor name is "+ instrator_name)
course("Physics","Alakh Pandey")

#2. DEFAULT ARGUMENTS
def gretting(name="Mayank"): #Mayank is the default value here
    print("Hello ! " + name)
gretting() #run without error using default value
gretting("Himanshu")

#3. Keyword Arguments (named arguments)
def numb(a,b):
    return a/b
result2=numb(b=3,a=2)
print(result2)       #result =  , it is a part of keyword arguments
result3=numb(3,2)   
print(result3)       #result=   , postional arguments

#4. Arbitrary Arguments (variable - lenght arguments *args and **kwarg)
#1.arbitratry postition arguments (*args) - store in tuple
def addn(*args):
    print(type(args))
    return sum(args)
res=addn(1,2,3,4)
print(res)
#example 2
def greting(*names):
    for name in names:
        print(f"hello , {name} !")  #f is use for formatting
greting("rohan","mohan","sohan")

#2.Arbitratory Keyword Arguments(**kwarg) - store in dictionary
def print_detail(**kwarg):
    for key,value in kwarg.items():
        print(f"{key}:{value}")
print_detail(name="Madhav",age="17",City="Najafgarh")