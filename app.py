def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3 ) / 3

print("===sistema de notas do aluno===")
n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
n3 = float(input("digite a terceira nota"))
media = calcular_media(n1, n2, n3)
print(f"A media final é: {media:.2f}")

if media >= 7.0:
    print("status: aprovado!")
else:
    print("status: reprovado")
