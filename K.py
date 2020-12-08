def strlenF(c):
       count=0
       for i in c:
             count=count+1
       print("the lenth is",count)
c=str(input("enter a string"))
strlenF(c)
n=int(input("Enter the size of list"))
lst=[]
for i in range(0,n):
	k=input("enter list element")
	lst.append(k)
	
strlenF(lst)
