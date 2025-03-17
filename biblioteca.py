class biblioteca:
    def __init__ (self):
        self.livros = []
    
    def add_livro(self, titulo : str, unidades : int):
        self.livros.append({'livro': titulo, 'unidades': unidades})
    
    def remove_livro(self, titulo: str):
        for l in self. titulo:
            if l['livro'] == titulo:
                self.livros.remove(l)
                return True
        return False

    def verifica_livro(self, titulo : str):
        for l in self.livros:
            if l['livro'] == titulo:
                return l['unidades']
        return 0

    def emprestimo(self, titulo : str, unidades : int):
        for l in self.livros:
            if l['livro'] == titulo:
                if l['unidades'] < unidades:
                    return False
                l['unidades'] -= unidades
                return True
        return False
    
    def devolucao(self, titulo : str, unidades : int):
        for l in self.livros:
            if l['livro'] == titulo:
                l['unidades'] += unidades
                return True
        return False