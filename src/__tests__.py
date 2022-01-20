from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree
from time import perf_counter
from random import randint
import pandas as pd

# Generate Random Database of Employees with 10000 points
generator = RandomDataGenerator(10000, 111)
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
        "Agile",
        "Laravel",
        "Photoshop",
        "Management",
        "Django",
        "Kubernetes",
        "Team working"
    ]

# Create a DataFrame to store the speedup measurements
dt = pd.DataFrame(columns=["points", "axes", "speedup"])

# Build KDTrees of Multiple Sizes
for _lpoints in [100, 500, 1000, 5000, 10000]:
    # Search with multiple combinations of axes
    for _laxes in [2,4,6,8,10]:

        _points = list(points.values())[:_lpoints]
        axes = axes[:_laxes]

        build_start = perf_counter()
        # Build the KDTree
        kdtree = KDTree(
            points = _points, 
            axes = axes
        )
        build_time = perf_counter() - build_start

        tests_passed = 0
        # Set the number of successive queries
        total = 20
        times = {"bs": [], "ln": []}

        for _ in range(total):

            # print('--------------------------------------------------------------')

            ranges = []

            for i in range(len(axes)):
                a, b = 0, 0
                while a == b:
                    a = randint(0,100)
                    b = randint(0,100)
                
                if randint(0,5) >= 2:
                    ranges.append((min(a,b), max(a,b)))
                else:
                    ranges.append(None)

            bs_start = perf_counter()
            # Perform range search
            res_bs = kdtree.range_search(kdtree.root, ranges=ranges)
            bs_time = perf_counter() - bs_start

            ln_start = perf_counter()
            # Perform linear search
            res_ln = kdtree.linear_search(ranges=ranges)
            ln_time = perf_counter() - ln_start

            _res_bs = []

            for item in res_bs:
                _res_bs.append([item.point.coordinates[a] for a in kdtree.axes])

            _res_bs.sort()

            _res_ln = []

            for item in res_ln:
                _res_ln.append([item.coordinates[a] for a in kdtree.axes])

            _res_ln.sort()

            _test_passed = _res_bs == _res_ln

            # print(f"Test Passed: {_test_passed}")
            # print(f"Ranges: {ranges}")
            # print(f"BS: {bs_time} s")
            # print(f"LN: {ln_time} s")

            tests_passed += int(_test_passed)
            times["bs"].append(bs_time)
            times["ln"].append(ln_time)

        speedup = sum(times["ln"]) / (sum(times["bs"]) + build_time)
        print(f"\nTests Passed: {tests_passed}/{total}")
        print(f"Points: {_lpoints}, Axes: {_laxes}")
        print(f"Speedup: {speedup}")
        dt = dt.append({"points": _lpoints, "axes": _laxes, "speedup": speedup}, ignore_index=True)

dt.to_csv("speedup.csv")