from AbstractClass import AbstractMovie

class Movie(AbstractMovie):
    """
    Esta clase es un decorador de property en la cual el metodo atributo
    sera una propiedad
    """
    @property
    def plump(self):
        if self.vip and self.regular == 0:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Pelicula: {self.movie} -> {self.time}"

