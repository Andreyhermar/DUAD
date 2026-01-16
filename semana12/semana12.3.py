# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
#
# 
# 
# Una herencia multiple puede usarse para compartir capacidades a las clases hijas, las cuales nos ayudan a la no repeticion de codigo dentro
# de nuestra aplicacion, pero tambien para realizar funciones muy especificas que no necesariamente van a darle capacidades a otra clase, 
# si no para realizar tareas donde ejecutan funciones muy especificas que otras funciones sin similaridades pueden necesitar.
#Ejemplos de uso:
    # Logging
    # Autenticación
    # Validaciones
    # Permisos
    # Serialización
    # Cache
    # Auditoría

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class LoggedAccount(BankAccount, LoggerMixin):
    pass

acc = LoggedAccount(100)
acc.log("Account created")