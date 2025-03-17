from usuario import usuario, Status, biblioteca

op = 0

def aguardar():
    input("Pressione enter para continuar")
    for i in range(50):
        print()

while op != 5:

    print("Seja bem vindo a biblioteca, o que deseja fazer?")
    print("1 - Login")
    print("2 - cadastro")
    print("5 - Sair")

    op = int(input())

    if op == 5:
        print("Até mais!")
        break
    
    if op == 2:
        print("Digite o usuário e senha para cadastro:")
        user = input("Usuário: ")
        password = input("Senha: ")
        user = usuario(user, password)
        if(user.login() == Status.BLOQUEADO):
            print("Usuário bloqueado!\nfavor entrar em contato com a administração\n")
            continue
        elif(user.login()['status'] == Status.INATIVO):
            user.status = Status.ATIVO
            print("Usuário reativado!\n")
    
    while True:
        print("Bem vindo, {}!".format(user.user))
        print("O que deseja fazer?")
        print("1 - Verificar livros disponíveis")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Logout")
        print("5 - Sair")
        op = int(input())

        if op == 5:
            print("Até mais!")
            break
        
        elif op == 1:
            print("Livros disponíveis:")
            for l in biblioteca.livros:
                s = l['livro'] + " - " + str(l['unidades'])
                if(l['unidades'] == 0):
                    s += " -- Livro indisponível"
                print(s)
            print()
            aguardar()
        elif op == 2:
            print("Digite o nome do livro e a quantidade que deseja emprestar:")
            livro = input("Livro: ")
            quantidade = int(input("Quantidade: "))
            if(quantidade < 1):
                print("Quantidade inválida")
                continue
            if(user.emprestimo(livro, quantidade)):
                print("Livro emprestado com sucesso!")
                continue
            print("Não foi possível emprestar o livro")
        elif op == 3:
            livro = input("Livro: ")
            quantidade = int(input("Quantidade: "))
            if(quantidade < 1):
                print("Quantidade inválida")
                continue
            if(user.emprestimo(livro, quantidade)):
                if(user.status == Status.BLOQUEADO):
                    print("Livro devolvido com atraso, usuário bloqueado!")
                    continue
                print("Livro devolvido com sucesso!")
                continue
            print("Não foi possível devolver o livro")
        elif op == 4:
            print("Até mais!")
            break