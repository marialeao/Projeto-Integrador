class Pessoa(object):
    def __init__(self, id: int, nome: str, email: str) -> None:
        self.__id = id
        self.__nome = nome
        self.__email = email
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def json(self): 
        return { 
        "id": self.__id, 
        "nome": self.__nome, 
        "email": self.__email
        }

    #get/set menos set do id
    # pode fazer tbem o repr