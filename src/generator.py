import sys
import random as rd
import pandas as pd
from __words__ import *
from __skills__ import *

class RandomDataGenerator():

    def __init__(self, size: int) -> None:
        if size <= 0: raise ValueError()

        self.size = size

    def generate_ids(self) -> list[str]:
        """
        Generates random ids as nicknames/pseudonyms
        """
        
        ids = set()

        if self.size <= 0:
            return []

        while len(ids) < self.size:
            word1 = WORDS[rd.randrange(0, len(WORDS))]
            word2 = WORDS[rd.randrange(0, len(WORDS))]
            id = word1 + word2

            if id not in ids:
                ids.add(id)
        
        return list(ids)

    def generate_skills(self) -> list[str]:
        """
        Generates rows filled with random data. 
        Each row is assigned a job role and gets random values for each skill
        """

        default_dict = { k:0 for k in COLUMNS}
        rows = []

        for _ in range(self.size):
            row = default_dict.copy()

            # assign Role - Tech or No Tech Role
            irole = rd.randrange(0, len(TECH_ROLES) + len(OTHER_ROLES))
            role = TECH_ROLES[irole] if irole < len(TECH_ROLES) else OTHER_ROLES[irole-len(TECH_ROLES)]
            row[role] = 1
            
            # if Tech Role, set Programming and Systems skills
            if irole < len(TECH_ROLES):
                for p in PROGRAMMING + SYSTEMS:
                    row[p] = rd.randrange(0,100)
            
            # Any Role, set Languages and Other skills
            for s in LANGUAGES + OTHER:
                row[s] = rd.randrange(0,100)

            rows.append(row)
        
        return rows

    def generate_database(self) -> list[tuple]:
        """
        Generates a random Database of the size specified
        """

        ids = self.generate_ids()
        skills = self.generate_skills()

        db = []

        for id in ids:
            _skills = skills.pop(rd.randrange(0, len(skills)))
            db.append((id,_skills))

        return db

if __name__ == '__main__':
    
    try:
        if len(sys.argv) < 2:
            raise Exception()

        SIZE = int(sys.argv[1])
        
        if len(sys.argv) >= 3:
            rd.seed(int(sys.argv[2]))

    except Exception as e:
        print("""Usage: generator.py size:int [seed:int]""")
        exit(1)

    generator = RandomDataGenerator(SIZE)
    db = generator.generate_database()

    dt = pd.DataFrame(columns=["id"] + COLUMNS)

    for id,skills in db:
        row = {"id":id}
        row.update(skills)
        dt = dt.append(row, ignore_index=True)

    dt.to_csv("./out.csv", index=False)