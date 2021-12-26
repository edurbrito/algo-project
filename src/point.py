class Point():

    def __init__(self, id:str, coordinates:dict[str:int]) -> None:
        self.id = id
        self.coordinates = coordinates

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f"{self.id}: {self.coordinates}"

    def __sizeof__(self) -> int:
        return len(self.coordinates)