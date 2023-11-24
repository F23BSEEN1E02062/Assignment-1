#print even and odd numbers from given lists
l1 = [10,20,25,30,35]
l2 = [40,45,60,75,90]
resultlist=[]
for i in l1:
    if i%2!=0:
        print(i,'odd number')
        resultlist.append(i)
for i in l2:
    if i%2==0:
        print(i,'even number')  
        resultlist.append(i) 
print(resultlist)        