from point import Point

class KDTreeNode():

    def __init__(self, point: 'Point', left_child: 'KDTreeNode' = None, right_child: 'KDTreeNode' = None) -> None:
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return self.point.id

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, __name: str) -> int:
        return self.point[__name]

    def in_range(self, axis, range):
        return self.point.in_range(axis, range)


class KDTree():

    def __init__(self, points: list, axes: list) -> None:
        self.points = points
        self.axes = axes
        self.root = self.__build(self.points)

    def __build(self, points: list, depth: int = 0) -> 'KDTreeNode':
        """
        Build the KDTree based on the specified axes and return the root node
        """

        if not points:
            return None

        k = len(self.axes)

        axis = depth % k

        points.sort(key=lambda p: p[self.axes[axis]])

        median = len(points) // 2

        node = KDTreeNode(point=points[median])

        left_child = self.__build(points[: median], depth=depth+1)
        right_child = self.__build(points[median + 1:], depth=depth+1)

        node.left_child, node.right_child = left_child, right_child

        return node

    def bfs_print(self, node, k=0):
        """
        Print the KDTree in a BFS fashion
        """

        if node:
            self.bfs_print(node.right_child, k + 1)
            print(' ' * ((len(self.axes) * 4 + 5) * k) +
                  '--| ' + str([node[a] for a in self.axes]))
            self.bfs_print(node.left_child, k + 1)

    def range_search(self, node: 'KDTreeNode', ranges: list, level=0) -> list:
        """
        Range Search through the list of points and return the points that fit
        """
        
        if not node:
            return []
        else:
            _len = len(ranges)
            _level = level % _len

            result = []

            if all([node.in_range(self.axes[r], ranges[r]) if ranges[r] else True for r in range(_len)]):
                result.append(node)

            if ranges[_level]:
                min, max = ranges[_level][0], ranges[_level][1]

                if node.in_range(self.axes[_level], ranges[_level]):
                    if node.left_child:
                        result.extend(
                            self.range_search(node.left_child, ranges, level+1))
                    if node.right_child:
                        result.extend(
                            self.range_search(node.right_child, ranges, level+1))
                elif min > node[self.axes[_level]]:
                    result.extend(
                        self.range_search(node.right_child, ranges, level+1))
                elif max < node[self.axes[_level]]:
                    result.extend(
                        self.range_search(node.left_child, ranges, level+1))
            else:
                if node.left_child:
                    result.extend(
                        self.range_search(node.left_child, ranges, level+1))
                if node.right_child:
                    result.extend(
                        self.range_search(node.right_child, ranges, level+1))
        return result

    def linear_search(self, ranges: list) -> list:
        """
        Linear Search through the list of points and return the points that fit
        """

        _len = len(ranges)
        result = []

        for point in self.points:
            if all([point.in_range(self.axes[r], ranges[r]) if ranges[r] else True for r in range(_len)]):
                result.append(point)
                
        return result
