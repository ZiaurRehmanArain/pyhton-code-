marks=[]
a1=0
for a in range(7):
    b=int(input("enter marks is 0 to 100 of student  no {0}:".format(a)))
    if(b>=0 and b<=100):
        marks.append(b)
        print("data add")
        a1+=1
    else:
        print("enter number 100 range sorry data no add")
print(a1 ,"number data add and you see list")
print(marks)
