class Point():

    def __init__(self, id:str, coordinates, connections) -> None:
        self.id = id
        self.coordinates = coordinates
        self.connections = connections

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f"{self.id}: {self.coordinates}"

    def __sizeof__(self) -> int:
        return len(self.coordinates)

    def __getitem__(self, __name: str) -> int:
        return self.coordinates[__name]

    def in_range(self, axis, range):
        return range[0] <= self[axis] <= range[1]