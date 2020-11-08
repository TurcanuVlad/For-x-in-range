a=int(input("Dati inceputul intervalului="))
b=int(input("Dati sfirsitul intervalului="))
for a in range(a,b+1,1):
    if a%2!=0:
        print(a)