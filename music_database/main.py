import json
import os

# Abrir arquivo json, caso o arquivo não exista, o algoritmo deverá criar um.

try: #Tenta ler um arquivo, caso o arquivo esteja vazio, adicionar um dicionario vazio ao arquivo.
    with open('database.json', 'r+') as data:
        if not data.read():
            data.write("{}")

except FileNotFoundError: #Caso o arquivo não exista, criar um e adicionar um dicionario vazio ao mesmo.
    print('Arquivo de Database não existe, portanto será criado...')
    with open('database.json', 'w+') as data:
        data.write('{}')
        print('...')
        print('Arquivo de Database criado com sucesso')

# Abertura do arquivo json, passamos a interagir com ele, através da variavel "dicionario".
os.system('cls')
with open('database.json', 'r') as data:
    dicionario = json.load(data)
    #Menu com opções definidas na lista "escolhas_possiveis", o menu está dentro de um "while True",
    #onde o laço só é quebrado ao escolher a opção "Sair, assim fechando o programa"
    while True:
        print('Database de Músicas')
    
        escolhas_possiveis = ['Exibir artistas', 'Exibir álbuns', 'Exibir Músicas', 'Adicionar', 'Sair']
        for i, opcao in enumerate(escolhas_possiveis):
            print(f'{i+1} - {opcao}')
        try:
            escolha_menu=int(input('> '))
            match escolha_menu:
                case 1:
                    os.system('cls')
                    # Listar Artistas contidos no arquivo json
                    print('--- Artistas ---')
                    for key in dicionario.keys():
                        print(key.capitalize())
                    print('')
                case 2:
                    os.system('cls')
                    # Listar Álbuns contidos no arquivo json
                    print('--- Álbuns ---')
                    for key in dicionario.keys():
                        lista_albuns=[album for album in dicionario[key]["albuns"].keys()]
                        print(*lista_albuns, sep='\n')
                    print('')

                case 3:
                    # Listar Músicas contidos no arquivo json
                    os.system('cls')
                    print('--- Músicas ---')
                    for key in dicionario.keys():
                        lista_musicas=[musica for album in dicionario[key]["albuns"].values() for musica in album["musicas"]]
                        print(*lista_musicas, sep='\n')
                    print('')
                
                case 4:
                    os.system('cls')
                    escolhas_add=['Adicionar Artista', 'Adicionar Álbum para um Artista existente', 'Adicionar Músicar em um Álbum existente', 'Voltar para o Menu Principal']
                    while True:
                        for i, escolha in enumerate(escolhas_add):
                            print(f'{i+1} - {escolha}')
                        escolha_menu_add=(int(input('> ')))
                        match escolha_menu_add:
                            case 1:
                                os.system('cls')
                                print('Digite o nome do Artista que deve ser adicionado')
                                nome = input(str('> '))
                                novo_artista={nome.upper():{"artista": nome.capitalize()}}
                                os.system('cls')
                                print(f'{nome.capitalize()} adicionado com sucesso')
                                print('')

                                with open("database.json", "r+") as data:
                                    dicionario = json. load(data)
                                    dicionario. update(novo_artista)
                                    data.seek(0)
                                    json.dump(dicionario, data, indent=4)
                            
                            case 2:
                                os.system('cls')
                                with open('database.json', 'r') as data:
                                    dicionario = json.load(data)
                                    print('--- Escolha o Artista ---')
                                    lista_artistas=[f'{i+1} - {artista.capitalize()}' for i,  artista in enumerate(dicionario.keys())]
                                    print(*lista_artistas, sep='\n')
                                    escolha_artista = int(input('> '))
                                    print(f'{list(dicionario.keys())[escolha_artista-1]} selecionado')

                            
                            case 3:
                                os.system('cls')
                                pass

                            case 4:
                                os.system('cls')
                                break


                case 5:
                    # encerrar o programa
                    os.system('cls')
                    print('Saindo')
                    break
                    
                case _:
                    os.system('cls')
                    print('Valor Invalido, item não está presente no menu')
        except:
            os.system('cls')
            print('Digite apenas números inteiros')

    