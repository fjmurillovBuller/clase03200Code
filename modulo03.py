'' 'edad = int(input("Digite su edad: ")) '' '

'''
if edad < 18:
        print("Es Menor de edad!!")
elif edad >=18 and edad <60:
        print("Es Adulto: ") 
else:
        print("Es adulto Mayor:")   


if edad < 18:
        print("Es Mayor de Edad: ")
else:
        print("Es un adulto: ")

        
                           
resultado = "Es Menor de edad " if edad < 18 else "Es adulto" if edad >= 18 and edad < 30 else "Sigue siendo adulto" if edad >= 30 and edad < 40 else "Es adulto mayor"
print(resultado)        
'''
""" WHILE controlado POR CONTEO"""
'''
contador = 1000
while contador > 0:
        print("Texto", contador)
        contador -=1
'''

""" WHILE controlado por Evento """
continuar = input("Quieres continuar (SI / NO ): ")
notas = []

while continuar == "SI":
        print("Estas dentro del programa")
        notas.append(int(input("Escriba la Nota: ")))
        continuar = input("Quieres continuar (SI / NO ) :")
        
print(notas)        
        

