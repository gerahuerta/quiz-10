def findThrees(m):
    sum = 0
    for p in m:
        if(p % 3 == 0):
            sum = sum + p
    return sum

l = []
print ("Pon stop para parar el programa")
n = (input("Dame un numero: "))
while (n!="stop"):
    l+= [int(n)]
    n = (input("Pon otro numero: "))
print(findThrees(l))
