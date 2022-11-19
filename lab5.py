# # # Question no 1

# # # number=int(input("enter table number  :"))
# # # for i in range(11):
# # #     print(number,"x",i,"=",number*i)

# # # Question no 2

# # # list =['Zia','Nabras','Zeeshan','Saif']
# # # c=len(list)
# # # for i in range(len(list)):
# # #     b=list[i]
# # #     if(b[0]=="S"):
# # #         print("greet ", list[i])


# # # Question no 3

# num=int(input("enter table number   :"))
# a=0
# while(a<=10):
#     print(num,"x",a,'=',num*a)
#     a+=1

# # # Question no 4

# # # a=int(input("enter number  :"))
# # # if(a%2==0):
# # #     print("number is not prime")
# # # else:
# # #     print("number is prime")


# # # Question no 5

# # # a=int(input("enter your number   :"))
# # # sum=0
# # # while(a>0):
# # #     sum+=a
# # #     a-=1
# # # print("sum of natural number is ",sum)

# # # Question no 6

# # # b= int(input('enter factorial number :'))
# # # fact=1
# # # if(b<0):
# # #     print("please enter positive number ")
# # # elif(b==0):
# # #     print("the factorial of 0 is 1 number")
# # # else:
# # #     for i in range(1,b+1):
# # #         fact*=i
# # #     print("the factorial of ",b,"is,",fact)


# # # Question no 7

# # # for i in range(1,5):
# # #     print(" "*(5-i),'*'*(i*2-1),)

# # # Question no 8

# # # for i in range(5):
# # #     print("*"*i)


# # # Question no 9

# # for i in range(5):
# #     for j in range(5):
# #         if(i==0 or j==0 or i==4  or j==4):
# #             print("*" ,end=' ')
# #         else:
# #             print(" " ,end=' ')


# #     print()



# # # Question no 10

a=int(input("enter table number  :"))
for b in range(10,0,-1):
    print(a,"x",b,'=',a*b)