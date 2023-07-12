import re

email = ('''
    Essa é uma lista de E-mails para fazer a verrificação
    E-mail: teste01@gmail.com
    E-mail: teste02@icloud.com
    E-mail: teste03@hotmail.com
    E-mail: teste04@teste.com
    E-mail: teste05@corporativo.com
''')

email_verrificacao = re.findall("\w+@\w+\.\w+.?\w+", email)

if email_verrificacao:
    print("A lista de E-mail são os:", email_verrificacao)
else:
    print("Nenhum E-mail foi verrificado na lista.")