import json
filename = 'jsonDB.json'

def openFile():
    with open(filename, 'w+') as f:
        f.write('{}')            
        f.close

openFile()


# lista_musica=[]
# def listar_musicas(indice):
#   contador =0
#   while contador != (len(data[indice]["albuns"].keys())):
#     lista_musica.extend(list(data[indice]["albuns"].values())[contador]["musicas"])
#     contador = contador +1
#   print(*lista_musica, sep='\n')