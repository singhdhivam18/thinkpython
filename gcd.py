def  gcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return gcd(b,r)
ans=gcd(27,6)
print(ans)