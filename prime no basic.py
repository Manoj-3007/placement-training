n=int(input())
while(n!=0):
  a=n%10
  c=0
  for i in range(2,(a//2)+1):
    if(a%i==0):
      c=c+1
      #break
    #c will give the no faactors
    
print(c)
if(c==0):
  print("it is a prime no")         
else:
   print("not")