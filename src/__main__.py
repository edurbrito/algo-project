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

print('Going throw the following nodes while searching the ranges...')
res = kdtree.bfs_search(kdtree.root, ranges=['10|60', '0|30', '10|40', ''])
print('--------------------------------------------------------------\n')

print('Finding the following nodes in ranges...')
for item in res:
    # print()
    print(str([item.point.coordinates[a] for a in kdtree.axes]))
    # for ax in axes:
    #     print(item.point.coordinates[ax], end=' ')

print(kdtree.search_steps)