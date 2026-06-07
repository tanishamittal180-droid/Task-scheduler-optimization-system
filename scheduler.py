import heapq

from backend.resource_allocator import (
    ResourceAllocator
)


class Scheduler:

    def __init__(
        self,
        tasks,
        resources
    ):

        self.tasks = tasks
        self.resources = resources

    def optimize(self):

        allocator = (
            ResourceAllocator()
        )

        heap = []

        for task in self.tasks:

            heapq.heappush(

                heap,

                (
                    -int(task.get(
                        "priority",
                        1
                    )),

                    int(task.get(
                        "deadline",
                        999
                    )),

                    task
                )
            )

        completed = []
        missed = []

        current_time = 0

        total_profit = 0

        while heap:

            _, _, task = (
                heapq.heappop(
                    heap
                )
            )

            resource = (
                allocator
                .assign_resource(
                    task,
                    self.resources
                )
            )

            start = current_time

            finish = (
                current_time
                +
                int(task.get(
                    "duration",
                    1
                ))
            )

            task[
                "start_time"
            ] = start

            task[
                "finish_time"
            ] = finish

            if resource:

                task[
                    "assigned_resource"
                ] = resource.get(
                    "resource_name",
                    "Unassigned"
                )

            else:

                task[
                    "assigned_resource"
                ] = "Unassigned"

            if finish <= int(
                task.get(
                    "deadline",
                    999
                )
            ):

                task[
                    "status"
                ] = "Completed"

                completed.append(
                    task
                )

                total_profit += int(
                    task.get(
                        "profit",
                        0
                    )
                )

            else:

                task[
                    "status"
                ] = "Missed"

                missed.append(
                    task
                )

            current_time = finish

        return (
            completed,
            missed,
            total_profit
        )
