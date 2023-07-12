import re

## Função Search neses exemplos
## Esse para procular um telefone
print("Essa é o codigo que utiliza a função search em expressões regulares (procura telefone na frase)")
print()
telefone = input("Qual a frase ou texto na que deeja aplicar a função: ")
print("=-" *50)
telefone_verrificado = re.search("\(\d{2}\)\d{4,5}-\d{4}", telefone)

if telefone_verrificado:
    print("A placa encontrado é: ", telefone_verrificado)
else:
    print("Não foi encontrado nenhuma placa.")


## Esse para procurar uma placa de carro
print()
print("Essa é o codigo que utiliza a função search em expressões regulares (procura placa de carro na frase)")
print()
placa = input("Qual a frase ou texto na que deeja aplicar a função: ")
print("=-" *50)
placa_verrificado = re.search("[A-Za-z]{3}-\d{4}", placa)

if placa_verrificado:
    print("A placa encontrado é: ", placa_verrificado)
else:
    print("Não foi encontrado nenhuma placa.")


## Esse para procurar um E-mail
print()
print("Essa é o codigo que utiliza a função search em expressões regulares (procura email na frase)")
print()
email = input("Qual a frase ou texto na que deeja aplicar a função: ")
print("=-" *50)
email_verrificado = re.search("\w+@\w+\.com", email)

if email_verrificado:
    print("O email encontrado é: ", email_verrificado)
else:
    print("Não foi encontrado nenhum email.")