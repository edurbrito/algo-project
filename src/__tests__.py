from generator import RandomDataGenerator
from point import Point
from kdtree import KDTree
from time import perf_counter
from random import randint

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
        "Agile",
        "Laravel",
        "Photoshop"
    ]

kdtree = KDTree(
    points = list(points.values()), 
    axes = axes
)

tests_passed = 0
total = 200
times = {"bs": [], "ln": []}

for _ in range(total):

    print('--------------------------------------------------------------')

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
    res_bs = kdtree.range_search(kdtree.root, ranges=ranges)
    bs_time = perf_counter() - bs_start

    ln_start = perf_counter()
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

    print(f"Test Passed: {_test_passed}")
    print(f"Ranges: {ranges}")
    print(f"BS: {bs_time} s")
    print(f"LN: {ln_time} s")

    tests_passed += int(_test_passed)
    times["bs"].append(bs_time)
    times["ln"].append(ln_time)

speedup = sum(times["ln"]) / sum(times["bs"])
print(f"\nTests Passed: {tests_passed}/{total}")
print(f"Speedup: {speedup}")