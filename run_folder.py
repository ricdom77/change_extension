from os import walk, path, rename


# r'C:\Users\ricad\Downloads\Profissão Desenvolvedor Full Stack Python'

main_folder = input('Insira o caminho completo da pasta a ser percorrida >> ')
add_extension = input('Insira qual extensão deve ser incluída >> ')

if main_folder == '':
    print('Impossível de prosseguir... entre com um path válido!')
else:
    contador = 0
    for diretorio, subpasta, arquivos in walk(main_folder):
        for arquivo in arquivos:
            if '.' not in arquivo[-4:]:
                arq = path.join(diretorio, arquivo)
                novoArq = f'{arq}.{add_extension}'
                rename(arq, novoArq)
                contador += 1
    print(f'{contador} arquivos foram identificados e alterados!')