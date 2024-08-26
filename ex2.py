nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

soma = nota1 + nota2 + nota3 

media = soma / 3

input(f'A soma das notas do aluno é: {soma:.2f}')
input(f'A média do aluno é: {media:.2f}')

if media >= 70:
    print("Aluno aprovado!")
else:
    print("Aluno retido!")