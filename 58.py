g,y=map(int,input().split())
m=list(map(int,input().split()[:g]))
count=0
for i in m:
   if(i==y):
      print("yes")
      break
else:
   print("no")
