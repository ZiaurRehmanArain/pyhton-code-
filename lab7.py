# # # # # Question no 1

# for a1 in range(2,21):
#     use_For_All_Data_Empty=open("table/table"+str(a1)+".txt","w")
#     use_For_All_Data_Empty.write(" ")
#     use_For_All_Data_Empty.close()
#     #  main purpose is next file data empty
#     for b in range(11):

#         if(a1==2):
#             c=open("table/table2.txt","a")
#             c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#             c.close()
#         elif(a1==3):
#              c=open("table/table3.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==4):
#              c=open("table/table4.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==5):
#              c=open("table/table5.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==6):
#              c=open("table/table6.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==7):
#              c=open("table/table7.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==8):
#              c=open("table/table8.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==3):
#              c=open("table/table3.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==9):
#              c=open("table/table9.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==10):
#              c=open("table/table10.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==11):
#              c=open("table/table11.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==12):
#              c=open("table/table12.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==13):
#              c=open("table/table13.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==14):
#              c=open("table/table14.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==15):
#              c=open("table/table15.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==16):
#              c=open("table/table16.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==17):
#              c=open("table/table17.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==18):
#              c=open("table/table18.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==19):
#              c=open("table/table19.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         elif(a1==20):
#              c=open("table/table20.txt","a")
#              c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
#              c.close()
#         else:
#             print("every thing is ok")


#########################################################################

for a1 in range(2,21):
    use_For_All_Data_Empty=open("table/table"+str(a1)+".txt","w")
    use_For_All_Data_Empty.write(" ")
    use_For_All_Data_Empty.close()
    #  main purpose is next file data empty
    for b in range(11):

        # if(a1==2):
            c=open("table/table"+str(a1)+".txt","a")
            c.write((str(a1)+"x"+str(b)+"="+str(a1*b)+"\n"))
            c.close()
    

#########################################################################

     

# # #  Question no 2

# a=open('table/Questionno2.txt','r')
# for b in a.readlines():
#     # print(b)
#     b=b.lower()
#     if(b=="donkey"):
#         c=open('table/Questionno2.txt','wt')
#         c.write("#########")
#         a.read()
 


# # Question no 3
# count=0
# a=open("log.txt","r")
# list=[]
# for i in a.readlines():
#  list.append(i)
 
# print(list)
 

# # Question no 4
# count=0
# a=open("log.txt","r")

# for i in a.readlines():

#  count+=1
#  if(i in 'python'):
#      print(count,'avialable in python')
#      break

# # Question no 5

# # count=0
# # a=open("this1.txt","r")

# # for i in a.readlines():

# #  count+=1
# #  if(i in 'python'):
# #      print(count,'line avialable in python')
# #      break

# # Question no 6

# # first method

# a=open('this1.txt','r')
# b= a.read()
# c=open('pastedata.txt','w')
# d=c.write(b)

# # second method

# import shutil
# shutil.copy("this1.txt","pastedata.txt")
# # Question no 7

# a=open('this1.txt','r')
# b= a.read()
# # print(b)

# c=open('pastedata.txt','r')
# d=c.read()
# # print(d)
# if(b==d):
#     print("files is match")
# else:
#     print("sorry file is not match")


# # Question no 8

# # import os
# # os.remove("remove.txt")

# # a=open("remove.txt",'w')
# # d=a.write(' ')
# # Question 9


# # import os
# # os.rename("this.txt","this1.txt")


# # Question 10

# a= int(input("enter value  :"))
# f=open("highScore.txt",'r')
# b=int(f.read())
# print("before value of file is ",b)
# if(a>b):
#     b=a
#     f=open("highScore.txt",'w')
#     s=str(a)
#     f.write(s)
#     print("write of ",s)
# elif(a==b):
#       f=open("highScore.txt",'r')
#       f.read()
# else:
#     print("sorry")




# 