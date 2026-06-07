from collections import defaultdict
from collections import deque


class DependencyGraph:

    def __init__(self):

        self.graph = defaultdict(list)

        self.indegree = defaultdict(int)

    def add_edge(
        self,
        parent,
        child
    ):

        self.graph[parent].append(
            child
        )

        self.indegree[child] += 1

    def topological_sort(
        self,
        tasks
    ):

        queue = deque()

        for task in tasks:

            task_id = task["task_id"]

            if self.indegree[
                task_id
            ] == 0:

                queue.append(
                    task_id
                )

        order = []

        while queue:

            node = queue.popleft()

            order.append(node)

            for neighbor in self.graph[node]:

                self.indegree[
                    neighbor
                ] -= 1

                if (
                    self.indegree[
                        neighbor
                    ] == 0
                ):

                    queue.append(
                        neighbor
                    )

        return order