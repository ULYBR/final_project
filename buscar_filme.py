# fazer um gerenciador de pesquisar pelo arquivo json
import json
import requests
req = None
def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=139d06c0')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro ao conectar com o servidor')
        exit()
        return None


def detalhe_filme(filme):
    print('Titulo: ' + filme['Title'])
    print('Ano: ' + filme['Year'])
    print('Genero: ' + filme['Genre'])
    print('Diretor: ' + filme['Director'])
    print('Nota: ' + filme['imdbRating'])
    print('\ndigite sair para sair da aplicação!')
    print('')


sair = False
while not sair:
    op = input(str('Digite o nome do filme:'))

    if op == 'sair':
        sair = True
    else:
        filme = requisicao(op)

        if filme['Response'] == False:
            print('Filme não encontrado')
        else:
            detalhe_filme(filme)
