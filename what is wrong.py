#User function Template for python3

class Solution:
    def IsPerfect(self,l,n):
        #Complete the function
        s=''
        for i in l:
            s+=str(i)
        n=int(s)
        print("n",n)
        x=n
        rev=0
        while(n>0):
            t=n%10
            rev=(rev*10)+t
            n=n//10
        print("rev",rev)
        print("x",x)
        if rev==x:
            return  "PERFECT"
        else:
            return  "NOT PERFECT"
###################################################
# https://practice.geeksforgeeks.org/problems/perfect-arrays4645/1?page=2&difficulty[]=-2&sortBy=submissions
####################################################
l=[20,4,15,10,14,19,11,8,5,19,13,8,18,13,3,12,8,16,19,11]
# 2041510141911851913818133128161911
s=''
for i in l:
    s+=str(i)
print(int(s))
n=int(s)
x=n
rev=0
while(n>0):
    t=n%10
    rev=(rev*10)+t
    n=n//10
print(rev)
if rev==x:
    print("palidrome")
else:
    print("not a palidrome")
