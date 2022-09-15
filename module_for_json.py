import json

# Funções relacionadas ao json
def lendo_filmes_json():  # return data
    f = open('imdb_top_1000.json', encoding= 'utf-8')  # Opening JSON file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()
    return data


def salvando_filmes_json(data):
    with open('imdb_top_1000.json', "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    print('Você salvou seu arquivo json')


def lendo_users_json():
    f = open('users.json', encoding= 'utf-8')  # Opening JSON file
    data_users = json.load(f)  # returns JSON object as a dictionary
    f.close()
    return data_users


def salvando_users_json(data):
    with open('users.json', "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    print('Você salvou seu arquivo json')