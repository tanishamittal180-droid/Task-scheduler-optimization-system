import pandas as pd


class Analytics:

    def compute_kpis(self, completed, missed):

        total = len(completed) + len(missed)

        return {
            "total_tasks": total,
            "completed": len(completed),
            "missed": len(missed),
            "success_rate": round(
                (len(completed) / total) * 100
                if total > 0 else 0,
                2
            )
        }

    def resource_utilization(self, completed):

        usage = {}

        for task in completed:

            r = task.get("assigned_resource", "Unknown")

            usage[r] = usage.get(r, 0) + task["duration"]

        return usage