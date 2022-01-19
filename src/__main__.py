"""
Example: Generating Points objects
"""

from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree

generator = RandomDataGenerator(1000, 111)
db = generator.generate_database()

points = {}

for id, skills, connections in db:
    p = Point(id, skills, connections)
    points[id] = p

axes = [   
        "English", 
        "Python",
        "Communication",
        "Agile"
    ]

kdtree = KDTree(
    points = list(points.values()), 
    axes = axes
)

kdtree.bfs_print(kdtree.root)

result = kdtree.range_search(kdtree.root, ranges=[(10,60), (0,30), None, (20,25)])

for item in result:
    print(item, str([item.point.coordinates[a] for a in kdtree.axes]))