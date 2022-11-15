class User:
    def __init__(self,id:str, preference:str) -> None:
        """
        clase constructor del usuario
        """
        self.id = id
        self.preference = preference

    def __repr__(self) -> str:
        return self.id