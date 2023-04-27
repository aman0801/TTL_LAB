a=int(input())
n=a
s=0
while a>0:
        s+=(a%10)**3
        a=int(a/10)
if s==n:
        print("armstrong")
else:
        print("not armstrong")
