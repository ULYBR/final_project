# fazer um gerenciador de pesquisar pelo arquivo json
import json
import requests
req = None
def requisicao(titulo):

    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=139d06c0' + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro ao conectar com o servidor\n'
              'Sistema indisponível')
        exit()
        return None


def detalhe_filme(filme):
    print('Titulo: ' + filme['Title'])
    print('Ano: ' + filme['Year'])
    print('Genero: ' + filme['Genre'])
    print('Diretor: ' + filme['Director'])
    print('Nota: ' + filme['imdbRating'])
    print('Premios: ' + filme['Awards'])
    print('Poster: ' + filme['Poster'])
    print('')



sair = False
while not sair:
    op = input(str('Digite o nome do filme ou sair para sair do sistema: '))

    if op == 'sair':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)

        if filme['Response'] == 'False':
            print('\nFilme não encontrado na base de dados.\n')
        else:
            detalhe_filme(filme)
