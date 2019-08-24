if __name__ == '__main__':
    print(" Bienvenido")
    print(" ----------")
    nombre = input(" ingrese su nombre:")
    import re

    placa = input(" placa a validar: ")

if re.match("PANAMA\s[0-9]|[A-Z]\s2019|2018+", placa):

 print("***PLACA VALIDA***\nSu tipo de placa es:\n-placa particular")

elif re.match("PANAMA\s[0-9]|[A-Z]\sPROPIEDAD DEL ESTADO\s2019|2018+", placa):

 print("***PLACA VALIDA***\nsu tipo de placa es: \n-OFICIAL VEHICULOS ESTATALES")

elif re.match("PANAMA\s[[MB]0-9]|[A-Z]\s2019|2018+", placa):

 print("***PLACA VALIDA***\nsu tipo de placa es: \n-PLACA DE metro bus")

elif re.match("TAXI\s[t][0-9]|[A-Z]\s2019|2018", placa):

 print("***PLACA VALIDA***\nsu tipo de placa es: \n-PLACA DE TAXI")

elif re.match('AUTORIDAD DEl CANAL\s[CP][0-9]|[A-Z]\s2019|2018+', placa):

 print('***PLACA VALIDA***\nsu tipo de placa es: \n-placa del canal')

elif re.match("PANAMA\s[PR][0-9]|[A-Z]\s2019|2018+", placa):
 print("***placa valida***\nsu tipo de placa es:\n-placa de prensa")

else:
    print("***PLACA INVALIDA***")
