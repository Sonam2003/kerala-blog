# t=int(input())
# for i in range(t):
#     n,x=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     c=0
#     for i in range(len(a)):
#         if a[i]>=x:
#             c+=b[i]
#     print(c)
# print(a)
# print(b)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[1,2,3],[4,5,6],[7,8,9]]
# c=[]
# for i in range(len(a)):
#   h=0
#   for j in range(len(a[i])):
#     h=h+a[i][j]+b[i][j]
#     c.append(h)
# print(c)
# n=int(input("enter:  "))
# list1 = [0]*n
# p = 0
# while p < n:
#     a = int(input('enter element: '))
#     list1[p]=a
#     p+=1
# print(list1)
# k = int(input("enter skipping no.:  "))
# l = []
# i = 0
# y=0
# count = 1
# while len(l)<=n:
#     if y==n:
#         break
#     elif list1[i] =="A":
#         pass
#     elif count ==k:
#         l.append(list1[i])
#         list1[i]="A"
#         count=1
#         y+=1
#     else:
#         count+=1
#     i=(i+1)%((n))
# print(l)
# a=[1,2,3,4,5,5,6,7,7]
# b=[1,1,4,2]
# s=set()
# for i in range(len(a)):
#     s.add(a[i])
# for i in range(len(b)):
#     s.add(b[i])
# print(list(s))




# n=int(input("Enter the number of element: "))
# list=[0]*n
# i=0
# while i<n:
#   a=int(input("Enter the number: "))
#   list[i]=a
#   i+=1
# i=0
# f=[]
# while i<n:
#   count=0
#   j=i+1
#   while j<n:
#     if list[i]!=list[j]:
#       f[i]=list[i]
#       print(f[i])
#     j+=1
# print(f)
#   if count==1:
#     print(list[i],end=" ")
#   i+=1


# n=int(input("Enter th enumber of element you want: "))
# b=[0]*n
# sum=0
# for i in range(n):
#   a=int(input("Enter the number:"))
#   b[i]=a
#   sum+=b[i]
# print("Mean=",sum/n)# Mean

# for i in range(n):
#     for j in range(i+1,n):    #Bubble sort
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
#         else:
#             if b[i]==b[j]:
#                 print("Mode=",b[i],end=",")
# s1=0
# c=n//2
# if n%2!=0:
#     print("Median=",b[c])      #Median with Odd Number
# else:
#     s1+=b[c]+b[c-1]
#     print("Median",s1/2)               #Median with even Number
n=int(input("Enter th enumber of element you want: "))
b=[0]*n
sum=0
for i in range(n):
  a=int(input("Enter the number:"))
  b[i]=a
  sum+=b[i]
print("Mean=",sum/n)          # Mean

for i in range(n):
    count=0
    for j in range(i+1,n):    #Bubble sort
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
        else:
            if b[i]==b[j]:
              count+=1
    if count==1:
      print("Mode=",b[i])
s1=0
c=n//2
if n%2!=0:
    print("Median=",b[c])      #Median with Odd Number
else:
    s1+=b[c]+b[c-1]
    print("Median",s1/2) 
    