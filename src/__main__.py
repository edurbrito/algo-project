"""
Example: Generating Points objects
"""

from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree

generator = RandomDataGenerator(31)
db = generator.generate_database()

points = {}

for id, skills, connections in db:
    p = Point(id, skills, connections)
    points[id] = p

kdtree = KDTree(
    points = list(points.values()), 
    axes = [   
        "English", 
        "Python",
        "Communication",
        "Agile"
    ]
)

kdtree.bfs_print(kdtree.root)