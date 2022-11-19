a=open('table/Questionno2.txt','r')
for b in a.readlines():
    # print(b)
    b=b.lower()
    if(b=="donkey"):
        c=open('table/Questionno2.txt','wt')
        c.write("#########")
        a.read()