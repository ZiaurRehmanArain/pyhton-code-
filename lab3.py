# # Question no 1

# a=int(input("enter the first number  :"))
# b=int(input("enter the second number  :"))
# c=int(input("enter the third number  :"))
# d=int(input("enter the fouth number  :"))


# if(a>b and a>c and a>d):
#     print(a,"a is greatest number ")
# elif(b>a and b>c and b>d):
#     print( b," b is greatest number")
# elif(c>a and c>b and c>d):
#     print( c," c is greatest number")
# elif(d>a and d>c and d>b):
#     print( d," d is greatest number")
# else:
#     print("two number are equal")
#     print("sorry please enter right")


# # Question no 2

# a= int(input("enter first subject number  :"))
# b= int(input("enter second subject number  :"))
# c= int(input("enter third subject number  :"))

# if(a>=0 and a<=100 and b>=0 and b<=100 and c>=0 and c<=100):
#     if(a>=40 and b>=40 and c>=40):
#         print("congrat pass in all subject")
#     elif(a<=40 and b<=40 and c<=40):
#         print("sorry fail all subject")
#     elif(a<=40 and b>=40 and c>=40):
#         print("fail in one subject and pass two subject")
        
#     elif(a>=40 and b<=40 and c>=40):
#         print("fail in one subject and pass two subject")
        
#     elif(a>=40 and b>=40 and c<=40):
#         print("fail in one subject and pass two subject")
     
#     elif(a>=40 and b>=40 and c<=40):
#         print("fail in one subject and pass two subject")
#     elif(a<=40 and b<=40 and c>=40):
#         print("fail in two subject and pass one subject")

#     elif(a>=40 and b<=40 and c<=40):
#         print("fail in two subject and pass one subject")
#     elif(a<=40 and b>=40 and c<=40):
#          print("fail in two subject and pass one subject")
# else:
#     print("please enter between 0 to 100 number")     


# Question no 3

# Make a lot of money
# Buy now
# click this
# subscribe
# first mehtod
# import re
# def detect_spam(text):
#  spam=['make alot of money','Buy now','Click this','subcrbe this']
#  for word in spam:
#     if re.search(word,text):
#         return True
#     return False
# print(detect_spam("make alot of money"))

# second method using input detect

# spam =['make alot of money','Buy now','Click this','subcrbe this']
# print("available statement  :",'make alot of money','Buy now','Click this','subcrbe this')
# b=input("enter your spam keyword   :")
# for i in spam:
#     if(i==b):
#       print("True")
#       break
#     else:
#         print('False')

# Question no 4

# a= input("enter  your name   :")
# b= len(a)
# if(b<=10):
#     print("In range of 10 and length is ",b)
# else:
#     print("out of range 10 and lenght is",b)
    
# Question no 5


# a=input("enter your name ")
# b=['zia','saif','nabras','zeeshan','umer','zaid']
# c=a.lower()
# d=" "
# for i in b:
#     if(i==c):
#         d="name is present"
#         break
#     else:
#         d="name is not present"
# print(d)


# Question no 6

# a=int(input("enter persentage of student  :"))
# if(a>=90 and a<=100):
#     print("excellent")
# elif(a>=80 and a<=90 ):
#     print("A grade")
# elif(a>=70 and a<=80 ):
#     print("B grade")
# elif(a>=60 and a<=70 ):
#     print("C grade")
# elif(a>=50 and a<=60 ):
#     print("D grade")
# else:
#     print("fail")