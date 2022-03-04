mascotas=['gatos','perros','Loros','peces']

result= len(mascotas)

m0= mascotas[0]
m2=mascotas[2]

print(result)
print (m2)


for index, mascota in enumerate (mascotas):
    print(index,mascota)

posicion_peces=0
for index, mascota in enumerate (mascotas):
    if mascota=="peces":
        posicion_peces=index

print ("Se encontró un pez en la posicion:", posicion_peces)