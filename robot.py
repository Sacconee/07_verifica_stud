import Component from component.py

class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str, componenti: list[Componente]) -> None.
        self.codice = codice
        self.modello = modello
        self.applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti = list[Componente]
        
    def set_codice(self, nuovo_codice):
        if nuovo_codice:
            self.codice = nuovo_codice
        else print("errore - il codice inserito non esiste")
        
    def get_codice(self):
        return self.codice
    
    
    def set_modello(self, nuovo_modello):
        if nuovo_modello:
            self.modello = nuovo_modello
        else print("errore - il modello inserito non esiste")
        
    def get_modello(self):
        return self.modello
    
    
    def set_applicazione(self, nuovo_applicazione):
        if nuovo_applicazione:
            self.applicazione = nuovo_applicazione
        else print("errore - l'applicazione inserita non esiste")
        
    def get_applicazione(self):
        return self.applicazione
    
    
    def set_peso_massimo_componenti_kg(self, nuovo_peso_massimo_componenti_kg):
        if nuovo_peso_massimo_componenti_kg > 0.0:
            self.peso_massimo_componenti_kg = nuovo_peso_massimo_componenti_kg
        else print("errore - il peso massimo inserito non è accettabile")
        
    def get_peso_massimo_componenti_kg(self):
        return self.peso_massimo_componenti_kg
    
    
    def set_stato(self, nuovo_stato):
        if nuovo_stato:
            self.stato = nuovo_stato
        else print("errore - lo stato inserito non esiste")
        
    def get_stato(self):
        return self.stato
    
    
    
    def aggiungi_componente(componente: Componenti) -> None:
        peso_totale = 0
        for componentes in componenti:
            if componente.codice = componentes.codice:
                print("errore - il codice è già presente")
                
        for componentes in componenti:
            peso_totale += componentes.peso_kg
            
        if peso_totale => peso_massimo_componenti_kg:
            print (errore - il peso massimo è stato superato)
        else componenti.append(componente)
        
        
    def peso_componenti -> float:
        peso_totale = 0
        for componentes in componenti:
            peso_totale += componentes.peso_kg
            
        return peso_totale
    
    def cerca_componente(codice_ricerca: str) -> Componente
        for componentes in componenti:
            if componentes.codice = codice_ricerca:
                return componentes
            
        return None
        
        
    def rimuovi_componente(codice: str) -> componente:
        for componentes in componenti:
            if componentes.codice = codice_ricerca:
                componenti.del(componentes)
                return componentes
        
        return None
    
    
    def componenti_sotto_peso(peso_massimo: float) -> list[Componente]:
        for componentes in componenti:
            if componentes.peso_kg <= peso_massimo:
                list.append(componentes)
                
        return list