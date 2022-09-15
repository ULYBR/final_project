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


sair = False
while not sair:
    op = input(str('Digite o nome do filme:'))

    if op == 'sair':
        sair = True
    else:
        dicionario = requisicao(op)
        if dicionario['Response'] == 'True':
            print('Titulo: ' + dicionario['Title'])
            print('Ano: ' + dicionario['Year'])
            print('Genero: ' + dicionario['Genre'])
            print('Diretor: ' + dicionario['Director'])
            print('Nota: ' + dicionario['imdbRating'])
            print('\ndigite sair para sair da aplicação!')

        else:
            print('Filme não encontrado')
