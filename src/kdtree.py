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
        self.search_result = []
        self.search_steps = 0

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



    def bfs_search(self, node: 'KDTreeNode', ranges, step=0):
        self.search_steps += 1
        if step == len(self.axes):
            step = 0

        if node == None:
            return self.search_result
        else:
            canAdded = True
            for i in range(len(ranges)):
                if len(ranges[i]) > 0:
                    min, max = int(ranges[i].split('|')[0]), int(ranges[i].split('|')[1])
                    if min > node.point[self.axes[i]] or node.point[self.axes[i]] > max:
                        canAdded = False
                        break
            if canAdded:
                self.search_result.append(node)

            if len(ranges[step]) > 0:
                min, max = int(ranges[step].split('|')[0]), int(ranges[step].split('|')[1])
                if min <= node.point[self.axes[step]] and node.point[self.axes[step]] <= max:
                    if node.left_child != None:
                        step+=1
                        self.search_result.extend(self.bfs_search(node.left_child, ranges, step))
                    if node.right_child != None:
                        step+=1
                        self.search_result.extend(self.bfs_search(node.right_child, ranges, step))

                elif min > node.point[self.axes[step]]:
                    step+=1
                    self.search_result.extend(self.bfs_search(node.right_child, ranges, step))
                elif max < node.point[self.axes[step]]:
                    step+=1
                    self.search_result.extend(self.bfs_search(node.left_child, ranges, step))
            else:
                step+=1
                if node.left_child != None:
                    self.search_result.extend(self.bfs_search(node.left_child, ranges, step))
                if node.right_child != None:
                    self.search_result.extend(self.bfs_search(node.right_child, ranges, step))

        return list(set(self.search_result))