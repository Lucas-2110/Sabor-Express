#Função "os" é usada para apagar as informações do console
import os

restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Pizza', 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana', 'ativo' : False}]

def exibir_nome_programa():
    '''Essa função exibe o nome dos programa'''
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    '''Essa função exibe as opções para selecionar no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar o estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função apresenta a mensagem de finalização do app'''
    exibir_subtitulo('Encerrando o app!')

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao menu principal, com o usuário digitando uma tecla
    
    Input:
    - Digite uma tecla para voltar ao menu principal

    Output:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Essa função é responsável por mostar se a opção é inválida
    
    Output:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir os subtítulos'''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_de_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o a categoria do restaurante {nome_de_restaurante}: ')
    dados_restaurante = {'nome' :nome_de_restaurante, 'categoria' :categoria, 'ativo' :False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante, {nome_de_restaurante}, foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes que estão na lista
    
    Output:
    - Exibe a lista de restaurante na tela
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def altenar_estado_restaurante():
    '''Essa função altera o status do restaurante entre ativado e desativado
    
    Output:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurantes['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f' o restaurante foi {nome_restaurante}, foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante}, foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função solicita que o usuário solicite uma opção
    
    Output:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            altenar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    '''Essa função é a função principal, que inicia o programa'''
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
