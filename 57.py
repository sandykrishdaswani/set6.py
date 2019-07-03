v,b=map(int,input().split())
h=list(map(int,input().split()[:v]))
count=0
for i in h:
   if(i==b):
      count=count+1
print(count) 
