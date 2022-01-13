"""
Example: Generating Points objects
"""

from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree

generator = RandomDataGenerator(10)
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

res = kdtree.bfs_search(kdtree.root, ranges=['10|60', '', '10|40', ''])


for item in res:
    # print()
    for ax in axes:
        print(item.point.coordinates[ax], end=' ')
    
    print('\n')

print(kdtree.steps)