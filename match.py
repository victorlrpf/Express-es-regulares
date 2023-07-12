import re

## Essa é a função match,
## Só usarei um exemplo onde pegamos qualqeur texto e vamos passar para ele encontrar determindada expressão

print("Essa é a errada")
frase_erro = "A placa do carro que eu anotei no assalto foi FTR-2020"
frase_erro_verrificado = re.match("[A-Za-z]{3}-\d{4}", frase_erro)

if frase_erro_verrificado:
    print("Quando está no início da frase, o match mostra esse resultado:", frase_erro_verrificado)
else:
    print("Quando está no início da frase, nenhuma correspondência encontrada.")

print("-=" *30)
print("Essa é a correta")
frase_certa = "FRT-2020 foi a placa que eu anotei no assalto"
frase_certa_verrificado = re.match("[A-Za-z]{3}-\d{4}", frase_certa)

if frase_certa_verrificado:
    print("Quando está no início da frase, o match mostra esse resultado:", frase_certa_verrificado)
else:
    print("Quando está no início da frase, nenhuma correspondência encontrada.")