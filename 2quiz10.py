def dotproduct(lista1,lista2):
    z = 0
    for (a,b) in zip(lista1,lista2):
        z = z + (a*b)
    return z

lista=[1,2,3,4,5]
lista1=[1,2,3,4]
lista2=[2,4,5,6]
print(dotproduct(lista1,lista2))        
