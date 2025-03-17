from enum import Enum
from datetime import datetime, timedelta
import biblioteca

class Status(Enum):
    INATIVO = 0
    ATIVO = 1
    BLOQUEADO = 2

biblioteca = biblioteca.biblioteca()

# Adicionando livros à biblioteca desse jeito apenas para exemplo
biblioteca.add_livro('Dom Casmurro', 2)
biblioteca.add_livro('O Alienista', 5)
biblioteca.add_livro('Memórias Póstumas de Brás Cubas', 0)
biblioteca.add_livro('Quincas Borba', 1)
biblioteca.add_livro('Helena', 4)

class usuario:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.emprestimos = []
        self.status = Status.ATIVO
    
    def login(self):
        #depois posso trocar por algo mais "real"
        if self.user == 'admin' and self.password == 'admin':
            return {'status': Status.ATIVO, 'tipo': 'admin'}
        
        elif self.user == 'user' and self.password == 'user':
            return {'status' : Status.ATIVO, 'tipo': 'user'}
        
        return {'status' : Status.INATIVO, 'tipo': None}

    def logout(self):
        pass

    def emprestimo(self, livro : str, unidades : int):
        #tentar fazer algo com banco de dados, não sei ainda
        
        if biblioteca.verifica_livro(livro) < unidades:
            return False
        if self.user.status == Status.BLOQUEADO:
            return False
        
        biblioteca.emprestimo(livro, unidades)
        data_datetime = datetime.now() + timedelta(days=14)
        data = data_datetime.strftime('%d/%m/%Y')
        self.emprestimos.append({'livro': livro, 'data devolução': data})
        return True
    
    def devolucao(self, livro : str, unidades : int):
        for emp in self.emprestimos:
            if emp['livro'] == livro:
                if(emp['data devolução'] < datetime.now().strftime('%d/%m/%Y')):
                    self.user.status = Status.BLOQUEADO

                biblioteca.devolucao(livro, unidades)
                self.emprestimos.remove(emp)
                return True
        return False