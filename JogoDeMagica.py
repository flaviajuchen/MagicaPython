a = ["A1","A2","A3","A4","A5","A6","A7"]
b = ["B1","B2","B3","B4","B5","B6","B7"]
c = ["C1","C2","C3","C4","C5","C6","C7"]
lista = []
for i in range(7):
    print(a[i],b[i],c[i])

escolhido = input("Escolha uma das colunas acima: ")

if(escolhido == "a"):
    lista = ( b + a + c)
elif(escolhido == "b"):
    lista = (a + b + c)
else: 
    lista = (a + c + b)

lista_a = []
lista_b = []
lista_c = []

contador = 0
for i in range(7):
    lista_a.append(lista[contador])
    contador +=1
    lista_b.append(lista[contador])
    contador += 1
    lista_c.append(lista[contador])
    contador += 1  

for n in range(7):
    print(lista_a[n], lista_b[n], lista_c[n])

lista1 = []
escolhido1 = input("Escolha uma das colunas acima: ")

if(escolhido1 == "a"):
    lista1 = ( lista_b + lista_a + lista_c)
elif(escolhido1 == "b"):
    lista1 = (lista_a + lista_b + lista_c)
else: 
    lista1 = (lista_a + lista_c + lista_b)

listaA = []
listaB = []
listaC = []

contador1 = 0
for n in range(7):
    listaA.append(lista1[contador1])
    contador1 +=1
    listaB.append(lista1[contador1])
    contador1 += 1
    listaC.append(lista1[contador1])
    contador1 += 1  

for j in range(7):
    print(listaA[j], listaB[j], listaC[j])

escolhido2 = input("Escolha uma das colunas acima: ")
lista2 = []
if(escolhido2 == "a"):
    lista2 = ( listaB + listaA + listaC)
elif(escolhido2 == "b"):
    lista2 = (listaA + listaB + listaC)
else: 
    lista2 = (listaA + listaC + listaB)

print("O Elemento escolhido foi ", lista2[10])