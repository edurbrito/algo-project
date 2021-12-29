from point import Point

class KDTreeNode():

    def __init__(self, point:'Point', left_child:'KDTreeNode'=None, right_child:'KDTreeNode'=None) -> None:
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return self.point.id

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, __name: str) -> int:
        return self.point[__name]

class KDTree():

    def __init__(self, points:list, axes:list) -> None:
        self.points = points
        self.axes = axes
        self.root = self.__build(self.points)

    def __build(self, points:list, depth:int = 0) -> 'KDTreeNode':

        if not points:
            return None

        k = len(self.axes)

        axis = depth % k

        points.sort(key=lambda p: p[self.axes[axis]])

        median = len(points) // 2

        node = KDTreeNode(point = points[median])

        left_child = self.__build(points[ : median], depth=depth+1)
        right_child = self.__build(points[median + 1 : ], depth=depth+1)

        node.left_child, node.right_child = left_child, right_child

        return node

    def bfs_print(self, node, k=0):
        if node:
            self.bfs_print(node.right_child, k + 1)
            print(' ' * ((len(self.axes) * 4 + 5) * k) + '--| ' + str([node[a] for a in self.axes]))
            self.bfs_print(node.left_child, k + 1)
