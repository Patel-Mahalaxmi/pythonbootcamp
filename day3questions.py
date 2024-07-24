

#1Q.Find even number or not
# a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    if(a[i]%2==0):
        print("even number")
    else:
        print("not even number")


#2Q:Find odd nbr or not
#a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    if(a[i]%2!=0):
        print("odd number")
    else:
        print("not odd number")
pe

#3Q:Find 3rd gretest nbr
#a,b,c=map(int,input().split())
if(a>b and a>c):
    print("a")
elif(b>c and b>c):
    print("b")
else:
    print("c")
#4Q:Find the peak elements

#a=list(map(int,input().split()))
l=len(a)
count=0
for i in range(1,(l)-1):
    if(a[i]>a[i-1] and a[i]>a[i+1]):
        count=i
    if(a[-1]>a[-2] and a[-i]>count ):
        count=l-1
print(a[count])
op:1 2 3  4 5
5
op:10 20 15 2 23 90 67
20
90

#5Q:second laegest nbr
#a=list(map(int,input().split()))
l=len(a)
a.sort(reverse=True)
for i in range(1,l):
    if(a[i] != a[0]):
        print(a[i])
        break
    else:
        print("no second largest number")
#6Q:Find squares of elements in array
l1=list(int(input().split()))
l=len(l1)
for i in range(l):
    a[i]=a[i]*a[i]
    print(a[i])
#7Q:Find squares of even elements & odd elements 
a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    if(a[i]%2==0):
       a[i]=a[i]*a[i]
        print("even number")
    else:
        print("not even number")
8#a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    if(a[i]%2!=0):
        a[i]=a[i]*a[i]
        print("odd number")
    else:
        print("not odd number")

#9Q:Find GCD
a=int(input())
b=int(input())
lcm=a*b
while b!=0:
    a,b=b,a%b
print("GCD of 2 number is ",a)
x=lcm//a
print("lcm is ",x)

#10Q:sum of digits
n=int(input())
sum=0
while n>0:
   r=n%10
   sum+=r
   n=n//10
print(sum)
 
#11Q:leap year
yr=int(input())
for i in range(2000,2025):
   if(yr%400==0 and yr%400==0 or yr%100!=0):
      print("leap year")
   else:
      print("not leap year") 

#12Q:FIND THE MAXIMUM ELEMENT IN AN ARRY
a=list(map(int,input().split()))
max=a[0]
for i in range(0,len(a)):
    if(a[i]>max):
       max=a[i]
print(max)

#13Q:reverse an array without using buildin functions
a=int(input())
rev=""
while n>0:
   rem=a%10
   rev=rev*str(rem)
   a=a//10
print(int(rev))


#15Q: FIND SQUARES OF ELEMENTS IN ARRAY
l1=list(map(int,input().split()))
l=len(l1)
for i in range(l):
    a[i]=a[i]*a[i]
    print(a[i])

#16Q: check number is palindrome with while loop
a=int(input())
rev=""
while n>0:
   rem=a%10
   rev=rev*str(rem)
   a=a//10
print(int(rev))
if(a==rev):
   print("palindrome")
else:
   print("not a palindrome")
#17Q:swapping 2nbrs
n=int(input())
sum=0
for i in range(n):
    sum=(n*(n+1))//2
print(sum)
a=10
b=20
a=a ^ b
b=b ^ a
a=a^b
print(a)
print(b)























