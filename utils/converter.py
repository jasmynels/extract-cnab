import json


def convert_cnab():

    file = open("files_up/CNAB.txt", "r")
    file.seek(0)
    lista_antiga = file.readlines()
    nova_lista = list()

    for object in lista_antiga:
        dictionary = {
            "type": object[0],
            "date": f"{object[1:5]}-{object[5:7]}-{object[7:9]}",
            "value": int(object[9:19])/100,
            "cpf": object[19:30],
            "card": object[30:42],
            "hour": f"{object[1:5]}-{object[5:7]}-{object[7:9]} {object[42:44]}:{object[44:46]}:{object[46:48]}",
            "store_own": object[48:62].strip(),
            "store_name": object[62:81].strip(),
        }
        nova_lista.append(dictionary)
    file.close()

    with open("files_up/CNAB.json", "w") as write_file:
        json.dump(nova_lista, write_file, indent=4, ensure_ascii=False)


def read_cnab():
    with open("files_up/CNAB.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
