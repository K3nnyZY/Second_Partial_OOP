from abc import ABC, abstractmethod
from typing import List

class AbstractMovie(ABC):
    def __init__(self, movie:str, time:str) -> None:
        """
        clase abstracta constructor de movie
        """
        self.movie = movie
        self.time = time
        self.vip = 0
        self.regular = 0

    @abstractmethod
    def plump(self):
       pass


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


class User:
    def __init__(self,id:str, preference:str) -> None:
        """
        clase constructor del usuario
        """
        self.id = id
        self.preference = preference

    def __repr__(self) -> str:
        return self.id


class Cine:
    def __init__(self, seat_vip:int, seat_regular:int) -> None:
        """
        clase constructor del cine
        """
        self.seat_vip = seat_vip
        self.seat_regular = seat_regular
        self.users = []
        self.movies = []


    def add_user(self,id:str, preference:str):
        """
        Añade un usario nuevo
        """
        self.users.append(User(id,preference))
        print(f"la preferencia de {id}, es {preference}")


    def user_register(self, id:str):
        """
        Encuentra el resitro de los usuarios
        """
        p = False
        user:User
        for user in self.users:
            if user.id == id:
                p = True
        return p


    def add_films(self, movies:List[Movie]):
        """
        Añade todas las peliculas en una lista, y lo muestra
        """
        for film in movies:
            film.vip = self.seat_vip
            film.regular = self.seat_regular
            self.movies.append(film)
            for film in self.movies:
                print(film)


    def available(self,A_movie:str):
        """
        muestra la disponibilidad de la pelicula de la lista
        """
        p = False
        P_movie:Movie
        for P_movie in self.movies:
            if P_movie.movie == A_movie:
                print(f"la pelicula, {A_movie}, esta disponible")
                p = P_movie            
        return p
            

    def sell(self, id:str, movie:int, time:str, vip:int, regular:int):
        """
        vende los ticketes segun la disponibilidad de vip o regular y revisa
        si el usuario esta registrado para su preferencia
        """
        user = self.user_register(id)
        if user:
            A_movie = self.available(movie)
            while A_movie == None:
                print(f"la pelicula, {movie}, no esta disponible")
            if A_movie:
                if A_movie.vip<vip:
                    print("no hay disponibilidad para VIP")
                if A_movie.vip>vip:
                    print(f"{vip} VIP tickets vendidos")
                    A_movie.vip = A_movie.vip - vip

                if A_movie.regular<regular:
                    print("no hay disponibilidad para regular")
                if A_movie.regular>regular:
                    print(f"{regular} regular tickets vendidos")
                    A_movie.regular = A_movie.regular - regular
        else:
            print(f"el usuario {id} no esta registrado")



    