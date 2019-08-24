print('FONDA LA SABROSONA') ;
print("------------------\n")

cliente = input("Cliente: ")

menu ={'1.Mondongo':'1.50$ \n',
         '2.Lengua': '0.75$',
         '3.Pato': '2.00$',
         'bebidas': ['Jugos' , 'Agua' ,'Sodas'] }
print(menu)
while True:
    try:
        opcion = int(input("Opcion: "))
    except:
        opcion = -1

    if opcion == 1:
        precio = 1.5
        comida = "mondongo"
        break
    elif opcion == 2:
        precio = 0.75
        comida = "lengua"
        break
    elif opcion == 3:
        precio = 2.0
        comida = "pata"
        break
    else:
        print("Opcion invalida")

        total = precio * 1.07
