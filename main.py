import Component from component.py
import Robot from robot.py


class Main:
    
    def registra_robot(robot_prodotti: list[Robot], robot: Robot) -> None:
    
    
    def cerca_robot(robot_prodotti: list[Robot], codice: str) -> Robot:
        
    
    def riepilogi_robot(nome_azienda: str, robot_prodotti: list[Robot]) -> None:
        
    
    
    
    
    lista_robot = list[Robot]
    
    componente1 = Componente("braccio destro", "1234", 10,0)
    componente1 = Componente("braccio sinistro", "2345", 10,0)
    componente1 = Componente("torso", "3456", 10,0)
    componente1 = Componente("gamba destra", "4567", 10,0)
    componente1 = Componente("gamba sinistra", "5678", 10,0)
    componente1 = Componente("bacino", "6789", 10,0)
    componente1 = Componente("piede", "7891", 10,0)
    
    robot1 = Robot("1234", "Modello1", "siderurgia", 150.0, "costruito")
    robot2 = Robot("2345", "Modello2", "siderurgia", 125.0, "costruito")
    robot3 = Robot("3456", "Modello3", "meccanica", 100.0, "non costruito")
    robot4 = Robot("4567", "Modello4", "cucina", 50.0, "non costruito")
    
    