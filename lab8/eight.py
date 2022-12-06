# # Question no 1
# lists=[]
# for a in range(7):
#     b=input("enter friut name that store in list  no {0}:".format(a))
#     lists.append(b)
# print(lists)



# # # Question no 2
# marks=[]
# a1=0
# for a in range(7):
#     b=int(input("enter marks is 0 to 100 of student  no {0}:"))
#     if(b>=0 and b<=100):
#         marks.append(b)
#         print("data add")
#         a1+=1
#     else:
#         print("enter number 100 range sorry data no add")
# print(a1 ,"number data add and you see list" )
# print(marks)



# Question no 3


# changedata=("zia","saif","faizan")

# print(changedata[0])  #access data 
# changedata[0]='saif'  # you see output in console tuple data cannot be change


# Question no 4
# first mehtod
# number=[34,56,34,56]
# b=0
# for a in number:
#   b+=a 
# print(b)

# # second method
# number=[34,56,34,56]
# print(sum(number))


# Question no 5

# first method
num=(0,3,5,8,0,6,5,0,3,0)
b=0
for a in num:
    if(a==0):
        b+=1
print("zero is repeatation in tuple",b)

# second method
num=(0,3,5,8,0,6,5,0,3,0)
print(num.count(0))