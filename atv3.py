a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triangulo = (a*c)/2
circulo = pi*c**2
trapezio = ((a+b)*c)/2
quadrado = b*b
retangulo = a*b

#.3f é para imprimir apenas 3 casas decimais após a vírgula
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))
