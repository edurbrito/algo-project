import sys
import random as rd
import pandas as pd
from __words__ import *
from __skills__ import *

class RandomDataGenerator():

    def __init__(self, size: int, seed:int=None) -> None:
        if size <= 0: raise ValueError()

        self.size = size
        self.seed = seed

    def generate_ids(self) -> list[str]:
        """
        Generates random ids as nicknames/pseudonyms
        """

        self.rd = rd.Random(self.seed)
        
        _ids, ids = set(), list()

        if self.size <= 0:
            return []

        while len(_ids) < self.size:
            word1 = WORDS[self.rd.randint(0, len(WORDS)-1)]
            word2 = WORDS[self.rd.randint(0, len(WORDS)-1)]
            id = word1 + word2

            if id not in _ids:
                _ids.add(id)
                ids.append(id)
        
        return ids

    def generate_skills(self) -> list[str]:
        """
        Generates rows filled with random data. 
        Each row is assigned a job role and gets random values for each skill
        """

        self.rd = rd.Random(self.seed)

        default_dict = { k:0 for k in COLUMNS}
        rows = []

        for _ in range(self.size):
            row = default_dict.copy()

            # assign Role - Tech or No Tech Role
            irole = self.rd.randint(0, len(TECH_ROLES) + len(OTHER_ROLES)-1)
            role = TECH_ROLES[irole] if irole < len(TECH_ROLES) else OTHER_ROLES[irole-len(TECH_ROLES)]
            row[role] = 1
            
            # if Tech Role, set Programming and Systems skills
            if irole < len(TECH_ROLES):
                for p in PROGRAMMING + SYSTEMS:
                    row[p] = self.rd.randint(0,100)
            
            # Any Role, set Languages and Other skills
            for s in LANGUAGES + OTHER:
                row[s] = self.rd.randint(0,100)

            rows.append(row)
        
        return rows

    def generate_connections(self, ids:list[str], prob:int=0.01) -> dict:
        """
        Generates random connections between pairs of individuals with probability prob
        """

        self.rd = rd.Random(self.seed)

        connections = { id:{} for id in ids }

        for id1 in ids:
            for id2 in ids:
                if id1 != id2 and id2 not in connections[id1]:
                    if rd.randint(1,100)/100.0 <= prob:
                        weight = rd.randint(0,10)
                        connections[id1][id2] = weight
                        connections[id2][id1] = weight

        return connections

    def generate_database(self) -> list[tuple]:
        """
        Generates a random Database of the size specified
        """

        self.rd = rd.Random(self.seed)

        ids = self.generate_ids()
        skills = self.generate_skills()
        connections = self.generate_connections(ids)

        db = []

        for id in ids:
            _skills = skills.pop(self.rd.randint(0, len(skills)-1))
            _connections = connections[id]
            db.append((id, _skills, _connections))

        return db

if __name__ == '__main__':
    
    try:
        if len(sys.argv) < 2:
            raise Exception()

        SIZE = int(sys.argv[1])
        SEED = None

        if len(sys.argv) >= 3:
            SEED = int(sys.argv[2])
        
    except Exception as e:
        print("""Usage: generator.py size:int [seed:int]""")
        exit(1)

    generator = RandomDataGenerator(SIZE, SEED)
    db = generator.generate_database()

    dt_skills = pd.DataFrame(columns=["id"] + COLUMNS)
    dt_connections = pd.DataFrame(columns=["id"] + [id for id,_,_ in db])
    
    i = 0

    for id,skills,connections in db:
        row_skills = {"id":id}
        row_connections = {"id":id}
        
        row_skills.update(skills)
        dt_skills = dt_skills.append(row_skills, ignore_index=True)

        row_connections.update(connections)
        dt_connections = dt_connections.append(row_connections, ignore_index=True)
        
        i += 1
        print(f"Progress: {i}/{SIZE}" + " "*10, end="\r")

    dt_skills.to_csv("./skills.csv", index=False)
    dt_connections.to_csv("./connections.csv", index=False)