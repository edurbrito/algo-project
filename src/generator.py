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

    def generate_database(self) -> list[tuple]:
        """
        Generates a random Database of the size specified
        """

        self.rd = rd.Random(self.seed)

        ids = self.generate_ids()
        skills = self.generate_skills()

        db = []

        for id in ids:
            _skills = skills.pop(self.rd.randint(0, len(skills)-1))
            db.append((id,_skills))

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

    dt = pd.DataFrame(columns=["id"] + COLUMNS)

    for id,skills in db:
        row = {"id":id}
        row.update(skills)
        dt = dt.append(row, ignore_index=True)

    dt.to_csv("./out.csv", index=False)