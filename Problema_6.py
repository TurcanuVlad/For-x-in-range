n=int(input("Dati numarul dorit= "))
a=1
s=0
s1=0
s2=0
s3=0
s4=0
s5=0
p=1
d=0
for a in range(1,n+1,1):
    s=a+s
print("Raspunsul la primul exemplu= ", s)

n=int(input("Dati numarul dorit= "))
for a in range(1,n+1,1):
    s1=((a-1)*a)+s1
print("Raspunsul la al 2 exemplu este= ", s1)

n=int(input("Dati numarul dorit= "))
for a in range(1,n+1,1):
    p*=a
    s2+=p
print("Raspunsul la al 3 exemplu este= ", s2)

n=int(input("Dati numarul dorit= "))
for a in range(1,n+1,1):
    a=str(a)
    a=int(a+"2")
    s3=s3+a
print("Raspunsul la exemplul 4 este= ", s3)

n=int(input("Dati numarul dorit= "))
for a in range(1,n+1,1):
    d=a/(a+1)
    s4=s4+d
print("Raspunsul la al 5 exemplu este= ", s4)

n=int(input("Dati numarul dorit= "))
for a in range(1,n+1,1):
    a=str(a)
    a=int("2"+a)
    s5=s5+a
print("Raspunsul la al 6 exemplu= ", s5)
