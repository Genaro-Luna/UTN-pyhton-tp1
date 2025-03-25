print("Hola mundo!")


nombre = input("Ingrese nombre: ")
print(f"Hola {nombre}")


nombre_completo = input("Ingrese nombre completo: ")
edad = input("Ingrese edad: ")
localidad = input("Ingrese localidad: ")
print(f"Soy {nombre_completo} tengo {edad} años y vivo en {localidad}")


pi = 3.14
radio = int(input("Ingrese radio del circulo: "))
area = radio**2 * pi
print(f"El area es {area}")


segundos = int(input("Ingrese segundos:"))
horas = segundos/60
print(f"Cantidad de horas equiivalentes: {horas}")


numero = int(input("Ingrese numero"))
i = 0
while i <= 10:
    print(numero * i)
    i += 1

  
num2 = int(input("Ingrese num1"))
num1 = int(input("Ingrese num2"))
if (num1 > 0) & (num2 > 0):
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    print(f"Resultados de la suma: {suma} || Resta: {resta} || Multiplicacion {mult} || Division {div}")
 
   
masa = int(input("Ingrese peso:"))
alt = float(input("Ingrese altura:"))
imc = masa/alt**2
print(f"IMC: {imc}")


celsius = float(input("Ingrese temperatuira en celsius:"))
fahrenheit = (9/5) * celsius + 32
print(f"Temperatura en fahrenheit {fahrenheit}")


num1 = float(input("Ingrese numero 1"))
num2 = float(input("Ingrese numero 2"))
num3 = float(input("Ingrese numero 3"))
promedio = (num1 + num2 + num3)/3
print(f"El promedio es: {promedio}")

print("FIN")