
def TrojkatPascala(n):
    result=[]
    for x in range(n+1):
        trojkat = []
        trojkat.append(1)
        if x==1:
            trojkat.append(1)
        elif x>1 :
            for y in range(1,x):
                trojkat.append(result[x-1][y]+result[x-1][y-1])
            trojkat.append(1)
        result.append(trojkat)
    return result

def TrojkatRekurencja(n,k):
    if n==0 or k==n : return 1
    if k==1 or k==n-1 : return n
    else : return TrojkatRekurencja(n-1,k)+TrojkatRekurencja(n-1,k-1)

k=int(input("Podaj ilosc wierszy"))
numerWierasza=0
for x in TrojkatPascala(k) :
    print(str(numerWierasza)+".",end="")
    numerWierasza+=1
    for y in range(int(k/2)) :
        print("  ",end="")
    k-=1
    print(*x,sep=" ")

for x in range(k):
    print(TrojkatRekurencja(k,x))