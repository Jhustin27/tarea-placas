def calcular_area(lado):
    area = lado * lado
    return area
def saludar ():
    print("Bienvenido Sr.Cuadrado")

if __name__=="__main__":
    print("Bienvenido Sr. Cuadrado")
    lado = float(input("Lado: "))
    resultado = calcular_area(lado)
    print(resultado)
