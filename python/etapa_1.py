'''Crea un script que pida lo siguiente
1. pide al usuario su nombre, edad y peso en kilogramos
2. calcula y muestre en que año cumpliria 100 años
3. convierta el peso en libras(1 kg = 2.20462 lb) y muestralo
4. indique con un msj si es mayor o menor '''

print("Bienvenido a la cauculadora de datos personales")
print("Por favor complete los siguientes campos")
nombre = input("Ingrese su nombre completo: ")

edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kg: "))
año = int(input("Ingrese el año actual: "))

print(f"Aqui te dejo un resumen {nombre}")
print(f"En el año {(100 - edad) + año} cumplirias 100 años")
print(f"Tu peso en libras es de {peso * 2.20462:.2f} lbs")
if edad < 18:
    print(f"Tienes {edad} años, eres menor")
else:
    print(f"Tienes {edad} años, eres mayor")