print("=BIENVENIDO A MI CALCULAORA =")
print("SELECCIONE UNA OPCION")#seleccionar una opcion
print("1_suma")
print("2_resta")
print("3_multiplicacion")
print("4_divicion")
x=input("elige")
y=float(x)

if(y==1):#operaciones aritmeticas
    a=input("ingrese n1\n")# operacion de suma
    b = input("ingrese n2\n")
    a2=float(a)
    b2=float(b)
    resultado=a2+b2
    print("TOTAL:",resultado)
elif(y==2):#0peracion de resta
    a = input("ingrese n1\n")
    b = input("ingrese n2\n")
    a2 = float(a)
    b2 = float(b)
    resultado = a2 - b2
    print("TOTAL:", resultado)
elif(y==3):#opercionde multiplicacion
    a = input("ingrese n1\n")
    b = input("ingrese n2\n")
    a2 = float(a)
    b2 = float(b)
    resultado = a2 * b2
    print("TOTAL:", resultado)
elif (y==4):#operacion de divicion
    a = input("ingrese n1\n")
    b = input("ingrese n2\n")
    a2 = float(a)
    b2 = float(b)
    resultado = a2 / b2
    print("TOTAL:", resultado)
else:
    print("NUMERO INVALIDO")
