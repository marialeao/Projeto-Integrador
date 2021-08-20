from pessoa import Pessoa

class Tarefa(object):
    
    def __init__(self, id: int, descricao: str, realizada: bool, data_execucao: str, pessoa: Pessoa) -> None:
        self.__id = id
        self.__descricao = descricao
        self.__realizada = realizada
        self.__data_execucao = data_execucao
        self.__pessoa = pessoa

    def get_id(self) -> int:
        return self.__id

    def set_descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def get_descricao(self) -> str:
        return self.__descricao

    def set_realizada(self, realizada: bool) -> None:
        self.__realizada = realizada
    
    def get_realizada(self) -> bool:
        return self.__realizada

    def set_data_execucao(self, data_execucao: str) -> None:
        self.__data_execucao = data_execucao

    def get_data_execucao(self) -> str:
        return self.__data_execucao

    def __repr__(self) -> str:
        return "Tarefa -> {0} - {1} - {2} - {3} {4}".format(self.__id, self.__descricao, self.__data_execucao, "Sim" if self.__realizada else "Não", self.__pessoa.get_nome())

    def json(self): 
        return {
        "id": self.__id, 
        "descricao": self.__descricao, 
        "realizada": self.__realizada, 
        "data_execucao": self.__data_execucao,
        "pessoa.id": self.__pessoa.get_id(),
        "pessoa.nome": self.__pessoa.get_nome(),
        "pessoa.email": self.__pessoa.get_email()
        }

pessoa = Pessoa(1, "Maria Eduarda", "dudaleiteleao@gmail.com")
tarefa = Tarefa(10, "prova de programação", True, "22/10/2021", pessoa)
print(repr(tarefa))
print(pessoa.json())
print(tarefa.json())