import json

# Projeto de gerenciamneto de reviews de filmes.

usuario_ativo = 'nao'

# Funções do menu
def menu_login():

    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'Realizar login (Escreva 1)\n' #Feito
                              f'Criar uma conta (Escreva 2)\n'
                              f'Fechar (Escreva 3)\n'
                              f'o----------------------------------------------------------o\n' #Feito
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 3:
            rodando_menu = False
            if opcao_seguida == 1:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                usuario_ativo = login()
                if usuario_ativo['admin']:
                    return menu_adm()
                else:
                    return menu_user()

            if opcao_seguida == 2:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                adm.create_account()
                return menu_login()

            if opcao_seguida == 3:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                continue

            return opcao_seguida
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 3\n')
def menu_user():
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'Buscar um filme (Escreva 1)\n'
                              f'Editar review para um filme (Escreva 2)\n'
                              f'Consultar overview (Escreva 3)\n'
                              f'Sair (Escreva 4)\n'
                              f'o----------------------------------------------------------o\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 5:
            rodando_menu = False

            if opcao_seguida == 1:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                imprimir_filme(consultando_filme())
                return menu_user()

            if opcao_seguida == 2:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                editando_filme(consultando_filme())
                return menu_user()

            if opcao_seguida == 3:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                imprimir_overview_filme(consultando_filme())
                return menu_user()

            if opcao_seguida == 4:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                return menu_login()

        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 5\n')
def menu_adm():
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'Buscar um usuário (Escreva 1)\n'
                              f'Deletar um usuário (Escreva 2)\n'
                              f'Adicionar um usuário (Escreva 3)\n'
                              f'Sair (Escreva 4)\n'
                              f'o----------------------------------------------------------o\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 4:
            rodando_menu = False
            if opcao_seguida == 1:
                buscar_usuario()
                return menu_adm()

            if opcao_seguida == 2:
                adm.delete_user()
                return menu_adm()

            if opcao_seguida == 3:
                adm.create_account()
                return menu_adm()

            if opcao_seguida == 4:
                return menu_login()

        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 4\n')


# Classes
class usuario:
    def __init__(self, name, senha, id, movies_reviewed):
        self._name = name
        self._id = id
        self._movies_reviewed = movies_reviewed
        self._senha = senha
class adm(usuario):
    def print_funcionarios(data_users):
        print(data_users)

    @staticmethod
    def delete_user():
        usuarios_cadastrados = lendo_users_json()
        passou_checagem = True
        print(f'Os usuários cadastrados são: \n')
        for lista_de_usuarios in usuarios_cadastrados:
            print(lista_de_usuarios['Name'])
        usuario = input(f'Digite o usuário que deseja deletar: ')

        for i in range(len(usuarios_cadastrados)):
            if usuario == usuarios_cadastrados[i]['Name']:
                del usuarios_cadastrados[i]
                salvando_users_json(usuarios_cadastrados)
                print(f'usuário deletado')
                break

    @staticmethod
    def create_account():  # return usuario  #usuario_ativo = login()
        usuario = input(f'Digite seu usuário: ')
        usuarios_cadastrados = lendo_users_json()
        passou_checagem = True
        for lista_de_usuarios in usuarios_cadastrados:
            if usuario == lista_de_usuarios['Name']:
                passou_checagem = False

        if passou_checagem:
            novo_usuario = {"Name": usuario,
                            "ID": (len(usuarios_cadastrados) + 1),
                            "movies_reviewed": [],
                            "admin": False}

            usuarios_cadastrados.append(novo_usuario)
            salvando_users_json(usuarios_cadastrados)
        else:
            print(f'usuário já cadastrado')

# Funções relacionadas ao login
def login():  # return usuario  #usuario_ativo = login()
    usuario = input(f'Digite seu usuário: ')
    senha = input(f'Digite sua senha: ') #decorativa
    usuarios_cadastrados = lendo_users_json()
    for item_usuario in usuarios_cadastrados:
        if usuario == item_usuario['Name']:
            print(f'login realizado corretamente')

            return item_usuario
    print(f'Usuário não cadastrado')
def buscar_usuario():
    usuario = input(f'Digite o usuário para busca: ')
    usuarios_cadastrados = lendo_users_json()
    for lista_de_usuarios in usuarios_cadastrados:
        if usuario == lista_de_usuarios['Name']:
            print(f'{lista_de_usuarios}')
        else:
            print(f'Usuário não cadastrado')
def logout():  # usuario_ativo = 'nao' #vai para o menu_login
    usuario = 'nao'
    return menu_login()



# Funções relacionadas aos filmes
def consultando_filme():  # return opcao_seguida
    rodando_menu = True
    while rodando_menu:
        tamanho = len(data)
        opcao_seguida = input(f"Temos {tamanho} filmes disponíveis, escreva um número de 0 a {tamanho} "
                              f"para escolher o filme: ")  # TODO fazer por nome
        try:
            opcao_seguida = int(opcao_seguida) - 1
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= tamanho:
            rodando_menu = False
            return opcao_seguida
        else:
            print(f'Espera-se uma opção seguida com valor inteiro entre 1 e {tamanho}\n')
def imprimir_filme(opcao_seguida):
    titulo = data[opcao_seguida]['Series_Title']
    ano = data[opcao_seguida]['Released_Year']
    nota = data[opcao_seguida]['Metrics']['IMDB_Rating']
    director = data[opcao_seguida]['Director']
    genero = data[opcao_seguida]['Genre']
    votos = data[opcao_seguida]['Metrics']["No_of_Votes"]

    print(f'O filme escolhido é o filme {titulo}, esse é um filme de {ano}, produzido por {director}.\n'
          f'Seus generos são {genero} e sua nota no IMDB é {nota} com {votos} votos')
def imprimir_overview_filme(opcao_seguida):
    titulo = data[opcao_seguida]['Series_Title']
    overview = data[opcao_seguida]['Overview']

    print(f'Exibindo o overview para o filme {titulo}:\n'
          f'{overview}')
def editando_filme(filme_seguido):
    print('A opção edição de filme foi escolhida')
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'titulo (Escreva 1)\n'
                              f'Ano (Escreva 2)\n'
                              f'Nota (Escreva 3)\n'
                              f'Diretor (Escreva 4)\n'
                              f'Genero (Escreva 5)\n'
                              f'Número de votos (Escreva 6)\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 6:
            rodando_menu = False
            if opcao_seguida == 1:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                data[filme_seguido]['Series_Title'] = input(f'Digite o novo Título')

            if opcao_seguida == 2:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                data[filme_seguido]['Released_Year'] = input(f'Digite o novo Ano')

            if opcao_seguida == 3:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                data[filme_seguido]['Metrics']['IMDB_Rating'] = input(f'Digite a nova nota')

            if opcao_seguida == 4:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                data[filme_seguido]['Director'] = input(f'Digite o novo Diretor')

            if opcao_seguida == 5:  # Salvar de uma lista para um JSON os grupos de trabalho (Escreva 5)
                data[filme_seguido]['Genre'] = input(f'Digite o novo gênero')

            if opcao_seguida == 6:  # Fechar o program (Escreva 6)
                data[filme_seguido]['Metrics']["No_of_Votes"] = input(f'Digite o novo número de votos')

            imprimir_filme(filme_seguido)
            return filme_seguido
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 6\n')
def add_review(filme_seguido):
    nota = data[filme_seguido]['Metrics']['IMDB_Rating']
    n_votos = data[filme_seguido]['Metrics']["No_of_Votes"]
    titulo = data[filme_seguido]['Series_Title']

    rodando_menu = True
    while rodando_menu:
        nova_nota = input(f'Qual nota você deseja adicionar ao filme {titulo}: ')

        try:
            nova_nota = int(nova_nota)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 0 <= nova_nota <= 10:
            rodando_menu = False
            data[filme_seguido]['Metrics']['IMDB_Rating'] = (nota*n_votos/(n_votos+1) + nova_nota/(n_votos+1))
            data[filme_seguido]['Metrics']["No_of_Votes"] = n_votos + 1

            return data
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 0 e 10\n')


# Funções relacionadas ao json
def lendo_filmes_json():  # return data
    f = open('datasets/imdb_top_1000.json', encoding="utf-8")  # Opening JSON file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()
    return data
def salvando_filmes_json(data):
    with open('datasets/imdb_top_1000.json', "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    print('Você salvou seu arquivo json')
def lendo_users_json():
    f = open('datasets/users.json')  # Opening JSON file
    data_users = json.load(f)  # returns JSON object as a dictionary
    f.close()
    return data_users
def salvando_users_json(data):
    with open('datasets/users.json', "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    print('Você salvou seu arquivo json')


# TODO googlinho
# TODO dashboard





if __name__ == '__main__':

    data = lendo_filmes_json()
    menu_login()

