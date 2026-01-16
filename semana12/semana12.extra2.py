# 2. Cree una clase abstracta `User` con los siguientes métodos abstractos:
#     - `get_role()`
#     - `has_permission(permission)`
# - Luego cree dos clases que hereden de ella:
#     - `AdminUser`
#     - `RegularUser`
# - Cada una debe implementar los métodos
# - Por ejemplo:
#     - `AdminUser` siempre tiene permisos
#     - `RegularUser` solo tiene permisos limitados (`"read"`, por ejemplo)
# - Ejemplo:
#     - Entrada:
        
#         ```python
#         user1 = AdminUser("Carlos")
#         user2 = RegularUser("Andrea")
#         ```
        
#     - Salida:
        
#         ```python
#         print(user1.has_permission("delete"))  # True
#         print(user2.has_permission("delete"))  # False
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self, name):
        pass
    
    @abstractmethod
    def has_permission(self):
        pass

class AdminUser(User):
    def __init__(self, name):
        self.name = name
        self.names = []
        self.permissions = [
            "read", 
            "write",
            "delete",
            "update",
            "create"
        ]

    def get_role(self, name):
        if name not in self.names:
            self.names.append(name)
        
    def has_permission(self, permission):
        return permission in self.permissions


class RegularUser(User):
    def __init__(self, name):
        self.name = name
        self.names = []
        self.permissions = [
            "read",
            "create"
        ]

    def get_role(self, name):
        if name not in self.names:
            self.names.append(name)
        
    def has_permission(self, permission):
        return permission in self.permissions

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False