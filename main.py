exercises=int(input("Ingrese el número del ejercicio que desee ejecutar: "))
if exercises==1:
    #Calcular el area de un triangulo
    Base=int(input("Ingrese la base del triangulo: "))
    height=int(input("Ingrese la altura del triangulo: "))
    Area=Base*height/2
    print("El area del triangulo es: ",Area)
elif exercises==2:
    #Suma de dos números
    first=int(input("Ingrese un número: "))
    second=int(input("Ingrese otro número: "))
    sum=first+second
    print("La suma de los 2 números es: ",sum)
elif exercises==3:
    #El cuadrado de un numero
    Number=int(input("Ingrese un número: "))
    Square=Number*Number
    print("El cuadrado del numero es: ",Square)
elif exercises==4:
    #Suma de 1234 y 532
    number1=1234
    number2=532
    sum=number1+number2
    print("La suma de 1234 + 532 es: ",sum)
elif exercises==5:
    #restar entre 1234 y 532
    number1=1234
    number2=532
    subtract=number1-number2
    print("el resultado de la resta: 1234 - 532 es: ",subtract)
elif exercises==6:
      #Multiplicación entre 1234 y 532
    number1=1234
    number2=532
    multiplication=number1*number2
    print("el resultado de la multiplicacion: 1234 x 532 es: ",multiplication)
elif exercises==7:
    #División entre 1234 y 532
    number1=1234
    number2=532
    Division=number1/number2
    print("El resultado de la división: 1234 / 532 es: ",Division)
elif exercises==8:
    #Modulo de 1234 entre 532
    Number1=1234
    Number2=532
    Module=Number1%Number2
    print("El Módulo de 1234 entre 532 es: ",Module)
elif exercises==9:
    #Conversion de euros a dolares
    Euro=float(input("Ingrese el euro: "))
    Conversion=Euro*1.10
    print("en dolares que es igual a: ",Conversion)
elif exercises==10:
    #Área de un rectángulo
    Broad=float(input("Ingrese el ancho del rectángulo: "))
    Height=float(input("Ingrese la altura del rectángulo: "))
    Area=Broad*Height
    print("El area del rectangulo es: ",Area)
elif exercises==11:
    #área y perímetro de un cuadrado
    Side=int(input("Ingrese el lado del cuadrado: "))
    #Área
    Area=Side*Side
    print("El area del cuadrado es: ",Area)
    #Perimetro
    Perimeter=Side*4
    print("El perímetro del cuadrado es: ",Perimeter)
elif exercises==12:
    #Área y volumen de un cilindro
    Radius=int(input("Ingrese el radio: "))
    Height=int(input("Ingrese la altura: "))
    #Área
    area=2*3.1416*Radius*(Radius+Height)
    print("el area del cilindro es: ",area)
    #Volumen
    Volume=3.1416*Radius*Radius*Height
    print("El volumen del cilindro es: ",Volume)
elif exercises==13:
    #Área y longitud de un círculo
    Radius=int(input("Ingrese el radio del círculo: "))
    #Longitud
    Length=2*3.1415926536*Radius
    print("La longitud del circulo es: ",Length)
    #Area
    Area=3.1415926536*Radius*Radius
    print("El area del circulo es: ",Area)
elif exercises==14:
    #promedio de tres números
    number1=int(input("Ingrese el primer número: "))
    number2=int(input("Ingrese el segundo numero: "))
    number3=int(input("Ingrese el tercer número: "))
    Average=(number1+number2+number3)/3
    print("La media de los tres números es: ",Average)