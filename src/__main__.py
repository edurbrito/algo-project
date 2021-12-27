"""
Example: Generating Points objects
"""

from generator import RandomDataGenerator
from point import Point

generator = RandomDataGenerator(1000,11)
db = generator.generate_database()

points = []

for id,skills in db:
    p = Point(id, skills)
    print(p)
    points.append(p)
