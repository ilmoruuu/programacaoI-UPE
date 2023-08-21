a, b, c = [float(valor) for valor in input().split()]
areatri = (a*c)/2
areacir = (3.14159*(c**2))
areatrap = ((a+b)*c)/2
areaquad = (b**2)
arearet = (a*b)

print(f'''TRIANGULO: {areatri:.3f}
CIRCULO: {areacir:.3f}
TRAPEZIO: {areatrap:.3f}
QUADRADO: {areaquad:.3f}
RETANGULO: {arearet:.3f}''' )