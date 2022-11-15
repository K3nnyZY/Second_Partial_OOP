from abc import ABC, abstractmethod

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