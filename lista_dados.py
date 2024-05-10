lista_dados = ['andrews','alice','enzos']

for i in lista_dados:
    nova_lista = []
    nova_lista.append(i)
    dados=tuple(nova_lista)
    print(dados)    

def dados_lista():
    dados = []
    for i in range(0,100):
        dados.append(i)
    return dados

lista = dados_lista()
print(lista)

def inserir_dados_dict():
    dicio = {'ola'}
    for i in range(0,10):
        dicio.add('aprendendo a programar')
        i+= i
    return i

dicionario_dados = inserir_dados_dict()
print(dicionario_dados)

