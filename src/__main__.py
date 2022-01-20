"""
Example: Range Search over 1000 points and 4 different axes
"""

from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree

# Generate Random Database of Employees with 1000 points
generator = RandomDataGenerator(1000, 111)
db = generator.generate_database()

points = {}

# Create the Points objects
for id, skills, connections in db:
    p = Point(id, skills, connections)
    points[id] = p

# Choose the axes to search with
axes = [   
        "English", 
        "Python",
        "Communication",
        "Agile"
    ]

# Build the KDTree
kdtree = KDTree(
    points = list(points.values()), 
    axes = axes
)

# Print the KDTree
kdtree.bfs_print(kdtree.root)

# Range Search through the points based on specific ranges
result = kdtree.range_search(kdtree.root, ranges=[(10,60), (0,30), None, (20,25)])

# Print the resulting points that fit into the range search
print("\nRange Search Result:\n")
for item in result:
    print(item, str([item.point.coordinates[a] for a in kdtree.axes]))