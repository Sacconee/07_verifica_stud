import Robot from robot.py 

class Componente(codice: str, nome: str, peso_kg: float):
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self.codice = codice
        self.nome = nome
        self.peso_kg = peso_kg
        
    def set_codice(self, nuovo_codice):
        if nuovo_codice:
            self.codice = nuovo_codice
        else print("errore - il codice inserito non esiste")
        
        def get_codice(self):
        return self.codice
        
        
    def set_nome(self, nuovo_nome):
        if nuovo_nome:
            self.nome = nuovo_nome
        else print("errore - il nome inserito non esiste")
        
         def get_nome(self):
        return self.nome
        
        
    def set_peso(self, nuovo_peso):
        if nuovo_peso > 0.0:
            self.peso = nuovo_peso
        else print("errore - il peso deve essere maggiore di zero")
        
    def get_peso(self):
        return self.peso