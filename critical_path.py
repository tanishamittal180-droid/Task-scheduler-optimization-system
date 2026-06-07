class CriticalPath:
    
    def calculate(
        self,
        tasks
    ):

        longest = 0

        path = []

        current = []

        total = 0

        for task in tasks:

            current.append(
                task["task_id"]
            )

            total += task[
                "duration"
            ]

            if total > longest:

                longest = total

                path = current.copy()

        return {

            "critical_path":
                path,

            "duration":
                longest
        }