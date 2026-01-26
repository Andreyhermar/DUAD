#  Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class Human:
    def __init__(self, gender):
        self.gender = gender

def female_only(func):
    def exclusion_gender(user, *args, **kwargs):
        print(f"Parameters: ",user, *args, **kwargs)
        if user.gender != "female":
            raise ValueError("It's a male, go to the males code")
        result = func(user, *args, **kwargs)
        print(f"Return: ", result)
        return result
    return exclusion_gender

@female_only
def female_info(user, hair_color, eye_color):
    print(f"{user.gender} {hair_color} {eye_color}")

u1 = Human("female")
female_info(u1, "blond", "green")

u2 = Human("male")
female_info(u2, "black", "blue")

