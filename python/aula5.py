#Atividades aula 5


text = 'Hello World'
name = input('Digite seu nome:')

print ('{} {}'. format(text,name))
print("\n")


#1. Concatene uma cidade e um adjetivo para ela
cidade = "São Paulo é"
adjetivo = input('Digite um adjetivo para São Paulo:')

print ('{} {}'. format(cidade,adjetivo))
print("\n")


#2. Concatene uma viagem e quem vai participar dela
viagem = "Na viagem irá eu e"
participantes = input('Digite o nome de um viajante:')

print ('{} {}'. format(viagem,participantes))
print("\n")


#3. Concatene função programador seu nome ou o nome do usuário
programador = "Olá programador"
nome = input('Digite o seu nome:')
username = input('Digite o seu nome do usuário:')

print ('Seja bem-vindo', nome, 'seu username é', username)
print("\n")




#Atividade do notion
print ('🎲 | Atividade do notion')

#1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
print("O quadrado do número é:", quadrado)
print("\n")



#2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
seunome = input('Digite o seu nome:')
seusobrenome = input('Digite o seu sobrenome:')

print ('Seja bem-vindo,', seunome, seusobrenome)
print("\n")



#3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

concatenacao = str(num1) + str(num2)

print('A concatenação dos números é:', concatenacao)
print("\n")



#4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
python = "Python"
numero = input('Digite um número: ')

concat_python = python + str(numero)
print(concat_python)
print("\n")


#5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.
print('Hello...')

frase = "Hello"
final = input('Digite a palavra que completa essa sentença de programação: ')
print ('{} {}'. format(frase,final))


# Desafio: Calculadora com as saidas concatenadas
print ('🐍 | Crie uma calculadora com as saidas concatenadas')
num1 = float (input ('Digite o primeiro valor: '))
num2 = float (input ('Digite o segundo valor: '))

soma = num1 + num2
subtraçao = num1 - num2
multiplicaçao = num1 * num2
divisao = num1 / num2
divisao2 = num1 // num2
potencia = num1**num2


print("\n")
print ('Os resultados obtidos foram:')
print ('+ | O resultado da soma é {}'. format (soma))
print ('- | O resultado da subtração é {}'. format (subtraçao))
print ('× | O resultado da multiplicação é {}'. format (multiplicaçao))
print ('÷ | O resultado da divisão é {}'. format (divisao))
print ('/ | O resultado da segunda divisão é {}'. format (divisao2))
print ('^ | O resultado da potência é {}'. format (potencia))
print("\n")