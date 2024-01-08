import os 

restaurantes = [ {'nome':'Assado','categoria':'Carnes','ativo':False},
                {'nome':'Praca','categoria':'Japones','ativo':False},
                {'nome':'PizzaSuprema','categoria': 'italiana','ativo':True}]

def exibir_nome_do_programa():  
    print('Flavor Express\n')

def exibir_opcoes():
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Alternar estado do Restaurante')
    print('4.Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    ''' Essa funcao retorna ao menu principal'''
    input('digite uma tecla para voltar para o menu principal')
    main()

def opcao_invalida():

    print('Opcao invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

    

def cadastrar_novo_restaurante():
    '''Essa funcao e responsavel por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja: ')
    categoria = input(f'digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante,
    'categoria':categoria, 'ativo':False
    }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    ''' Essa funcao lista os restaurantes, sua categoria e se esta ativo ou nao'''
    exibir_subtitulo('Listar restaurantes')
    print(f'{'Nome do restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' -  {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
    
def alternar_estado_restaurante():
    ''' Essa funcao alterna entre um restaurante ativo ou desativado'''
    exibir_subtitulo('alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

        


   
   
   
    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()