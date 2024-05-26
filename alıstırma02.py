s1=int(input("sayı 1 "))
s2=int(input("sayı 2 "))
s3=int(input("sayı 3 "))

if s2<s1<s3:   
    print(bool(True))
    
elif s3<s1<s2:
    print(bool(True))
    
else:
    print(bool(False))