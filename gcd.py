*** LCM--->LEAST COMMON MULTIPLE

a=int(input())
b=int(input())
x=a*b
while b!=0:
   a,a=b,a%b
lcm=x//a
print(lcm)


*** GCD OF TWO NUMBERS

x=int(input())
y=int(input())
while b!=0:
  a,b=b,a%b
print("GCD of 2 numbers is",a)

*** PRIME NUMBER OR NOT

n=int(input())
r=n**0.5
count=0
if a==1:
   print("not prime")
elif a==2:
   print("prime")
for i in range(2,int(r+1)):
   if(n%i==0):
    count=1
    break
if(count==0):
    print("prime")
else:
    print("not prime")

*** WRITE A PROGRAM TO PRINT ALL PRIME NUMBERS IN A RANGE

a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,i):
       if i%j==0:
          break
    else:
       print(i)

*** FIND WHETHER THE YEAR IS LEAF YEAR OR NOT

year=int(input())
if year%4==0 and year%400==0 or year%100!=0  :
    print("it is leaf year)
else:
    print("not a leaf year")

